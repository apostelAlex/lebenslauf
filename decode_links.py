import json
import time,json
from selenium.webdriver import Safari
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException

def decode_stelle(driver:Safari):
    with open(f"data/{driver.current_url.split('/')[-1]}.html", "w") as f:
        f.write(driver.page_source)

if __name__ == "__main__":
    with open("links.txt", "r") as f:
        links = json.load(f)
    driver = Safari()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.stepstone.de")
    driver.find_element(By.XPATH, '//*[@id="ccmgt_explicit_accept"]/div').click()
    with open("decoded.json", "r") as f:
        decoded = json.load(f)
    for link in links:
        if link not in decoded:
            current = driver.find_element(By.TAG_NAME, "body")
            driver.get(link)
            while current == driver.find_element(By.TAG_NAME, "body"):
                pass
            stelle = decode_stelle(driver)
            decoded += [link]
            with open("decoded.json", "w") as f:
                json.dump(decoded, f)
        
        
    