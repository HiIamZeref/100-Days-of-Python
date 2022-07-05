
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")
all_movies_tags = soup.find_all(name= "h3", class_="title")
#reverse list
all_movies_tags.reverse()

with open("movie_list.txt", mode="w", encoding= "utf-8") as doc:
    for tag in all_movies_tags:
        doc.write(f"{tag.getText()} \n")


