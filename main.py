from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
options = Options()
options.add_argument("--start-maximized")  # Start maximized
# options.add_argument("--headless")       # Uncomment to run without UI
# options.add_argument("--no-sandbox")     # Useful for Docker or CI
# options.add_argument("--disable-dev-shm-usage")

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to a page
driver.get("https://www.python.org")

# Example interaction
print("Title:", driver.title)
search_box = driver.find_element("name", "q")
search_box.send_keys("Selenium\n")

import time
time.sleep(2)

print("New title:", driver.title)

driver.quit()
