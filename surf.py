import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Read the search terms from the file
with open("search_terms.txt") as f:
    search_terms = f.readlines()

with open("website.txt") as f:
    website = f.read().rstrip()

with open("search_id.txt") as f:
    search_id = f.read().rstrip()

# Iterate over the search terms
while search_terms:
    # Get the first search term and strip leading/trailing whitespace
    search_term = search_terms[0].strip()

    driver.get(website)

    if ("threat_defence" in driver.current_url):
        # Wait for the page to load
        driver.implicitly_wait(10)

        input("Enter captcha: ")
        driver.find_element(by=By.ID, value="button_submit").click()


    # Wait for the page to load
    driver.implicitly_wait(10)

    # Find the search box and enter the search query
    search_box = driver.find_element(by=By.ID, value="searchinput")
    search_box.clear()  # Clear any previous search term
    search_box.send_keys(search_term)

    # Find the search button and click it
    search_button = driver.find_element(by=By.XPATH, value=f'//*[@id="{search_id}"]/table/tbody/tr[1]/td[2]/button')
    search_button.click()

    # Wait for the search results to load
    driver.implicitly_wait(10)

    # Chances are a spam window opened up, go back to the initialpage
    driver.switch_to.window(driver.window_handles[0])

    # Wait for the search results to load
    driver.implicitly_wait(10)

    # Go to the first result
    first_result = driver.find_element(by=By.XPATH, value='/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[2]/a[1]')
    first_result.click()

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Find the download link and click it
    download_link = driver.find_element(by=By.XPATH, value='/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/a[1]')
    download_link.click()

    # Remove the used search term from the list
    search_terms.pop(0)

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Write the updated search terms back to the file
    with open("search_terms.txt", "w") as f:
        f.writelines(search_terms)

# Close the browser
driver.close()

