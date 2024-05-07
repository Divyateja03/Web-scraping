# Web-scraping
To scrape data from a webpage, we can input the URL and use Python's BeautifulSoup and requests module to request the server for the page's HTML code. After execution of the code, we can export all the relevant data into a CSV file, which will be structured in the same way as the original HTML page. We also use 'html.parser' to parse the data which is obtained from requesting the content from the server.

For this, we need to install requests and BeautifulSoup modules.

pip install requests

pip install beautifulsoup4

As an example I took the URL as "https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_quick_guide.htm" and the output for this URL is given in the web_content.csv file.
