import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}

product_url = 'https://www.flipkart.com/apple-iphone-14-pro-deep-purple-128-gb/p/itm75f73f63239fa'

def get_reviews(product_url):
    reviews = []
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    review_containers = soup.find_all('div', {'class': '_1AtVbE'})

    for container in review_containers:
        divs = container.findAll('div', {'class': 't-ZTKy'})
        if(divs):
            for div in divs:
                reviews.append(div.text)

    return reviews


reviews = get_reviews(product_url)

for review in reviews:
    print(review)
    print('---')