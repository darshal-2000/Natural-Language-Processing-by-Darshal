import json
from selenium import webdriver
from selenium.webdriver.common.by import By
def scrap(url):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Darshal\\Downloads\\chromedriver.exe")
    driver.get(url)
    driver.implicitly_wait(100)
    try:
        buttons = driver.find_elements(By.XPATH, '//div[text()="Continue Reading"]')
        for button in buttons:
            button.click()
        que = driver.find_element_by_class_name("qu-pb--small")
        aut = driver.find_elements_by_class_name("qu-truncateLines--3")
        ans = driver.find_elements_by_class_name("puppeteer_test_answer_content")
        driver.close()
        info = {}
        info.update({'question': que.text})
        auth_ans = []
        for a in range(5):
            auth_ans.append({'author': aut[a].text, 'answer': ans[a].text})
        info.update({'answer': auth_ans})
        json_object = json.dumps(info, indent=4)
        with open("quora.json", "w") as outfile:
            outfile.write(json_object)
    except:
        print()
