from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Set options (optional)
options = Options()
options.add_argument("--start-maximized")  # Start maximized
options.add_argument("--headless")  # Run without opening a browser window

# Initialize the Firefox driver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

# Navigate to a webpage
driver.get("https://www.python.org")

# Print the title
print("Page title:", driver.title)

# Find an element
search_box = driver.find_element("name", "q")
search_box.send_keys("Selenium\n")

# Wait a bit (for demo purposes)
import time
time.sleep(3)

# Print the new title
print("New page title:", driver.title)

# Quit the browser
driver.quit()
