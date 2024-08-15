import pandas as pd

cities_disclosing_2020 = pd.read_csv("C:/Users/User/OneDrive/Documents/Predicting-city-collaboration-with-business/Datasets/Data/Cities/Cities Disclosing/2020_Cities_Disclosing_to_CDP.csv")
cities_responses_2020 = pd.read_csv("C:/Users/User/OneDrive/Documents/Data/Cities/Cities Responses/2020_Full_Cities_Dataset.csv")

corp_climate_change_2020 = pd.read_csv("C:/Users/User/OneDrive/Documents/Data/Corporations/Corporations Disclosing/Climate Change/2020_Corporates_Disclosing_to_CDP_Climate_Change.csv")
corp_water_security_2020 = pd.read_csv("C:/Users/User/OneDrive/Documents/Data/Corporations/Corporations Disclosing/Water Security/2020_Corporates_Disclosing_to_CDP_Water_Security.csv")



merged_2020 = pd.merge(cities_disclosing_2020, corp_climate_change_2020, on=['account_number', 'survey_year'], suffixes=('_city', '_corp_climate'))

merged_2020 = pd.merge(merged_2020, corp_water_security_2020, on=['account_number', 'survey_year'], suffixes=('', '_corp_water'))

merged_responses_2020 = pd.merge(cities_responses_2020, corp_climate_change_2020, on=['account_number', 'survey_year'], suffixes=('_city', '_corp_climate'))
merged_responses_2020 = pd.merge(merged_responses_2020, corp_water_security_2020, on=['account_number', 'survey_year'], suffixes=('', '_corp_water'))

merged_2020['climate_change_collaboration'] = (merged_2020['theme_city'] == merged_2020['theme_corp_climate']).astype(int)
merged_2020['water_security_collaboration'] = (merged_2020['theme_city'] == merged_2020['theme_corp_water']).astype(int)

merged_responses_2020['impact'] = merged_responses_2020['Response Answer_city'].apply(lambda x: len(str(x)))

climate_change_collab_rate = merged_2020['climate_change_collaboration'].mean()
print(f"Climate Change Collaboration Rate in 2020: {climate_change_collab_rate}")

water_security_collab_rate = merged_2020['water_security_collaboration'].mean()
print(f"Water Security Collaboration Rate in 2020: {water_security_collab_rate}")

average_impact_2020 = merged_responses_2020['impact'].mean()
print(f"Average Impact on Cities in 2020: {average_impact_2020}")

import matplotlib.pyplot as plt

# Bar plot for collaboration rates
collab_rates = {
    'Climate Change': climate_change_collab_rate,
    'Water Security': water_security_collab_rate
}
plt.bar(collab_rates.keys(), collab_rates.values())
plt.title('Collaboration Rates in 2020')
plt.ylabel('Rate')
plt.show()

# Histogram for impact distribution
plt.hist(merged_responses_2020['impact'], bins=20)
plt.title('Impact Distribution in 2020')
plt.xlabel('Impact')
plt.ylabel('Frequency')
plt.show()
