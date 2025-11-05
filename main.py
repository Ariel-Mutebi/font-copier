import os
import time
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_folder_names_from_github_page(github_page_url: str) -> List[str]:
    driver.get(github_page_url)
    time.sleep(2)

    links = driver.find_elements(By.CSS_SELECTOR, "tbody .Link--primary")
    texts = [link.text for link in links]

    def is_folder_name(name: str) -> bool:
        return name and not bool(os.path.splitext(name)[1]) and not name.startswith(".")

    return list(filter(is_folder_name, texts))

mapbox_font_names = scrape_folder_names_from_github_page("https://github.com/mapbox/mapbox-studio-default-fonts/tree/master")
mapka_font_names = scrape_folder_names_from_github_page("https://github.com/mapka-dev/fonts/tree/master/packages/fonts/fonts")

def capitalised_snake_case_to_kebab_case(s: str) -> str:
    return s.replace("_", "-").lower()

mapka_font_names = [capitalised_snake_case_to_kebab_case(name) for name in mapka_font_names]
fonts_to_add = [font_name for font_name in mapbox_font_names if not font_name in mapka_font_names]
print(fonts_to_add)

driver.quit()
