import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Read the CSV data
data = pd.read_csv('drought_proofing_measures.csv')

# Create a PDF to save the slides
pdf = PdfPages('drought_proofing_measures_presentation.pdf')

# Set the style for the plots
plt.style.use('ggplot')

# Function to create a new figure (slide)
def create_slide():
    return plt.figure(figsize=(11, 8.5))

# Function to safely extract min and max costs
def extract_cost(x):
    try:
        if ' to ' in x:
            return [float(val) for val in x.split(' to ')]
        else:
            return [float(x), float(x)]
    except:
        return [float('nan'), float('nan')]

# Slide 1: Title
fig = create_slide()
plt.axis('off')
plt.text(0.5, 0.5, 'Drought Proofing Measures in Southern India', 
         fontsize=24, ha='center', va='center')
pdf.savefig(fig)
plt.close()

# Slide 2: Adoption Rates
fig = create_slide()
adoption_data = data[data['adoption_rate'].notna() & (data['adoption_rate'] != 'N/A')]
adoption_data.loc[:, 'adoption_rate'] = pd.to_numeric(adoption_data['adoption_rate'], errors='coerce')
adoption_data = adoption_data.dropna(subset=['adoption_rate'])
plt.bar(adoption_data['measure'], adoption_data['adoption_rate'])
plt.title('Adoption Rates of Drought Proofing Measures')
plt.xlabel('Measure')
plt.ylabel('Adoption Rate (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
pdf.savefig(fig)
plt.close()

# Slide 3: Cost per Cubic Meter
fig = create_slide()
cost_data = data[data['cost_per_cubic_meter'].notna() & (data['cost_per_cubic_meter'] != 'N/A')].copy()
cost_data[['min_cost', 'max_cost']] = cost_data['cost_per_cubic_meter'].apply(extract_cost).tolist()
cost_data = cost_data.dropna(subset=['min_cost', 'max_cost'])
plt.barh(cost_data['measure'], cost_data['max_cost'], alpha=0.5, label='Max Cost')
plt.barh(cost_data['measure'], cost_data['min_cost'], alpha=0.5, label='Min Cost')
plt.title('Cost per Cubic Meter of Water')
plt.xlabel('Cost (₹/m³)')
plt.ylabel('Measure')
plt.legend()
plt.tight_layout()
pdf.savefig(fig)
plt.close()

# Slide 4: Rate of Return
fig = create_slide()
return_data = data[data['rate_of_return'].notna()].copy()
return_data.loc[:, 'rate_of_return'] = pd.to_numeric(return_data['rate_of_return'], errors='coerce')
return_data = return_data.dropna(subset=['rate_of_return'])
plt.bar(return_data['measure'], return_data['rate_of_return'])
plt.title('Rate of Return for Different Measures')
plt.xlabel('Measure')
plt.ylabel('Rate of Return (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
pdf.savefig(fig)
plt.close()

# Slide 5: Benefits Comparison
fig = create_slide()
plt.axis('off')
plt.title('Benefits of Different Measures')
text = '\n'.join([f"{row['measure']}: {row['benefit']}" for _, row in data.iterrows()])
plt.text(0.1, 0.9, text, va='top', ha='left', wrap=True)
plt.tight_layout()
pdf.savefig(fig)
plt.close()

# Save the PDF
pdf.close()

print("Presentation saved as 'drought_proofing_measures_presentation.pdf'")