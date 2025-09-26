The goal is to build a simple **web scraper** that collects top news headlines from a public website.

---

## 🛠️ Tools & Technologies
- **Language:** Python 3  
- **Libraries:**  
  - `requests` → to fetch HTML content  
  - `beautifulsoup4` → to parse and extract headlines  

---

## 🚀 How It Works
1. Fetches the HTML content of [BBC News](https://www.bbc.com/news).  
2. Parses the content using **BeautifulSoup**.  
3. Extracts headlines from `<h2>` and `<h3>` tags.  
4. Saves them in a file called **`headlines.txt`**.  
