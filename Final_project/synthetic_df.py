import pandas as pd
import numpy as np

# Load the district-level dataset
df = pd.read_csv("DistrictwisePensiondataundertheNationalSocialAssistanceProgrammeNSAP.csv")

synthetic_data = []

for _, row in df.iterrows():
    scheme = row['schemecode']
    district = row['districtname']
    total = row['totalbeneficiaries']
    
    # Skip rows with zero or missing beneficiaries
    if pd.isna(total) or total == 0:
        continue

    # Gender probabilities
    male_ratio = row['totalmale'] / total if total else 0
    female_ratio = row['totalfemale'] / total if total else 0
    gender_probs = np.array([male_ratio, female_ratio])
    gender_probs = gender_probs / gender_probs.sum() if gender_probs.sum() > 0 else [0.5, 0.5]

    # Aadhaar and mobile availability
    aadhaar_ratio = row['totalaadhaar'] / total if total else 0
    mobile_ratio = row['totalmpbilenumber'] / total if total else 0
    aadhaar_ratio = min(max(aadhaar_ratio, 0), 1)
    mobile_ratio = min(max(mobile_ratio, 0), 1)

    # Caste probabilities
    caste_ratios = {
        'SC': row['totalsc'] / total if total else 0,
        'ST': row['totalst'] / total if total else 0,
        'GEN': row['totalgen'] / total if total else 0,
        'OBC': row['totalobc'] / total if total else 0
    }
    caste_probs = np.array(list(caste_ratios.values()))
    caste_probs = caste_probs / caste_probs.sum() if caste_probs.sum() > 0 else [0.25, 0.25, 0.25, 0.25]

    # Simulate up to 100 applicants per district-scheme
    for _ in range(min(100, int(total))):
        gender = np.random.choice(['Male', 'Female'], p=gender_probs)
        caste = np.random.choice(list(caste_ratios.keys()), p=caste_probs)
        aadhaar = np.random.choice([1, 0], p=[aadhaar_ratio, 1 - aadhaar_ratio])
        mobile = np.random.choice([1, 0], p=[mobile_ratio, 1 - mobile_ratio])
        
        # Scheme-specific logic
        if scheme == 'IGNOAPS':
            age = np.random.randint(60, 91)
            marital = np.random.choice(['Married', 'Widowed', 'Single'])
            disability = 0
        elif scheme == 'IGNWPS':
            age = np.random.randint(40, 81)
            marital = 'Widowed'
            disability = 0
        else:  # IGNDPS
            age = np.random.randint(18, 61)
            marital = np.random.choice(['Married', 'Single'])
            disability = 1

        synthetic_data.append({
            'Age': age,
            'Gender': gender,
            'Disability': disability,
            'MaritalStatus': marital,
            'Caste': caste,
            'Aadhaar': aadhaar,
            'Mobile': mobile,
            'District': district,
            'Scheme': scheme
        })

# Create DataFrame
synthetic_df = pd.DataFrame(synthetic_data)

# Save to CSV (optional)
synthetic_df.to_csv("synthetic_applicant_data.csv", index=False)

print("Synthetic dataset generated with", len(synthetic_df), "records.")