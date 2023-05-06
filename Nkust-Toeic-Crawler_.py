from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from docx import Document


def remove_blank_lines(text):
    return "".join([s for s in text.splitlines(True) if s.strip()])

driver = webdriver.Chrome()
driver.get("https://www.easytest.nkust.edu.tw/")
driver.set_window_size(1536, 864)

# 執行登入
driver.find_element(By.LINK_TEXT, "登入").click()
driver.implicitly_wait(10)
driver.find_element(By.ID, "cust_id").send_keys("C109156224")
driver.implicitly_wait(10)
driver.find_element(By.ID, "cust_pass").send_keys("7206")
driver.implicitly_wait(10)
# driver.find_element(By.ID, "myModal").click()
# driver.implicitly_wait(30)
driver.find_element(By.ID, "cust_pass").send_keys(Keys.ENTER)
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, ".section-title-border:nth-child(1) b").click()

driver.find_element(By.CSS_SELECTOR, ".service:nth-child(4)").click()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, ".service:nth-child(2) h3").click()
driver.implicitly_wait(10)
driver.find_element(By.ID, "testtype").click()
driver.implicitly_wait(10) 
dropdown = driver.find_element(By.ID, "testtype")
driver.implicitly_wait(10)
dropdown.find_element(By.XPATH, "//option[. = 'Part-6-Text Completion']").click()
driver.implicitly_wait(10)

for button_number in ["1", "5", "6", "7", "8", "9", "16", "17", "18", "19"]:
    button_xpath = "//a[contains(@onclick, \"set_level('" + button_number + "')\")]"
    driver.find_element(By.XPATH, button_xpath).click()
    driver.implicitly_wait(3)
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.END)
    driver.find_element(By.CSS_SELECTOR, "img").click()
    driver.find_element(By.ID, "modify_a4").click()

    frame_top = driver.find_element(By.NAME, "topFrame")
    driver.switch_to.frame(frame_top)
    content_top = driver.page_source

    driver.switch_to.default_content()

    frame_main = driver.find_element(By.NAME, "mainFrame")
    driver.switch_to.frame(frame_main)
    content_main = driver.page_source

    soup = BeautifulSoup(content_main, 'html.parser')
    soup = soup.get_text()
    soup = remove_blank_lines(soup)
    document = Document()
    p=document.add_paragraph(soup)
    document.save('第' + button_number + '回Part-6.docx')
    driver.implicitly_wait(3)

    driver.implicitly_wait(3)
    driver.switch_to.window(window_handles[0])

driver.quit()
