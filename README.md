# 🪙 Crypto Bot

A Telegram crypto parsing bot built with **Python**, **pyTelegramBotAPI**, and **Selenium**.

## 📘 Overview

**Crypto Bot** automatically fetches cryptocurrency data (like prices and trends) from web sources using Selenium and delivers it to users via a Telegram bot interface powered by `pyTelegramBotAPI`.

This project demonstrates how to combine web scraping and Telegram automation in a simple, extendable Python application.

## ✨ Features

* 🔹 Real-time cryptocurrency price parsing via Selenium
* 🔹 Telegram bot interface for user interaction
* 🔹 Easy to extend with new coins or data sources
* 🔹 Simple setup and configuration

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AlbertZaqaryan/crypto_bot.git
cd crypto_bot
```

### 2️⃣ Install dependencies

If a `requirements.txt` file exists:

```bash
pip install -r requirements.txt
```

Otherwise, install manually:

```bash
pip install pyTelegramBotAPI selenium
```

### 3️⃣ Configure environment variables

Before running the bot, you’ll need a Telegram bot token and WebDriver path.

Create a `.env` file or edit config variables directly in your code:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
WEBDRIVER_PATH=/path/to/chromedriver
```

### 4️⃣ Run the bot

```bash
python bot.py
```

Then open your Telegram app, find your bot, and send `/start`.

---

## 🗂 Project Structure

| File / Folder        | Description                                          |
| -------------------- | ---------------------------------------------------- |
| `bot.py`             | Main entry point; handles bot commands and responses |
| `parser.py`          | Web scraper module using Selenium                    |
| `image_bot.jpg`      | Example image or bot screenshot                      |
| `config.py` / `.env` | Configuration and environment variables              |
| `requirements.txt`   | Python dependencies                                  |

---

## ⚙️ Configuration Notes

* Ensure you have the correct **WebDriver** (e.g., ChromeDriver or GeckoDriver) installed and accessible in your system PATH.
* In `parser.py`, modify the **target URL** and **selectors (XPath/CSS)** to match your data source.
* You can extend `bot.py` to include new commands, custom messages, or periodic updates.

---

## 💡 Future Improvements

* Add multiple data sources for more accurate crypto data
* Implement scheduled updates or background jobs
* Integrate visualizations (charts, graphs)
* Cache or store data using SQLite or Redis
* Add Docker support for easy deployment

---

## 🧠 Technologies Used

* **Python 3.x**
* **pyTelegramBotAPI** — Telegram Bot API wrapper
* **Selenium** — Web automation and scraping
* **Chromedriver / Geckodriver** — Browser drivers

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it as long as proper attribution is given.

---

