'''from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)'''


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cities_responses_2020 = pd.read_csv("C:/Users/User/OneDrive/Documents/Predicting-city-collaboration-with-business/Datasets/Data/Cities/Cities Responses/2020_Full_Cities_Dataset.csv")
cities_disclosing_2020 = pd.read_csv("C:/Users/User/OneDrive/Documents/Predicting-city-collaboration-with-business/Datasets/Data/Cities/Cities Disclosing/2020_Cities_Disclosing_to_CDP.csv")

print(cities_responses_2020.head())
print(cities_disclosing_2020.head())



# Assuming 'corporations_disclosing_2020' is your DataFrame
# Sample DataFrame creation for illustration
data = {'country': ['USA', 'USA', 'Canada', 'Canada', 'Canada', 'UK', 'UK', 'France', 'Germany']}
corporations_disclosing_2020 = pd.DataFrame(data)

# Group by country and calculate the total number of disclosures
summary_df = corporations_disclosing_2020.groupby('country').size().reset_index(name='total')

# Sort countries by total disclosures
summary_df = summary_df.sort_values('total', ascending=False)

# Plotting
plt.figure(figsize=(10, 8))
sns.barplot(x='total', y='country', data=summary_df, palette='viridis')

# Adding text labels
for index, value in enumerate(summary_df['total']):
    plt.text(value, index, str(value), va='center', ha='left', size=10)

# Labels and title
plt.xlabel('Total')
plt.ylabel('Country')
plt.title('Corporations disclosing in 2020 per Country')

# Display the plot
plt.show()

