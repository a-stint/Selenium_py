from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://smoothcomp.com/en/event/13661/participants')

try:
    registrations = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "registrations"))
    )

    participants_grp = registrations.find_elements((By.CLASS_NAME,"participant-group margin-bottom-xs-64"))
    print(participants_grp.text)
    for group in participants_grp:
        participants =  group.find_elements((By.CLASS_NAME, "sc-card margin-bottom-xs-16 relative"))
        print(participants.text)

finally:
    driver.quit()

