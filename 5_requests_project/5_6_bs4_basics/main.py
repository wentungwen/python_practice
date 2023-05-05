from bs4 import BeautifulSoup
import requests

with open("./test_content.html") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
tags = soup.select(selector="h3")
titles = [tag.get_text() for tag in tags]
reverse_titles = titles[::-1]
print(reverse_titles)

with open("./movie_titles.txt", mode="a") as f:
    for title in reverse_titles:
        f.write(title + "\n")

"""
# web scratching practice

res = requests.get("https://news.ycombinator.com/")
content = res.text

soup = BeautifulSoup(content, "html.parser")
tags = soup.find_all(class_="titleline")

title_line = [n.get_text() for n in tags]
link = [tag.find("a").get("href") for tag in tags]
upvote = [int(n.get_text().strip(" points")) for n in soup.select(selector=".subline .score")]

max_idx = upvote.index(max(upvote))
highest_data = (title_line[max_idx],link[max_idx], upvote[max_idx])


print(title_line)
print(link)
print(highest_data)


# basic Practice
with open("website.html") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.a)
all_a_tags = soup.find_all(name="a")
for tag in all_a_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name", class_="name")
print(heading)

company_url = soup.select_one(selector="p#intro strong a.intro")
print(company_url)

name_soup = soup.find_all("input")
for n in name_soup:
    try:
        len = n.get("maxlength")
        print(len)
    except AttributeError:
        continue
print(name_soup)
"""
