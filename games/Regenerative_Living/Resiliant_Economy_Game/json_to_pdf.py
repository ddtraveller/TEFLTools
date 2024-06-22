import json
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import inch

def create_cards(data, filename):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []
    for card_type in ['resource_cards', 'need_cards', 'event_cards']:
        elements.append(Table([[card_type.replace('_', ' ').upper()]],
                        style=[('BACKGROUND', (0, 0), (-1, -1), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, -1), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                               ('FONTSIZE', (0, 0), (-1, -1), 14),
                               ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                               ('BACKGROUND', (0, 0), (-1, -1), colors.grey)]))
        elements.append(Table([['']]))  # Add some space
        for card in data[card_type]:
            if card_type == 'event_cards':
                card_data = [
                    [card['event']],
                    [card['description']],
                    [card['effect']]
                ]
            else:
                if card_type == 'resource_cards':
                    card_key = 'resource'
                else:
                    card_key = 'need'

                card_data = [
                    [f"Type: {card['type']}"],
                    [f"{'Resource' if card_type == 'resource_cards' else 'Need'}: {card[card_key]}"],
                    [f"Quantity: {card['quantity']}"]
                ]

            t = Table(card_data, colWidths=[4*inch])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.beige),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('TOPPADDING', (0, 0), (-1, -1), 5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(t)
            elements.append(Table([['']]))  # Add some space
    doc.build(elements)

# Load the JSON data
with open('Activity_Cards.json', 'r') as f:
    data = json.load(f)

# Create the PDF
create_cards(data, 'Activity_Cards.pdf')
print("Cards have been created and saved as 'Activity_Cards.pdf'")