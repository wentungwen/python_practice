from requests_html import HTMLSession
from bs4 import BeautifulSoup

WEB_PAGE = "https://www.empireonline.com/movies/features/best-movies-2/"
WEB_FILE = "./test_content.html"


# Using requests_html to render JavaScript
def get_web_page():
    # create an HTML Session object
    session = HTMLSession()
    # Use the object above to connect to needed webpage
    response = session.get(WEB_PAGE)
    # Run JavaScript code on webpage
    response.html.render()

    # Save web page to file
    with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.html.html)


def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        get_web_page()
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")


# Read web file if it exists, load from internet if it doesn't exist
result = read_web_file()
