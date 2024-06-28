import json
import folium
import boto3
import csv
import io
import random

s3 = boto3.client('s3', region_name='us-west-2')
bucket_name = 'tl-web'
map_key = 'index.html'
csv_key = 'map_data.csv'
color_list = ['darkblue', 'lightgray', 'black', 'cadetblue', 'purple', 'lightred', 'green', 'lightblue', 'beige', 'lightgreen', 'blue', 'darkpurple', 'darkred', 'orange', 'red', 'gray', 'darkgreen', 'white', 'pink']

def generate_random_color():
    return random.choice(color_list)

def lambda_handler(event, context):
    try:
        # Parse the SMS message from the SNS event
        sms_message = event['Records'][0]['Sns']['Message']
        print(f"Received SMS message: {sms_message}")

        # Split the SMS message to extract the marker data
        message_parts = sms_message.split()
        
        if len(message_parts) < 3:
            raise ValueError("Invalid message format. Expected at least 3 parts.")

        action = message_parts[0].lower()
        if action not in ['add', 'drop']:
            raise ValueError(f"Invalid action: {action}. Expected 'add' or 'drop'.")

        # Skip the word "marker" if it's present
        coord_index = 2 if message_parts[1].lower() == 'marker' else 1

        try:
            lat, lon = message_parts[coord_index].split(',')
            lat, lon = float(lat), float(lon)
        except ValueError:
            raise ValueError(f"Invalid coordinates: {message_parts[coord_index]}. Expected format: lat,lon")

        label = ' '.join(message_parts[coord_index+1:]) if len(message_parts) > coord_index+1 else ''

        print(f"Parsed data: Action: {action}, Lat: {lat}, Lon: {lon}, Label: {label}")

        # Try to read the existing CSV file from S3
        try:
            csv_content = s3.get_object(Bucket=bucket_name, Key=csv_key)['Body'].read().decode('utf-8')
            csv_data = csv.reader(io.StringIO(csv_content))
            markers = list(csv_data)
        except s3.exceptions.NoSuchKey:
            # If the CSV file doesn't exist, initialize an empty list for markers
            markers = []

        # Create a new map centered on Dili
        dili_map = folium.Map(location=[-8.5579, 125.5736], zoom_start=13)

        # Generate marker colors based on unique item types in the CSV
        marker_colors = {}
        print("Markers: ")
        print(markers)
        for marker in markers:
            labelx = marker[2]
            if labelx not in marker_colors:
                marker_colors[labelx] = marker[3] if len(marker) > 3 else generate_random_color()

        # Generate the legend HTML dynamically from the marker colors
        legend_html = """
        <div style="position: fixed; bottom: 50px; left: 50px; width: 140px; border:2px solid grey; z-index:9999; font-size:14px; background-color: white; padding: 10px;">
        """

        # Process the marker data
        print('action ' + action)
        if action == 'add':
            color = color_list[len(markers) % len(color_list)]
            marker_colors[label] = color
            
            markers.append([str(lat), str(lon), label, color])

        elif action == 'drop':
            # Remove the marker from the CSV if it exists
            markers = [marker for marker in markers if marker[:2] != [str(lat), str(lon)]]

        # Add markers to the map
        for marker in markers:
            lat2, lon2, label2, color2 = marker
            folium.Marker(
                [float(lat2), float(lon2)],
                popup=label2,
                icon=folium.Icon(color=color2)
            ).add_to(dili_map)
            legend_html += f'<p style="margin: 0;"><span style="color: {color2}">&#9679;</span> {label2}</p>'

        legend_html += '</div>'
        dili_map.get_root().html.add_child(folium.Element(legend_html))

        # Generate the updated map HTML
        updated_map_html = dili_map.get_root().render()

        # Generate the updated CSV content
        updated_csv_content = io.StringIO()
        csv_writer = csv.writer(updated_csv_content)
        csv_writer.writerows(markers)

        # Upload the updated map HTML and CSV to S3
        s3.put_object(Bucket=bucket_name, Key=map_key, Body=updated_map_html.encode('utf-8'), ContentType='text/html')
        s3.put_object(Bucket=bucket_name, Key=csv_key, Body=updated_csv_content.getvalue().encode('utf-8'), ContentType='text/csv')

        return {
            'statusCode': 200,
            'body': json.dumps('Map and CSV updated successfully!')
        }

    except Exception as e:
        print(f"Error processing message: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps(f'Error processing message: {str(e)}')
        }