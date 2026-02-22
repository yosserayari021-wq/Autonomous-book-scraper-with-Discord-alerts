# 📚 Autonomous Market-Intelligence & Price Monitor

This industrial-grade Python tool automates the process of monitoring e-commerce data to find high-value products. It scrapes live data from a book catalog, performs statistical analysis, and delivers real-time "Buy Alerts" and market snapshots directly to a Discord channel.



## 🚀 Key Features

* **Multi-Page Autonomous Crawling**: Uses advanced pagination logic to traverse the site (up to a 5-page limit) without manual intervention.
* **Real-time Discord Alerts**: Instantly notifies a Discord channel when a "5-star" rated book under £20 is discovered.
* **Data Persistence & Cleaning**: Exports a full market snapshot to CSV, automatically removing duplicate entries by UPC and sorting by the best value (Rating/Price).
* **Visual Market Analytics**: Generates a Matplotlib-based price distribution histogram to help visualize market trends at a glance.
* **Automated Reporting**: Automatically uploads the visual chart directly to Discord at the end of every run for team or personal review.

## 🛠️ Tech Stack

* **Python 3.12**: Core logic and automation.
* **BeautifulSoup4**: HTML parsing and data extraction.
* **Pandas**: High-performance data manipulation and CSV management.
* **Matplotlib**: Data visualization and statistical report generation.
* **Requests**: Web communication and Discord Webhook integration.

---

## 📊 How it Works

1.  **Extraction**: The script visits the catalog and extracts Title, Price, UPC, and Rating for every item across multiple pages.
2.  **Filtering**: It runs comparison logic to identify "5-star" items under a £20 budget.
3.  **Communication**: High-value items are sent as formatted "Embeds" to Discord via Webhooks.
4.  **Analysis**: Once all pages are scraped, it builds a Pandas DataFrame to clean the data and calculate distribution.
5.  **Visualization**: A PNG report (`market_report.png`) is generated and uploaded to the cloud via the Discord API.



---

## ⚙️ Setup & Installation

1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Secrets**:
    Create a `config.py` file in the root directory and add your Discord Webhook URL:
    ```python
    WEBHOOK_URL = "your_discord_webhook_url_here"
    ```
4.  **Run the Scraper**:
    ```bash
    python scraper.py
    ```

## 📄 Output Samples
* **CSV Log**: `all_books.csv` — A historical record of every book seen, including timestamps and URLs.
* **Discord Embed**: Real-time notifications with clickable links and star ratings.
* **Market Snapshot**: `market_report.png` — A professional chart showing the current price landscape.

---
*Developed as part of a Python Automation Portfolio - 2026*
