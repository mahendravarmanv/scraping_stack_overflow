from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://stackoverflow.com/")
#chrome_options = Options()
#chrome_options.add_argument("--start-maximized")
value = []
value1 = []
value2 = []
search = driver.find_element_by_name("q")
search.send_keys("c++ libraries")
search.send_keys(Keys.ENTER)
final = ""
for i in range(1 , 4):
	if(i >= 2):
		driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
		try:
			page = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[5]/a[6]/span").click()
		except:
			pass
		for var in range(1,15):
			try:
				title = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[4]/div/div["+str(var)+"]/div[2]/div[1]/h3/a")
				answers = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[4]/div/div["+str(var)+"]/div[2]/div[2]")
				votes = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[4]/div/div["+str(var)+"]/div[1]/div/div[1]/div/span/strong")
				#final = title.text + "    " + answers.text + "Votes are   " + votes.text
				value.append(title.text)
				value1.append(answers)
				value2.append(votes)
				final =final + title.text + "\n" + answers.text + "Solution is : + \t\n" + "Votes are "+ votes.text+"\n\n\n\n"
				
			except:
				pass
			
	else:
		driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
		for var in range(1,15):
			title = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[4]/div/div["+str(var)+"]/div[2]/div[1]/h3/a")
			value.append(str(title.text))

			
#print(value)
with open('CS19M007.txt', 'w' , encoding="utf-8") as txtfile:
	txtfile.write(final)
	
		
        