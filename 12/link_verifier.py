import bs4
import requests
from urllib.parse import urljoin

user_input = input("What site do you want to verify:\n")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
res = requests.get(user_input, headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

all_links = soup.select("a")
broken_links = []

for link in all_links:
    href = link.get('href')
    if href:
        full_url = urljoin(user_input, href)  
        try:
            res = requests.get(full_url,headers=headers)
            print(full_url)
            res.raise_for_status()

        except Exception as e:
            print(f"Broken link found: {full_url} ({e})")
            broken_links.append(full_url)
print("Broken links:\n" + "\n".join(broken_links))


