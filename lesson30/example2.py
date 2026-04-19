from bs4 import BeautifulSoup

html_content = """ <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Beatiful Soup</title>
</head>
<body>

    <h1>My Useful Links</h1>
    
    
    <div id= "links">
      <p class ="intro"> Here are some useful links:</p>
        <!-- Link 1: External Website -->
        <li><a href="https://google.com">Go to Google</a></li>
        
        <!-- Link 2: Another Local File -->
        <li><a href="about.html">About Us</a></li>
        
        
        <li><a href="mailto:someone@example.com">Send an Email</a></li>
    </div>

</body>
</html>

"""

soup = BeautifulSoup(html_content, "html.parser")
print("title of the page:", soup.title.text)

intro_text = soup.find('p', class_='intro').text
print("Intro text:", intro_text)

div_content = soup.find('div' , id='links')
links = div_content.find_all('a')
for link in links:
    print("Link:", link['href'])