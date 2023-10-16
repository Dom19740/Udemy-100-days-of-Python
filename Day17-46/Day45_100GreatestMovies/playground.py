from bs4 import BeautifulSoup

# import lxml #if html.parser does not work

with open('website.html', 'r', encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")  # try "lxml" if html.parser doesnt work

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)  # get first p tag

# all_anchor_tags = soup.find_all(name="a")

# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)