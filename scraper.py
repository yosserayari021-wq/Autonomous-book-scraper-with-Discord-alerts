import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import random
import time
import matplotlib.pyplot as plt
from config import WEBHOOK_URL
def send_discord_alert(item):
    stars = "⭐" * int(item['rating'])
    payload = {
        "username": "Book Deal Bot",
        "embeds": [{
            "title": f"🚨 DEAL FOUND: {item['title']}",
            "url": item['url'],
            "color": 5814783,
            "fields": [
                {"name": "Price", "value": f"£{item['price']}", "inline": True},
                {"name": "Rating", "value": stars, "inline": True},
                {"name": "UPC", "value": item['UPC'], "inline": False}
            ],
            "footer": {"text": "Scraper Bot 2026"}
        }]
    }
    requests.post(WEBHOOK_URL, json=payload)

all_data=[]
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
keywords = ["freedom", "soul", "freedom", "personal"]

current_url="https://books.toscrape.com/catalogue/page-1.html"
page_count = 0
print("Starting autonomous scraper...")

while current_url and page_count < 3:
    page_count += 1
    print(f"--- SCRAPING PAGE {page_count} ---")
    response=requests.get(current_url)
    soup=BeautifulSoup(response.text, "html.parser")
    books=soup.find_all("article", class_="product_pod")
    print(f"Scraping {current_url}... Found {len(books)} books.")

    for book in books:
        relative_url=book.h3.a["href"].replace("/../../../", "")
        book_url="https://books.toscrape.com/catalogue/"+relative_url

        book_recs=requests.get(book_url)
        book_soup=BeautifulSoup(book_recs.text, "html.parser")

        upc=book_soup.find("td").get_text()

        rating_tag = book.find("p", class_="star-rating")
        rating_word = rating_tag.get("class")[1]
        rating_num = rating_map.get(rating_word, 0)
        price=book.find("p", class_="price_color").get_text()
        clean_price=price.replace("£", " ").replace("Â", " ")
        num=float(clean_price)
        title = book.h3.a["title"]
        item={"UPC": upc,
              "title" : book.h3.a["title"],
              "price": num,
              "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
              "rating": rating_num,
              "url": book_url}
        is_match = any(word in item['title'].lower() for word in keywords)

        if rating_num == 5 and num < 20:
            send_discord_alert(item)
            print(f"📢 Alert sent to Discord for: {title}")
            all_data.append(item)
            print(f"MATCH FOUND: {upc} | {title} | {is_match} | ({rating_num} stars) at £{num} | {book_url}")
        next_btn = soup.find("li", class_="next")
    if next_btn:
        next_page_path=next_btn.find("a")["href"]
        if "catalogue/" in next_page_path:
            current_url = "https://books.toscrape.com/" + next_page_path
            time. sleep(1)        
    else:
        current_url = None

df=pd.DataFrame(all_data)

date_str=datetime.now().strftime("%Y_%b_%d")
filename = f"scrape_results_{date_str}.csv"

df = df.sort_values(by=["rating", "price"], ascending=[False, True])
df.to_csv("all_books.csv", index=False)

print("-" * 30)
print(f"MISSION COMPLETE!")
print(f"Total Books Captured: {len(all_data)}")
print(f"Saved to: {filename}")   

def create_market_report(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['price'], bins=15, color='#7289da', edgecolor='white')
    plt.title('Market Snapshot: Book Price Distribution (First 5 Pages)', fontsize=14)
    plt.xlabel('Price (£)', fontsize=12)
    plt.ylabel('Number of Books', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('market_report.png')
    print("\n Visualization complete! Check 'market_report.png' in your folder.")

create_market_report(df)

def upload_chart_to_discord():
    with open('market_report.png', 'rb') as f:
        file_data = {'file': ('market_report.png', f)}
        payload = {"content": "**Daily Market Analysis Complete!** Here is the price distribution for today:"}
        requests.post(WEBHOOK_URL, data=payload, files=file_data)
    print(" Report uploaded to Discord!")

upload_chart_to_discord()
