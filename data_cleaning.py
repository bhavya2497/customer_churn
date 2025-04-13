import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")
#print(df)
df.drop_duplicates(inplace=True)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

df = df[df['TotalCharges'].notnull()]

df['SeniorCitizen'] = df['SeniorCitizen'].apply(lambda x:'Yes' if x == 1 else 'No')

def tenure_group(tenure):
    if tenure <= 12:
        return "0-1 year"
    elif tenure <= 24:
        return "1-2 years"
    elif tenure <= 48:
        return "2-4 years"
    elif tenure <= 60:
        return "4-5 years"
    else:
        return "5+ years"

df['TenureGroup'] = df['tenure'].apply(tenure_group)

df.to_csv("Telco-Customer-Churn-Clean.csv", index= False)
print(df)
print("Data Cleaned")


