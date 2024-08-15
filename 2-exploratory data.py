import pandas as pd

def print_opportunities_corporation(org, corporations_disclosing_2020, corporations_responses_2020):
    # Filter the DataFrame for the specified organization
    df3 = corporations_disclosing_2020[corporations_disclosing_2020['Organization'] == org][['Country', 'City', 'CDP Region']]

    if not df3.empty:
        print(f"COUNTRY: {df3['Country'].values[0]} CORPORATION: {org}\n")
        print(f"CITY: {df3['City'].values[0]}, CDP REGION: {df3['CDP Region'].values[0]}\n")
    else:
        print(f"No data found for the corporation: {org} in corporations_disclosing_2020")

    # Filter the responses DataFrame for the specified organization and question
    df2 = corporations_responses_2020[
        (corporations_responses_2020['Organization'] == org) & 
        (corporations_responses_2020['question_number'] == 'C2.4a')
    ][['question_unique_reference', 'response_value']]

    print(f"{org} OPPORTUNITIES:\n")
    if not df2.empty:
        print(f"QUESTION: {df2['question_unique_reference'].unique()[0]}\n")
        print("RESPONSES:")
        for response in df2['response_value']:
            print(f"- {response}")
    else:
        print("No detailed response data available for this organization.")

# Load the datasets
corporations_disclosing_2020 = pd.read_csv(r"C:/Users/User/OneDrive/Documents/Predicting-city-collaboration-with-business/Datasets/Data/Cities/Cities Disclosing/2020_Cities_Disclosing_to_CDP.csv")
corporations_responses_2020 = pd.read_csv(r"C:/Users/User/OneDrive/Documents/Data/Corporations/Corporations Responses/Climate Change/Full_Corporations_Response_Data_Dictionary.csv")

# Check unique organizations
print("Unique organizations in corporations_disclosing_2020:")
unique_organizations = corporations_disclosing_2020['Organization'].unique()
print(unique_organizations)

# Call the function with a valid organization name from the unique organizations list
valid_org_name = unique_organizations[0]  # Replace with an actual name from the printed list
print_opportunities_corporation(valid_org_name, corporations_disclosing_2020, corporations_responses_2020)
