📚 Autonomous Market-Intelligence & Price Monitor
This industrial-grade Python tool automates the process of monitoring e-commerce data to find high-value products. It scrapes live data, performs statistical analysis, and delivers real-time "Buy Alerts" and market snapshots to a Discord channel.

🚀 Key Features
Multi-Page Autonomous Crawling: Uses pagination logic to traverse the site (up to a set page limit) without manual intervention.

Real-time Discord Alerts: Instantly notifies a Discord channel when a "5-star" rated book under £20 is discovered.

Data Persistence & Cleaning: Exports a full market snapshot to CSV, automatically removing duplicate entries and sorting by the best deals (Rating/Price).

Visual Market Analytics: Generates a Matplotlib-based price distribution histogram to help visualize market trends.

Automated Reporting: Uploads the visual chart directly to Discord at the end of every run for team or personal review.

🛠️ Tech Stack
Python 3.x: Core logic.

BeautifulSoup4: HTML parsing and data extraction.

Pandas: Data manipulation and CSV management.

Matplotlib: Data visualization and report generation.

Requests: Web communication and Discord Webhook integration.

📊 How it Works (Logic Flow)
Extraction: The script visits the book catalog and extracts the Title, Price, UPC, and Rating for every item.

Filtering: It runs a comparison against a "Keyword" list and specific business logic (Rating > 4 and Price < £20).

Communication: High-value items are sent as "Embeds" to Discord via Webhooks.

Analysis: Once all pages are scraped, it builds a DataFrame to find the average price distribution.

Visualization: A PNG report is generated and uploaded to the cloud.
