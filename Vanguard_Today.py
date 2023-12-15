from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys


app_path = os.path.dirname(sys.executable)

#modifying the file name by date for easy access
now = datetime.now()
day_month_year = now.strftime('%d-%m-%Y')


website = "https://www.vanguardngr.com"
path = r"C:\Users\CHARLIE\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"

#activating headless mode
options = Options()
options.add_argument("--headless=new")
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')


#creating service and activating drivers
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

titles = []
links = []

#Exctracting Web Elements from site
Web_E = driver.find_elements(by="xpath", value='//div[@class="entry-body"]')

for Web in Web_E:
    title = Web.find_element(by="xpath", value='./h3').text
    link = Web.find_element(by="xpath", value='./h3/a').get_attribute('href')

    titles.append(title)
    links.append(link)

dict = {"Titles": titles,"Links": links,}
Vanguard_Today = pd.DataFrame(dict)

file_name = f"Vanguard_Today{day_month_year}.csv"
final_path = os.path.join(app_path, file_name)
Vanguard_Today.to_csv(final_path)

driver.quit()
