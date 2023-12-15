from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

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
Vanguard_news = pd.DataFrame(dict)
Vanguard_news.to_csv("Vanguard_Today.csv")

driver.quit()
