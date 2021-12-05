from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import sys


driver = webdriver.Chrome('./chromedriver')
driver.headless = True # also works kinda

driver.get("https://www.sst.dk/en/english/corona-eng/status-of-the-epidemic/covid-19-updates-statistics-and-charts")

# // The following few useless lines of code clicks and removes a lame cookie pop up.
# identify element with xpath and click()
acceptcookiesbutton = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[1]/button[3]')
acceptcookiesbutton.click()
# // Lame Cookie Stuff ends here..


# // In the following few lines we
# /html/body/div[1]/div/div/div[1]/div[2]/div[1]/button[3]
# identify element with xpath and read text
vaccinepercent = driver.find_element_by_xpath('/html/body/main/main/article/div[3]/div/div[1]/div[1]/table/tbody/tr[3]/td[2]/span').get_attribute("innerHTML")
# print(vaccinepercent)

start = '('
end = ')'
s = vaccinepercent
print (s[s.find(start)+len(start):s.rfind(end)])



# /html/body/main/main/article/div[3]/div/div[1]/div[1]/table/tbody/tr[3]/td[2]/span/text()[2]
driver.close()