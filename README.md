# Polly novel Scraper

A modern web scraping tool to extract chapter content from WordPress-based websites. The tool automatically follows "Next Chapter" links and compiles all content into a single HTML file for easy reading and offline access. Features a sleek UI with real-time status updates and a spinner during the scraping process.

![image](https://github.com/user-attachments/assets/1ed8638e-a1b2-4243-a970-c76ebfb65e78)

---

## Features

- **Web Scraping:** Extracts chapter content and follows "Next Chapter" links using regex.
- **Modern UI:** Sleek, responsive design with a glassmorphism effect and vibrant colors.
- **Real-Time Feedback:** Displays a spinner and status updates during the scraping process.
- **Asynchronous Processing:** Uses the Fetch API to submit form data and update the UI without reloading the page.
- **Downloadable Output:** Saves the scraped content as an HTML file for easy download.

---

## Technologies Used

- **Flask:** Backend framework for handling web requests and processing.
- **BeautifulSoup:** Web scraping library to extract content from WordPress sites.
- **HTML/CSS/JavaScript:** Frontend for a modern, responsive UI with a spinner and status updates.
- **Fetch API:** For asynchronous form submission and real-time updates.
- **Regex:** To dynamically detect "Next Chapter" links.

---

## How It Works

1. **Input URL:** Enter the starting chapter URL and an output file name.
2. **Scraping Process:** The tool scrapes the content, follows "Next Chapter" links, and compiles everything into an HTML file.
3. **Real-Time Feedback:** A spinner and status message keep you informed during the process.
4. **Download:** Once complete, the HTML file is available for download.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/wordpress-scraper.git
   cd wordpress-scraper
   ```
2. Install the required dependencies:

```bash
pip install flask requests beautifulsoup4
```
3. Run the Flask app:

```bash
python app.py
```
4. Open your browser and navigate to:

```
http://127.0.0.1:5000
```
