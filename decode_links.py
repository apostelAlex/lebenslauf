import json
import time,json
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException

def decode_stelle(driver:Chrome):
    with open(f"data/{driver.current_url.split('/')[-1][17:-150]}", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
        
def decode_stelle_2(driver:Chrome):
    with open(f"data/{hash(driver.current_url.split('/')[-1])}", "w", encoding="utf-8") as f:
        f.write(driver.page_source)


if __name__ == "__main__":
    with open("links-MA.txt", "r") as f:
        links = json.load(f)
    driver = Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.stepstone.de")
    driver.find_element(By.XPATH, '//*[@id="ccmgt_explicit_accept"]/div').click()
    with open("decoded.json", "r") as f:
        decoded = json.load(f)
    for link in links:
        current = driver.find_element(By.TAG_NAME, "body")
        if link in decoded: 
            print(1)
            continue
        driver.get(link)
        while current == driver.find_element(By.TAG_NAME, "body"):
            pass
        try:
            stelle = decode_stelle(driver)
        except:
            stelle = decode_stelle_2(driver)
        decoded += [link]
        with open("decoded.json", "w") as f:
            json.dump(decoded, f)
        
        
    