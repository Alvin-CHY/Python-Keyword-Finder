import requests

def scrape_site():
    requests = requests.get(url)
    if search_text.lower() in response.text.lower():
        print(f" '{search_text}'on the website")
    else:
        print(f" '{search_text}'not found the website")

if name == "main":
    url = input("Enter website URL: ")
    search_text = input("Enter word to search: ")
    search_website_text(url, search_text)