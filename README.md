<h1>Data Scraping</h1>
<p>This script is designed to scrape product information from Daraz Bangladesh's website using Selenium. It specifically retrieves details about sunglasses, including their names, links, and images. The script automates a web browser to extract this data dynamically.</p>

<h2>Requirements</h2>
<ul>
    <li>Python</li>
    <li>Selenium WebDriver</li>
    <li>Google Chrome</li>
    <li>ChromeDriver (compatible with your Chrome version)</li>
</ul>

<h2>Installation</h2>
<pre><code>pip install selenium</code></pre>
<p>Download ChromeDriver from <a href="https://chromedriver.chromium.org/downloads">here</a> and ensure it is in your system's PATH or the script directory.</p>

<h2>How It Works</h2>
<ol>
    <li><strong>Initiate WebDriver</strong>: The script launches a Chrome browser using Selenium.</li>
    <li><strong>Navigate to Daraz</strong>: It opens the Daraz Bangladesh search results page for sunglasses.</li>
    <li><strong>Extract Product Name and Link</strong>: The script retrieves the name and URL of the first product listed on the page.</li>
    <li><strong>Extract Image URLs</strong>: It iterates through the first 9 products and collects their image URLs.</li>
    <li><strong>Print Data</strong>: The extracted product name, link, and image URLs are printed.</li>
    <li><strong>Wait and Close</strong>: The script waits for 60 seconds before closing the browser.</li>
</ol>

<h2>Code Explanation</h2>
<ul>
    <li><code>webdriver.Chrome()</code>: Launches a Chrome browser instance.</li>
    <li><code>driver.get(URL)</code>: Sends a request to the specified Daraz catalog page.</li>
    <li><code>driver.maximize_window()</code>: Maximizes the browser window.</li>
    <li><code>driver.find_element(By.XPATH, xpath).text</code>: Extracts the text content of the specified element.</li>
    <li><code>driver.find_element(By.XPATH, xpath).get_attribute("href")</code>: Retrieves the hyperlink from the element.</li>
    <li><strong>Image Extraction</strong>: Uses a loop to dynamically fetch image URLs for multiple products.</li>
    <li><code>time.sleep(60)</code>: Keeps the browser open for 60 seconds before quitting.</li>
    <li><code>driver.quit()</code>: Closes the browser session.</li>
</ul>

<h2>Usage</h2>
<pre><code>python scrap_daraz.py</code></pre>
<p>Ensure that ChromeDriver is correctly set up before running the script.</p>

<h2>Notes</h2>
<ul>
    <li>The script may break if Daraz updates its webpage structure. In such cases, update the XPaths accordingly.</li>
    <li>Modify <code>range(1,10)</code> to scrape more or fewer products.</li>
    <li>Add error handling for better robustness.</li>
</ul>

<h2>Author</h2>
<p>This script was developed by [Sajib Saha].</p>
