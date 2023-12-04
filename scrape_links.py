import time,json
from selenium.webdriver import Safari
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException

def get_url(i):
    if i == 1:
        return "https://www.stepstone.de/jobs"
    else:
        return f"https://www.stepstone.de/jobs?page={i}"


def get_pages(driver:Safari):
    # elem = driver.find_element(By.XPATH, '//*[@id="stepstone-pagination"]/ul/li[8]/a/span/span/span')
    return 6099

def get_aa(driver:Safari):
    aa = None
    while aa is None:
        try:
            aa = driver.find_elements(By.TAG_NAME, "a") 
        except NoSuchFrameException:
            pass
    res = []
    for a in aa:
        try:
            link = a.get_property("href")
        except:
            continue
        if link.startswith("https://www.stepstone.de/stellenangebote"):
            res += [a]
    return res
    




def ext_links(driver:Safari):
    aa = None
    res = []
    while aa is None:
        try:
            aa = driver.find_elements(By.TAG_NAME, "a") 
        except NoSuchFrameException:
            pass
    for a in aa:
        try:
            link = a.get_property("href")
        except:
            continue
        if link.startswith("https://www.stepstone.de/stellenangebote"):
            res += [link]
    return res



if __name__ == "__main__":
    driver = Safari()
    driver.maximize_window()
    driver.implicitly_wait(5)
    index = 39
    npages = get_pages(driver)
    driver.get("https://www.stepstone.de")
    driver.find_element(By.XPATH, '//*[@id="ccmgt_explicit_accept"]/div').click()
    with open("links.txt", "r") as f:
        links = json.load(f)
        print(len(links)%25)
    # links = []
    driver.get(get_url(index))
    while index <= npages:
        current_page = get_aa(driver)
        driver.find_element(By.CSS_SELECTOR, '[id^="stepstone-pagination-"] > ul > li:nth-child(9) > a').click()
        while get_aa(driver) == current_page:
            pass
        links += ext_links(driver=driver)
        with open("links.txt", "w") as f: json.dump(links, f)
        print(index)
        index += 1