#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
"""
example script in the book
"""
import requests
import os
import bs4
from pathlib import Path

here = Path(__file__).resolve().parent
url = "https://xkcd.com"  # starting url
os.makedirs(here / "xkcd", exist_ok=True)  # store comics in /xkcd
while not url.endswith("#"):
    # Download the page.
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the URL of the comic image.

# <img src="//imgs.xkcd.com/comics/craters.png" title="It&#39;s annoying that the Nastapoka Arc isn&#39;t a meteor impact crater, but I truly believe that--with enough time, effort, and determination--we could make it one." alt="Craters" srcset="//imgs.xkcd.com/comics/craters_2x.png 2x" style="image-orientation:none" />
# </div>
    comicElem = soup.select("#comic img") # finds div with id= "comic", assigns every img item inside it to list called comicElem
    # comicElem = [<img alt="Craters" src="//imgs.xkcd.com/comics/craters.png" srcset="//imgs.xkcd.com/comics/craters_2x.png 2x" style="image-orientation:none" title="It's annoying that the Nastapoka Arc isn't a meteor impact crater, but I truly believe that--with enough time, effort, and determination--we could make it one."/>]
    if comicElem == []:
        print("Could not find comic image.")
    else:

        comicUrl = "https:" + comicElem[0].get("src")
        # comicUrl = 'https://imgs.xkcd.com/comics/craters.png'

        # Download the image.
        print("Downloading image %s..." % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to /xkcd.
        imageFile = open(os.path.join(here / "xkcd", os.path.basename(comicUrl)), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    # <a rel="prev" href="/2982/" accesskey="p">&lt; Prev</a>
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prevLink.get("href")
