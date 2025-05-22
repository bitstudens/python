
import csv
import numpy as np
from datetime import datetime, timedelta
import random

num_rows = 100000
np.random.seed(0)  # For reproducibility

transaction_ids = range(1, num_rows + 1)
customer_ids = np.random.randint(1000, 5000, size=num_rows)
gender = np.random.choice(['Male','Female'], size=num_rows)
categories = np.random.choice(['Electronics', 'Clothing', 'Home', 'Books', 'Toys'], size=num_rows)
amounts = np.round(np.random.uniform(10.0, 500.0, size=num_rows), 2)
dates = [datetime.now() - timedelta(days=random.randint(0, 365)) for _ in range(num_rows)]


with open('transactions.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Transaction ID', 'Customer','Gender', 'Category', 'Amount', 'Date'])
    for i in range(num_rows):
        writer.writerow([transaction_ids[i], customer_ids[i],gender[i], categories[i], amounts[i], dates[i].strftime('%Y-%m-%d')])
print("CSV file 'transactions.csv' generated successfully.")
