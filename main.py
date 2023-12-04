import time
from pdf import main as extract_pdf
from gpt import ask_gpt
from selenium.webdriver import Safari
from selenium.webdriver.common.by import By

def get_jobs(jobtitle, area):
    driver = Safari()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.stepstone.de")
    driver.find_element(By.XPATH, '//*[@id="ccmgt_explicit_accept"]/div').click()
    job_title_elem = driver.find_element(By.ID, "stepstone-autocomplete-162")
    job_title_elem.send_keys(jobtitle)
    location_elem = driver.find_element(By.ID, "stepstone-form-element-173-input")
    location_elem.send_keys(area)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app-searchBar"]/div/div/div/div/div[2]/button').click()
    time.sleep(2)
    aa = driver.find_elements(By.TAG_NAME, "a")
    res = []
    for a in aa:
        try:
            link = a.get_property("href")
        except:
            continue
        if link.startswith("https://www.stepstone.de/stellenangebote"):
            res += [link]
    return res
        
def main():
    p = input("Please enter the path...\n")
    text = extract_pdf(p)
    result = ask_gpt(text, "gpt-3.5-turbo")
    jobs = result.split("\n")
    for n,j in enumerate(jobs):
        jobs[n] = j.split(".")[-1].strip()
    links = []
    for j in jobs:
        links += get_jobs(j, "Baden-Württemberg")
    with open("/Users/a2/Desktop/stellenanzeigen.txt", "w") as f:
        f.write(links.__str__())
        
    
    
if __name__ == "__main__":
    main()
