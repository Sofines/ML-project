import pandas as pd
import h2o
from sklearn.model_selection import train_test_split

cities_responses_2020 = pd.read_csv(r"C:/Users/User/OneDrive/Documents/Data/Cities/Cities Responses/2020_Full_Cities_Dataset.csv")
cities_disclosing_2020 = pd.read_csv(r"C:/Users/User/OneDrive/Documents/Data/Cities/Cities Disclosing/2020_Cities_Disclosing_to_CDP.csv")

print(cities_responses_2020.columns)
df_cities = cities_disclosing_2020.copy()
# Filter and merge for Question Number == "0.5" and Column Name == "Current population"
df = cities_responses_2020[(cities_responses_2020['Question Number'] == '0.5') & 
                           (cities_responses_2020['Column Name'] == 'Current population')]
df = df[['Country', 'Organization', 'Response Answer']]
df_cities = pd.merge(df_cities, df, on=['Country', 'Organization'])
df_cities['Response Answer'] = pd.to_numeric(df_cities['Response Answer'], errors='coerce')
df_cities.rename(columns={'Response Answer': 'Current population'}, inplace=True)

# Filter and merge for Question Number == "0.6" and Column Name == "Land area of the city boundary as defined in question 0.1 (in square km)"
df = cities_responses_2020[(cities_responses_2020['Question Number'] == '0.6') & 
                           (cities_responses_2020['Column Name'] == 'Land area of the city boundary as defined in question 0.1 (in square km)')]
df = df[['Country', 'Organization', 'Response Answer']]
df_cities = pd.merge(df_cities, df, on=['Country', 'Organization'])
df_cities['Response Answer'] = pd.to_numeric(df_cities['Response Answer'], errors='coerce')
df_cities.rename(columns={'Response Answer': 'Land area square Km'}, inplace=True)

# Filter and merge for Question Number == "6.2"
df = cities_responses_2020[cities_responses_2020['Question Number'] == '6.2']
df = df[['Country', 'Organization', 'Response Answer']]
df_cities = pd.merge(df_cities, df, on=['Country', 'Organization'])
df_cities.rename(columns={'Response Answer': 'target'}, inplace=True)
df_cities['target'] = df_cities['target'].astype('category')

# Filter and merge for Question Number == "6.0" and Column Name == "Opportunity"
df = cities_responses_2020[(cities_responses_2020['Question Number'] == '6.0') & 
                           (cities_responses_2020['Column Name'] == 'Opportunity')]
df = df[['Country', 'Organization', 'Response Answer']]
df_cities = pd.merge(df_cities, df, on=['Country', 'Organization'])
df_cities.rename(columns={'Response Answer': 'opportunity'}, inplace=True)
df_cities['opportunity'] = df_cities['opportunity'].astype(str)
df_cities['Country'] = df_cities['Country'].astype(str)

# Display the resulting DataFrame
print(df_cities.head())

training_set, testing_set = train_test_split(df_cities, test_size=0.3, random_state=42, stratify=df_cities['target'])

# Display the shapes of the resulting datasets
print(f"Training set shape: {training_set.shape}")
print(f"Testing set shape: {testing_set.shape}")

# Initialize H2O
if h2o.cluster().is_running():
    h2o.cluster().shutdown()
h2o.init()