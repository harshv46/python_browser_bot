from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#import discord_webhook


# driver = webdriver.Chrome(chrome_options=opt,service_log_path='NUL')
driver = None
URL = "https://www.codechef.com/"

#put your teams credentials here
CREDS = {'user' : '','passwd':''}



def login():
	global driver
	#login required
	print("logging in")
	unameField = driver.find_element_by_xpath('//*[@id="edit-name"]')
	unameField.click()
	unameField.send_keys(CREDS['user'])
	upassField = driver.find_element_by_xpath('//*[@id="edit-pass"]')
	upassField.click()
	upassField.send_keys(CREDS['passwd'])
	driver.find_element_by_xpath('//*[@id="edit-submit"]').click() #Next button
	# return driver





def start_browser():

	global driver
	driver = webdriver.Edge(executable_path="F:\\downloads\\edgedriver_win64 (1)\\msedgedriver.exe")

	driver.get(URL)

	WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))

	if("https://www.codechef.com/" in driver.current_url):
		print("logging in")
		login()




if __name__=="__main__":
	# joinclass("Maths","15:13","15:15","sunday")
	op = int(input(("1. Login to Codechef\n2. Quit\nEnter option : ")))
	
	if(op==1):
		start_browser()
