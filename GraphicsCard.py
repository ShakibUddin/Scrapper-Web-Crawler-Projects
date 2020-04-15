from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

def getData(url):
    source = urlopen(url)

    soup = BeautifulSoup(source, "html.parser")

    for product_info in soup.find_all("div", class_="product-info"):

        description_for_one_product = ""
        product_name = product_info.h4.a.text
        product_description = product_info.find("ul")
        product_price = product_info.find("div", class_="price space-between").span.text[:-1]+" Taka"

        for i, item in enumerate(product_description):
            description_for_one_product += item.text+", "

        csv_writer.writerow([product_name,description_for_one_product,product_price])

csv_file = open('Graphics_Crad.csv','w',newline='',encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name','Description','Price'])

for page in range(1,9):
    getData("https://www.startech.com.bd/component/graphics-card?page="+str(page))
    print("Data collection successful for page ", page)

print("All data collected")
csv_file.close()
