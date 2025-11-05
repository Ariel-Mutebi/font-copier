import os
import time
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Utilities
def is_folder_name(name: str) -> bool:
    return name and not bool(os.path.splitext(name)[1]) and not name.startswith(".")

def capitalised_snake_case_to_kebab_case(s: str) -> str:
    return s.replace("_", "-").lower()

def kebab_case_to_no_case(s: str) -> str:
    return s.replace("-", "")

def kebab_case_to_capitalized_snake_case(s: str) ->  str:
    return "_".join([segment.capitalize() for segment in s.split("-")])

# Main program
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_folder_names_from_github_page(github_page_url: str) -> List[str]:
    driver.get(github_page_url)
    time.sleep(2)

    links = driver.find_elements(By.CSS_SELECTOR, "tbody .Link--primary")
    texts = [link.text for link in links]

    return list(filter(is_folder_name, texts))

mapbox_font_names = scrape_folder_names_from_github_page(
    "https://github.com/mapbox/mapbox-studio-default-fonts/tree/master"
)
mapka_font_names = scrape_folder_names_from_github_page(
    "https://github.com/mapka-dev/fonts/tree/master/packages/fonts/fonts"
)

driver.quit()

mapka_font_names_with_mapbox_casing = [
    capitalised_snake_case_to_kebab_case(name) for name in mapka_font_names
]
fonts_to_add = [
    font_name for font_name in mapbox_font_names
    if not font_name in mapka_font_names_with_mapbox_casing
]

MAPKA_FONTS_DIRECTORY_ABSOLUTE_PATH = "/home/player/Mapka/fonts/packages/fonts/fonts/"

for font in fonts_to_add:
    github_google_fonts_mirror_for_svn = f"https://github.com/google/fonts/trunk/ofl/{kebab_case_to_no_case(font)}"
    destination = MAPKA_FONTS_DIRECTORY_ABSOLUTE_PATH + kebab_case_to_capitalized_snake_case(font)
    os.makedirs(destination, exist_ok=True)
    os.system(f"svn export {github_google_fonts_mirror_for_svn} {destination}")
