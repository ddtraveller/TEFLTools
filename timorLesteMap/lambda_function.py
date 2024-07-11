import json
import folium
import boto3
import csv
import io
import random
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3', region_name='us-west-2')
bucket_name = 'tl-web'
map_key = 'index.html'
csv_key = 'map_data.csv'
color_list = ['darkblue', 'lightgray', 'black', 'cadetblue', 'purple', 'lightred', 'green', 'lightblue', 'beige', 'lightgreen', 'blue', 'darkpurple', 'darkred', 'orange', 'red', 'gray', 'darkgreen', 'white', 'pink']

def get_color_for_category(category, category_colors):
    if category in category_colors:
        return category_colors[category]
    else:
        unused_colors = list(set(color_list) - set(category_colors.values()))
        if unused_colors:
            new_color = random.choice(unused_colors)
        else:
            new_color = random.choice(color_list)
        category_colors[category] = new_color
        return new_color

def lambda_handler(event, context):
    try:
        # Parse the SMS message from the SNS event
        sms_message = json.loads(event['Records'][0]['Sns']['Message'])
        message_body = sms_message['messageBody']
        logger.info(f"Received SMS message: {message_body}")

        # Split the SMS message to extract the marker data
        message_parts = message_body.split()
        
        if len(message_parts) < 3:
            raise ValueError("Invalid message format. Expected at least 3 parts.")

        action = message_parts[0].lower()
        if action not in ['add', 'drop']:
            raise ValueError(f"Invalid action: {action}. Expected 'add' or 'drop'.")

        # Skip the word "marker" if it's present
        coord_index = 2 if message_parts[1].lower() == 'marker' else 1

        try:
            lat, lon = map(float, message_parts[coord_index].split(','))
            if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
                raise ValueError(f"Invalid coordinate range: Lat {lat}, Lon {lon}")
        except ValueError as e:
            raise ValueError(f"Invalid coordinates: {message_parts[coord_index]}. Expected format: lat,lon. {str(e)}")

        label = ' '.join(message_parts[coord_index+1:]) if len(message_parts) > coord_index+1 else ''

        logger.info(f"Parsed data: Action: {action}, Lat: {lat}, Lon: {lon}, Label: {label}")

        # Try to read the existing CSV file from S3
        try:
            csv_content = s3.get_object(Bucket=bucket_name, Key=csv_key)['Body'].read().decode('utf-8')
            csv_data = csv.reader(io.StringIO(csv_content))
            markers = list(csv_data)
            logger.info(f"Loaded {len(markers)} markers from CSV")
        except s3.exceptions.NoSuchKey:
            logger.info("CSV file not found. Initializing new data.")
            markers = []
        except boto3.exceptions.BotoServerError as e:
            logger.error(f"AWS service error: {str(e)}")
            raise

        # Create a new map centered on Dili
        dili_map = folium.Map(location=[-8.5579, 125.5736], zoom_start=13)

        # Generate marker colors based on unique item types in the CSV
        category_colors = {}
        logger.info(f"Processing existing markers: {markers}")
        for marker in markers:
            if len(marker) >= 3:
                category = marker[2]
                if len(marker) > 3:
                    category_colors[category] = marker[3]
                else:
                    get_color_for_category(category, category_colors)
            else:
                logger.warning(f"Skipping invalid marker: {marker}")

        logger.info(f"Category colors after processing existing markers: {category_colors}")

        # Generate the legend HTML dynamically from the marker colors
        legend_html = """
        <div style="position: fixed; bottom: 50px; left: 50px; width: 140px; border:2px solid grey; z-index:9999; font-size:14px; background-color: white; padding: 10px;">
        """

        # Process the marker data
        logger.info(f'Action: {action}')
        if action == 'add':
            color = get_color_for_category(label, category_colors)
            new_marker = [str(lat), str(lon), label, color]
            markers.append(new_marker)
            logger.info(f"Added new marker: {new_marker}")
        elif action == 'drop':
            # Remove the marker from the CSV if it exists
            markers = [marker for marker in markers if marker[:2] != [str(lat), str(lon)]]
            logger.info(f"Markers after drop: {markers}")

        # Add markers to the map
        for marker in markers:
            if len(marker) >= 4:
                lat2, lon2, label2, color2 = marker
                folium.Marker(
                    [float(lat2), float(lon2)],
                    popup=label2,
                    icon=folium.Icon(color=color2)
                ).add_to(dili_map)
                legend_html += f'<p style="margin: 0;"><span style="color: {color2}">&#9679;</span> {label2}</p>'
            else:
                logger.warning(f"Skipping invalid marker: {marker}")

        legend_html += '</div>'
        dili_map.get_root().html.add_child(folium.Element(legend_html))

        # Generate the updated map HTML
        updated_map_html = dili_map.get_root().render()

        # Add the favicon link to the HTML head
        favicon_link = '<link rel="icon" type="image/x-icon" href="https://tarotcardsstyles.s3.us-west-2.amazonaws.com/favicon.ico">'
        updated_map_html = updated_map_html.replace('<head>', f'<head>\n    {favicon_link}')

        # Generate the updated CSV content
        updated_csv_content = io.StringIO()
        csv_writer = csv.writer(updated_csv_content)
        csv_writer.writerows(markers)

        # Upload the updated map HTML and CSV to S3
        s3.put_object(Bucket=bucket_name, Key=map_key, Body=updated_map_html.encode('utf-8'), ContentType='text/html')
        s3.put_object(Bucket=bucket_name, Key=csv_key, Body=updated_csv_content.getvalue().encode('utf-8'), ContentType='text/csv')

        logger.info("Map and CSV updated successfully")
        return {
            'statusCode': 200,
            'body': json.dumps('Map and CSV updated successfully!')
        }

    except Exception as e:
        logger.error(f"Error processing message: {str(e)}", exc_info=True)
        return {
            'statusCode': 400,
            'body': json.dumps(f'Error processing message: {str(e)}')
        }