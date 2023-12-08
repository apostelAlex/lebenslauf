import json
import re
import time,json, os
from selenium.webdriver import Safari
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException
from bs4 import BeautifulSoup

def decode_stelle(driver, index):
    soup = BeautifulSoup(driver, "lxml")
    elem1 = soup.select('a[data-at="header-company-name"]')[0]
    elem2 = elem1.parent.next_sibling
    elems = soup.select("li span:nth-of-type(2)")
    if elems[0].text.startswith("Sei einer der ersten "):
        del elems[0]
    stadt = elems[0]
    anstellung = elems[1] # Feste Anstellung or Befristeter Vertrag or Ausbildung, Studium
    zeit = elems[2] # Vollzeit, Teilzeit, Home Office möglich
    erschienen = elems[3]
    # stadt = soup.find_all("span", class_=re.compile(r"^listing-content-provider-.*$"))[3]
    dd = {"Firma": elem1.text,
          "Stelle": elem2.text, 
          "Stadt": stadt.text, 
          "Anstellung": anstellung.text,
          "Arbeistzeit" : zeit.text, 
          "Erschienen": erschienen.text
          }
    with open("data/"+str(index)+ ".json", "w") as f:
        json.dump(dd, f)

# def decode_stelle(driver:Safari):
#     with open(f"data/{driver.current_url.split('/')[-1]}.html", "w") as f:
#         f.write(driver.page_source)

if __name__ == "__main__":
    index = 0
    for x in os.listdir("data/"):
        with open("data/" + x, "r") as f:
            decode_stelle(f.read(), index)
        index += 1
    # with open("links.txt", "r") as f:
    #     links = json.load(f)
    # driver = Safari()
    # driver.maximize_window()
    # driver.implicitly_wait(5)
    # driver.get("https://www.stepstone.de")
    # driver.find_element(By.XPATH, '//*[@id="ccmgt_explicit_accept"]/div').click()
    # with open("decoded.json", "r") as f:
    #     decoded = json.load(f)
    # for link in links:
    #     if link not in decoded:
    #         current = driver.find_element(By.TAG_NAME, "body")
    #         driver.get(link)
    #         while current == driver.find_element(By.TAG_NAME, "body"):
    #             pass
    #         stelle = decode_stelle(driver)
    #         decoded += [link]
    #         with open("decoded.json", "w") as f:
    #             json.dump(decoded, f)
        
        
    