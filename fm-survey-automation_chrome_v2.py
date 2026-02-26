from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, InvalidSessionIdException, InvalidArgumentException
from selenium.webdriver.chrome.options import Options
from random import randint # inclusive 
from random import choice
import time
# from selenium.webdriver.chrome.service import Service
def fm_survey_chrome():
	chrome_options = Options()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless") # bez gui
# driver = webdriver.Chrome(options=chrome_options)
	try:
		url = input("Enter url: ")
		driver = webdriver.Chrome() # starts Chrome
		driver.get(url)
		print("got page loaded")
		time.sleep(0.5)
	except InvalidArgumentException as e:
		print("---WRONG URL--- ", e)
		return 0

	iterations = 43
	while iterations > 0:
		try:
			print("locating audio button")
			audio_button = WebDriverWait(driver, 10).until(
			    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "audio"))
			)
			actions = ActionChains(driver) # object of sequential user actions fe. drag and drops, holding
			actions.move_to_element(audio_button).click()
			print("playing song")
			actions.perform() # executes the queue

# element = driver.find_element(By.TAG_NAME, "body") # next element in body to be focused
# element.click()
# element.send_keys(Keys.TAB)
# time.sleep(2)
# element.send_keys(Keys.SPACE) # manual song play

# play_button = WebDriverWait(driver, 10).until(
# 	expected_conditions.presence_of_element_located(
# 		(By.CSS_SELECTOR, 'audio[id="myAudio_L1q20m_3_1"]')
# 	)
# )
# if play_button:
# 	driver.execute_script(""" 
# 		document.getElementById('myAudio_L1q20m_3_1').play() 
# 	""") # multiline string is between three hashtags
# js .play() is treated as script auto action, no human interaction detected
			time.sleep(5.5)
			print("finding question 1")
			question_radio_1 = driver.find_element(By.CSS_SELECTOR, f"input[type='radio'][id^='L1q20_'][id$='_{choice([1,2])}']")
			print("answering question 1")
			driver.execute_script("arguments[0].click();", question_radio_1) # question_radio_1 is the first argument, counted from 0
			time.sleep(0.5)
			print("finding question 2")
			question_radio_2 = driver.find_element(By.CSS_SELECTOR, f"input[type='radio'][id^='L1q22_'][id$='_{randint(1,3)}']")
			print("answering question 2")
			driver.execute_script("arguments[0].click();", question_radio_2) # executes JS script and allows for interaction with hidden elements
# driver.find_element(By.CSS_SELECTOR, "css selector here']").click() # finding element by selector, may not work with buttons
# question_radio_1 = WebDriverWait(driver, 10).until( # holder for radio - WebElement
# 	expected_conditions.element_to_be_clickable(
# 		(By.CSS_SELECTOR, f"input[type='radio'][id='L1q20_3_1']")
# 	)
# )
# print(question_radio_1)
# question_radio_1.click() # first question
# time.sleep(1)
# question_radio_2 = WebDriverWait(driver, 10).until(
# 	expected_conditions.element_to_be_clickable(
# 		(By.CSS_SELECTOR, f"input[type='radio'][id='L1q22_3_{randint(1,3)}']") # second question
# 	)
# )
# question_radio_2.click()
			time.sleep(0.5)
			print("finding and submitting page")
			submit_button = driver.find_element(By.ID, "fmnextbtn") # next page
			driver.execute_script("arguments[0].click();", submit_button)

			iterations -= 1
			print("iterations left: ", iterations)
		except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
			print("error on " + str(iterations) + " iteration") # types must be coherent
			time.sleep(0.2) # to not stress cpu
			pass # does absolutely nothing
			# continue # skips current iteration
		except InvalidSessionIdException as e:
			print("---SESSION CLOSED--- ",  e)
			# raise InvalidSessionIdException # creates unneccesarilly new exception
			return 0

	print("final delay")
	time.sleep(5)
	driver.quit()

if __name__ == "__main__": # while importing as module, prevents executing main function automatically
	fm_survey_chrome() 
