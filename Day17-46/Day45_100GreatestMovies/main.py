import requests
from bs4 import BeautifulSoup
import pandas as pd

# Open the file in read mode
with open("D:/soup/3.htm", "r") as file:
    # Read the entire file and store it in a string
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all div tags with class 'name'
name_tags = soup.find_all('div', {'class': 'name'})

# Extract the text within each tag
movie_titles = [tag.get_text() for tag in name_tags]

df = pd.DataFrame(movie_titles, columns=['Movie Title'])

# Save the DataFrame to a CSV file
df.to_csv('movie_list.csv', index=False)
