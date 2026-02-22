# 📚 Autonomous Market-Intelligence Scraper

An industrial-grade web scraper that monitors e-commerce data, performs price analysis, and sends real-time investment alerts via Discord.

## 🛠️ Tech Stack
- **Python 3.12**
- **BeautifulSoup4** (Parsing)
- **Pandas** (Data Structuring)
- **Discord Webhooks** (Real-time Alerts)

## 🤖 Features
- **Pagination Logic:** Automatically traverses multiple pages via "Next" buttons.
- **Data Cleaning:** Converts raw HTML currency strings into float values for analysis.
- **Smart Filtering:** Only alerts users for high-rated products (5 stars) under a specific budget (£20).
- **Persistence:** Exports full market snapshots to CSV for historical tracking.

## 📊 Market Snapshot
> This tool generates a CSV of all books found. Below is a sample of the data captured:
| Title | Price | Rating |
| :--- | :--- | :--- |
| Scott Pilgrim's Precious Little Life | £21.01 | 5 |
| Set Me Free | £17.46 | 5 |

## ⚙️ Setup
1. Clone the repo.
2. Run `pip install -r requirements.txt`.
3. Add your webhook URL to `config.py`.
4. Execute `python scraper.py`.
