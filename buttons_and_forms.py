#Install mechanical soup - $ python3 -m pip install MechanicalSoup
#Done

import mechanicalsoup

#1 - Finding the form
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

#2 - Filling in the form
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus" # Filling in the username automatically
form.select("input")[1]["value"] = "ThunderDude" #Filling in the password automatically

#3 - Submiting the form
profiles_page = browser.submit(form, login_page.url) #Clicking the log-in button automatically

#print(profiles_page.url)

links = profiles_page.soup.select("a")

#Invalid syntax

base_url = "http://olympus.realpython.org"
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")