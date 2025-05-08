import csv
import requests

# Configuration
CSV_FILE = 'gclid.csv'  # Path to your CSV file
URL = ''
CAMPAIGN_ID = ''
CONSENT = 0
BEARER_TOKEN = ''  # <-- Replace with your actual token!

def read_gclids(file_path):
    gclids = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Skip empty rows
                gclids.append(row[0].strip())
    return gclids

def send_conversion(gclid, campaign_id, consent, token):
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'click_id': gclid,
        'campaign_id': campaign_id,
        'is_mobwizards': 1,
        'account_id': 'none',  # changed from 0 to 'none' as expected by API
        'consent': consent
    }

    try:
        response = requests.post(URL, json=payload, headers=headers)
        if response.status_code != 200:
            print(f"\n❌ Request failed for GCLID: {gclid}")
            print(f"Status Code: {response.status_code}")
            try:
                print("Response JSON:", response.json())
            except ValueError:
                print("Response Text:", response.text)
            return False
        return True
    except requests.RequestException as e:
        print(f"\n🚨 Network error for GCLID: {gclid}")
        print(f"Error: {e}")
        return False

def main():
    gclids = read_gclids(CSV_FILE)
    all_success = True

    for gclid in gclids:
        success = send_conversion(gclid, CAMPAIGN_ID, CONSENT, BEARER_TOKEN)
        if not success:
            all_success = False
            break  # Stop on first failure

    if all_success:
        print("✅ All conversions sent successfully.")
    else:
        print("❌ Stopped due to a failed request.")

if __name__ == '__main__':
    main()