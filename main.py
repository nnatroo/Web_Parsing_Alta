from bs4 import BeautifulSoup
import requests
import csv
from time import sleep
from random import randint

page_numb = 1
url = f"https://alta.ge/pcs-notebooks-tablets-page-{page_numb}.html"

file = open('items.csv', 'w', encoding="utf-8_sig", newline="\n")
file_object = csv.writer(file)
file_object.writerow(["სახელი", "ფასი", "სურათის_URL"])

while page_numb < 10:
    r = requests.get(url)
    content = r.text
    # print(content)

    soup = BeautifulSoup(content, "html.parser")

    items = soup.find('div', class_="grid-list")
    # print(items)

    list_of_items = items.find_all("div", class_='ty-column3')
    # print(list_of_items)
    for each in list_of_items:
        image_url = each.div.form.div.img.attrs.get('src')
        # print(image_url
        title = each.find("a", class_="product-title").text
        print(title)
        price = each.find("span", class_="ty-price-num").text
        print(price)
        file_object.writerow([title, price, image_url])

    sleep(randint(15, 20))
    page_numb += 1
