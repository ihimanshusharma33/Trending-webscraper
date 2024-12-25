# Twitter Trending Topics Web Scraper

This project is a web scraping application designed to fetch trending hashtags from Twitter and display them on a Flask web interface. The project uses Selenium for web scraping, MongoDB for storing data, and Flask for the web interface.

## Features
- Automates login to Twitter using Selenium.
- Fetches trending hashtags from the Twitter homepage.
- Stores the trending hashtags in a MongoDB database.
- Provides a Flask-based web interface to trigger the scraping process and display the results.

---

## Prerequisites

### Tools and Libraries
- Python 3.9+
- Selenium
- MongoDB
- Flask

### Dependencies
Install the required Python packages:
```bash
pip install selenium pymongo flask
```

### Browser Driver
- Download ChromeDriver compatible with your Chrome browser version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
- Place the `chromedriver.exe` in the specified path (e.g., `C:/chromedriver-win32/chromedriver.exe`).

---

## Project Structure
```
project/
├── selenium_script.py      # Main script for web scraping
└── app.py                  # Flask application

```

---

## Setup

1. **Configure MongoDB**
   - Replace `______MONOGO_URI______` with your MongoDB connection string.
   - Ensure the database `twitter_trends` and collection `trending_topics` are created automatically.

2. **Twitter Credentials**
   - Replace `______YOUR_EMAIL______` and `______YOUR_PASSWORD______` in `selenium_script.py` with your Twitter login credentials.

3. **Proxy Configuration** (Optional)
   - Replace `PROXY_HOST`, `PROXY_PORT`, `PROXY_USER`, and `PROXY_PASS` in `selenium_script.py` with your proxy details if required.

4. **Run Flask Application**
   - Start the Flask app using the command:
     ```bash
     python app.py
     ```
   - Access the app at `http://127.0.0.1:5000/` in your browser.

---

## How It Works

### Selenium Script
1. Logs into Twitter using Selenium.
2. Waits for the Twitter homepage to load.
3. Scrapes Trendings # tags.
4. Stores the scraped data into the MongoDB collection `trending_topics`.

### Flask Application
1. Displays a button to trigger the Selenium script.
2. Fetches the latest scraped data from MongoDB.
3. Displays the trending hashtags and their timestamp on the web interface.

---

## Error Handling
- **Timeouts**: If an element is not found within the specified time, a timeout exception is logged.
- **Debugging**: If an error occurs, the page source is saved to `debug_page_source.html` for analysis.
- **No Data**: If no data is found in MongoDB, the web interface displays an appropriate message.



---

## Future Improvements
- Schedule scraping tasks using a task scheduler (e.g., `cron` or `Celery`).

---
