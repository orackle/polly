from flask import Flask, render_template, request, send_from_directory
import os
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

def get_chapter_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return None, None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract entry content
    entry_content = soup.find('div', class_='entry-content')
    if not entry_content:
        print("Entry content not found.")
        return None, None

    # Remove unwanted divs
    for unwanted in entry_content.find_all('div', class_='sharedaddy'):
        unwanted.decompose()

    # Find the 'Next Chapter' link using regex
    next_chapter_link = None
    for link in soup.find_all('a', href=True):
        if re.search(r'next\s*chapter|next|>>', link.text.lower()):
            next_chapter_link = link['href']
            break

    return str(entry_content), next_chapter_link

def scrape_wordpress_site(start_url, output_file):
    current_url = start_url
    all_content = "<html><body>"  # To store all chapters' content
    chapter = 1
    while current_url:
        print(f"Scraping: {current_url}")
        chapter_content, next_url = get_chapter_content(current_url)

        if not chapter_content or not next_url:
            print("No 'Next Chapter' link found. Stopping.")
            break

        # Append chapter with a header for separation
        all_content += f"<div class='chapter'>\n<h2>Chapter {chapter}</h2>\n{chapter_content}\n</div>\n<hr>\n"

        # Move to the next chapter
        current_url = next_url
        chapter +=1

    all_content += "</body></html>"

    # Save to an HTML file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(all_content)

    print(f"Scraping completed. Saved to {output_file}")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        start_url = request.form.get("start_url")
        output_file = request.form.get("output_file")

        if not start_url or not output_file:
            return "Please provide both a starting URL and an output file name."

        # Ensure the output file has a .html extension
        if not output_file.endswith(".html"):
            output_file += ".html"

        # Run the scraper
        scrape_wordpress_site(start_url, output_file)

        return f"Scraping completed! File saved as <a href='/{output_file}'>{output_file}</a>."

    return render_template("index.html")

@app.route("/<filename>")
def download_file(filename):
    return send_from_directory(".", filename)

if __name__ == "__main__":
    app.run(debug=True)
