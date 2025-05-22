import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter
import csv

url = "https://merojob.com/search/?q=&page=1"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get all job cards
    job_cards = soup.find_all('div', class_='card mt-3 hover-shadow')
    print(f"Found {len(job_cards)} job listings")

    job_titles = []
    companies = []
    job_data = []

    for job in job_cards:
        # Job title
        title_tag = job.find('h1', class_='text-primary font-weight-bold media-heading h4')
        title = title_tag.get_text(strip=True) if title_tag else None

        # Company name
        company_tag = job.find('h3', class_='h6')
        company_link = company_tag.find('a') if company_tag else None
        company = company_link.get_text(strip=True) if company_link else None

        if title and company:
            job_titles.append(title)
            companies.append(company)
            job_data.append((title, company))
    print(job_data)    
    # Save job data to CSV
    with open('merojob_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Job Title', 'Company'])
        writer.writerows(job_data)        

    # Plot top companies by number of job posts
    company_counts = Counter(companies)
    top_companies = company_counts.most_common(10)

    if top_companies:
        comp_names, comp_counts = zip(*top_companies)

        plt.figure(figsize=(10, 6))
        plt.bar(comp_names, comp_counts)
        plt.title("Top 10 Companies by Job Postings on Merojob")
        plt.xlabel("Company")
        plt.ylabel("Number of Postings")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
    else:
        print("No companies found in the scraped data.")
else:
    print(f"Request failed with status code: {response.status_code}")