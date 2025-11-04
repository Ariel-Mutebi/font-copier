import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Configure Chrome options
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Mapbox fonts page
driver.get("https://github.com/mapbox/mapbox-studio-default-fonts/tree/master")

time.sleep(2)

# scrape text in links to folders/files
links = driver.find_elements(By.CSS_SELECTOR, "tbody .Link--primary")
texts = [link.text for link in links]

def is_folder_name(name: str) -> bool:
    """Return True if the name does not have a file extension (is a folder)."""
    return name and not bool(os.path.splitext(name)[1]) and not name.startswith(".")

# I'm assuming that all the folder names are fonts.
mapbox_font_names = list(filter(is_folder_name, texts))
print(mapbox_font_names)

driver.quit()
