from bs4 import BeautifulSoup

html_content = " <html><body><h1> Hello beautifulSoup </h1></body></html>"
soup = BeautifulSoup(html_content, "html.parser")
paragraph = soup.find('h1').text
print(paragraph)