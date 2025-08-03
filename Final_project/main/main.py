# main.py

import requests
from config import API_KEY, DEPLOYMENT_URL

# Mapping short codes to full pension scheme names
SCHEME_LABELS = {
    "NSAP": "National Social Assistance Programme",
    "IGNOAPS": "Indira Gandhi National Old Age Pension Scheme",
    "IGNWPS": "Indira Gandhi National Widow Pension Scheme",
    "IGNDPS": "Indira Gandhi National Disability Pension Scheme"
    # Add more mappings if needed
}

def get_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    response = requests.post(url, data={
        "apikey": api_key,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    })
    if response.status_code != 200:
        raise Exception(f"Token request failed: {response.text}")
    return response.json()["access_token"]

def predict_eligibility(fields, values):
    token = get_token(API_KEY)
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    
    payload = {
        "input_data": [{
            "fields": fields,
            "values": values
        }]
    }

    response = requests.post(DEPLOYMENT_URL, json=payload, headers=headers)
    
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def display_prediction(prediction_data):
    result = prediction_data["predictions"][0]["values"][0]
    predicted_code = result[0]
    probabilities = result[1]

    scheme_names = list(SCHEME_LABELS.values())
    label_keys = list(SCHEME_LABELS.keys())

    print("\n🎯 Predicted Pension Scheme:")
    print(f"  → {SCHEME_LABELS.get(predicted_code, predicted_code)} ({predicted_code})\n")

    print("📊 Class Probabilities:")
    for label, prob in zip(label_keys, probabilities):
        print(f"  - {SCHEME_LABELS.get(label, label)}: {round(prob * 100, 2)}%")

def main():
    print("=== Pension Eligibility Predictor ===\n")

    fields = [
        "Age", "Gender", "Disability", "MaritalStatus",
        "Caste", "Aadhaar", "Mobile", "District"
    ]

    user_values = []
    for field in fields:
        val = input(f"Enter {field}: ")
        if field in ["Age", "Disability", "Aadhaar", "Mobile"]:
            val = float(val)
        user_values.append(val)

    print("\nSending data to model for prediction...\n")
    prediction_data = predict_eligibility(fields, [user_values])
    display_prediction(prediction_data)

if __name__ == "__main__":
    main()
