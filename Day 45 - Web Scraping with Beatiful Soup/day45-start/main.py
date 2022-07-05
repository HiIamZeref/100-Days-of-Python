from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get("https://news.ycombinator.com")
website = response.text

soup = BeautifulSoup(website, "html.parser")
all_story_links = soup.find_all(name="a", class_= "titlelink")
articles = []
links = []
for tag in all_story_links:
    articles.append(tag.getText())
    links.append(tag.get("href"))


article_upvote = soup.find_all(name= "span", class_= "score")
upvotes = []
for upvote in article_upvote:
    integer = (upvote.getText()).split(" ")
    upvotes.append(int(integer[0]))

max_value = max(upvotes)
index = upvotes.index(max_value)

print(articles[index])
print(links[index])
print(max_value)
print(upvotes[index])









# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# all_anchor_tags = soup.find_all(name="a")


# for tag in all_anchor_tags:
#     print(tag.getText())
