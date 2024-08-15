import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
cities_responses_2020 = pd.read_csv(r"C:/Users/User/OneDrive/Documents/Data/Cities/Cities Responses/2020_Full_Cities_Dataset.csv")
# Print the column names
print("Columns in the DataFrame:", cities_responses_2020.columns)


# Filter the DataFrame to include only rows where 'Question Number' is "6.2"
df = cities_responses_2020[cities_responses_2020['Question Number'] == '6.2']

# Select the relevant columns
df = df[['Country', 'Organization', 'Response Answer']]

# Convert 'Response Answer' to a categorical variable (optional)
df['Response Answer'] = df['Response Answer'].astype('category')

# Group by 'Response Answer' and count occurrences
response_counts = df.groupby('Response Answer').size().reset_index(name='total')
response_counts = response_counts.sort_values(by='total', ascending=False)

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x='total', y='Response Answer', data=response_counts, palette='viridis')

# Adding labels to the bars
for i, count in enumerate(response_counts['total']):
    plt.text(count, i, f' {count}', va='center', fontsize=10, color='black')

plt.xlabel('Total')
plt.ylabel('Answer')
plt.title('Does your city collaborate in partnership with businesses\n in your city on sustainability projects?')

plt.show()