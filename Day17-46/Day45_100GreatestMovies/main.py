import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

movie_list = soup.find_all('h3', class_='title')

movie_titles = [movie.getText() for movie in movie_list]

reverse_list = movie_titles[::-1]


with open("movies.txt", mode="w") as file:
    for entry in reverse_list:
        file.write(f"{entry}\n")