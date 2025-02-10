import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus, urljoin
import time

def get_search_url(label):
    query = quote_plus(label)
    return f"https://www.google.com/search?hl=en&tbm=isch&q={query}"

def fetch_image_urls(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]
    return [urljoin(url, img_url) for img_url in img_urls]


def create_folder(label):
    folder_name = label.replace(" ", "_")
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def download_image(img_url, folder_name, index):
    try:
        img_data = requests.get(img_url).content
        with open(f"{folder_name}/{folder_name}_{index+1}.jpg", 'wb') as f:
            f.write(img_data)
        print(f"Downloaded {folder_name}_{index+1}.jpg")
        time.sleep(1)
    except Exception as e:
        print(f"Error downloading image {index+1}: {e}")

def download_images(label, num_images):
    url = get_search_url(label)
    img_urls = fetch_image_urls(url)
    folder_name = create_folder(label)
    
    for i, img_url in enumerate(img_urls[:num_images]):
        download_image(img_url, folder_name, i)


def download_images(label, num_images):
    """
    Scrapes images from Google Images based on the label and downloads them to a local folder.

    Args:
        label (str): Label or search keyword for the images (e.g., "cats", "dogs", "power line").
        num_images (int): The number of images to be scraped and downloaded.
    
    Returns:
        None
    """
    url = get_search_url(label)
    img_urls = fetch_image_urls(url)
    folder_name = create_folder(label)
    
    for i, img_url in enumerate(img_urls[:num_images]):
        download_image(img_url, folder_name, i)

if __name__ == "__main__":
    label = input("Enter the label (e.g., 'cats', 'power line'): ")
    num_images = int(input("Enter the number of images to download: "))
    download_images(label, num_images)