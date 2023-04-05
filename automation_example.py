import requests
from bs4 import BeautifulSoup
import csv

# Set the URL of the webpage to be scraped
url = 'https://www.imdb.com/chart/top'

# Send a GET request to the URL and get the response
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element that contains the data to be scraped
table = soup.find('table', {'class': 'chart full-width'})

# Create a list to hold the rows of data
data = []

# Loop through each row in the table and extract the data
for row in table.find_all('tr'):
    # Create a list to hold the data for this row
    row_data = []

    # Loop through each cell in the row and extract the text
    for cell in row.find_all('td'):
        row_data.append(cell.text.strip())

    # Add the row data to the overall list of data
    data.append(row_data)

print(data)

# Write the data to a CSV file
with open('imdb_top250.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
