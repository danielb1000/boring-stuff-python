from pathlib import Path
import requests
import os
import bs4

# here = parent folder of this file
here = Path(__file__).resolve().parent

# the naked imgur url
imgur = "https://imgur.com/search?q="

# ask user what to search
category = input("Search category:\n")

# the new url with users input in consideration
search_url = f"{imgur}{category}"

# where to save future images
# C:/path/to/here/category
save_dir = here / f"{category}"
os.makedirs(save_dir, exist_ok=True)

# set headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
# "browse" to https://imgur.com/search?q=category
res = requests.get(search_url, headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")


# download the immediate images which sadly are low resolution
def getLowResimages():
    # the images are all inside a <div> with class="cards"
    # select all <img> elements that are within <div> elements with the class cards
    elems = soup.select("div.cards img")
    for img_tag in elems:
        # <img alt="Image Tile." src="//i.imgur.com/xxxxxxx.jpg" original-title="">
        # we want the link in src
        img_src = img_tag.get("src")

        if img_src:
            # convert relative url to full url
            if img_src.startswith("//"):
                img_src = "https:" + img_src

            # given https://i.imgur.com/xxxxxxx.jpg we will save the image as C:/path/to/here/category/xxxxxxx.jpg
            img_filename = os.path.basename(img_src)
            img_path = save_dir / img_filename

            try:
                print(f"Accessing {img_src}...")
                img_response = requests.get(img_src, headers=headers)
                img_response.raise_for_status()

                # download the image
                with open(img_path, "wb") as f:
                    for chunk in img_response.iter_content(100000):
                        f.write(chunk)
                print(f"Saved image to {img_path}")
            except Exception as e:
                print(f"Failed to download {img_src}: {e}")


# get the HD version of the images by "clicking" them, being redirected to the "gallery"
# version of the image and then finding the direct link to it in the html code
# sadly this doesn't work because imgur uses too much javascript
def getHDimages():
    images = soup.select("div.cards a[href]")
    for image in images:
        href = image.get("href")
        if href:
            img_page_url = f"https://imgur.com{href}"
            try:
                res = requests.get(img_page_url, headers=headers)
                res.raise_for_status()
                img_soup = bs4.BeautifulSoup(res.text, "html.parser")

                # this is where the messed up html source can be found
                # messed up due to lack of javascript
                print(img_soup.prettify())

                img_tag = img_soup.select("div.imageContainer img")
                if img_tag:
                    # we might've found multiple img elements so we'll assume the first one is the correct one
                    img_src = img_tag[0].get("src")

                    if img_src and img_src.startswith("//"):
                        img_src = "https:" + img_src

                    img_filename = os.path.basename(img_src)
                    img_path = save_dir / img_filename

                    print(f"Accessing {img_src}...")
                    file_response = requests.get(img_src, headers=headers)
                    file_response.raise_for_status()

                    with open(img_path, "wb") as f:
                        for chunk in res.iter_content(100000):
                            f.write(chunk)
                    print(f"Saved HD image to {img_path}")
                else:
                    print(f"HD image not found at {img_page_url}")
            except Exception as e:
                print(f"Failed to download HD image from {img_page_url}: {e}")


getLowResimages()
# getHDimages()
