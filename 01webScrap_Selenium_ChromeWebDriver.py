from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\Raksh\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

driver.get("http://python.org")

html_doc=driver.page_source

print(html_doc)