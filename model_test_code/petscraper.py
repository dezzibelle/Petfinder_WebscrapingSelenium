from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re

driver = webdriver.Chrome()
driver2 = webdriver.Chrome()

# Start page to scrape
#driver.get("https://www.petfinder.com/search/dogs-for-adoption/us/pa/state-college/?distance=25")
driver.get("https://www.petfinder.com/search/dogs-for-adoption/us/ny/white-plains/?distance=10")
#driver.get("https://www.petfinder.com/search/dogs-for-adoption/us/pa/state-college/?distance=10&sort%5B0%5D=recently_added")

csv_file = open('pets_2_StateCollege25mi.csv', 'w')
writer = csv.writer(csv_file)

#STEPS:
# 1 - From search result page - Click each dog's pic (pet_tile) to go to its page
# 2 - Scrape individual page
# 3 - Return to result page, select next pet until no more on page
# 4 - Next page, then repeat until no more pages

index = 1
dog_num = 0
while True:  #While Next button is at bottom of page
	try:
		print("Scraping Page #: " + str(index))
		index = index + 1

		# Find all the pets on the page
		pet_tiles = driver.find_elements_by_xpath('//a[@class="petCard-overlay-link"]')
		pets = [x.get_attribute("href") for x in pet_tiles]

		for pet in pets:
			driver2.get(pet)

			# Find all the info on each pet's page
			pet_dict = {}  #initialize dictionary

			name = driver2.find_element_by_xpath('.//h1[@id="Detail_Main"]').text
			organization = driver2.find_element_by_xpath('.//pf-truncate[@line-count="3"]').text
			story = driver2.find_element_by_xpath('(.//div[@class="u-vr4x"])[2]').text
			info1 = driver2.find_element_by_xpath('.//div[@class="card-section-inner"]').text
			info2 = driver2.find_element_by_xpath('//div[@class="grid grid_gutterLg u-vr4x"]').text
			info_all = (driver2.find_elements_by_tag_name("script"))[42].get_attribute("innerHTML")

			pet_dict['name'] = name
			pet_dict['organization'] = organization
			pet_dict['info1'] = info1
			pet_dict['info2'] = info2
			pet_dict['story'] = story
			pet_dict['info_all'] = info_all
			dog_num = dog_num + 1
			print("Writing dog #: " + str(dog_num))
			writer.writerow(pet_dict.values())  #writing to csv file

		# Locate the next button on the page.
		wait_button = WebDriverWait(driver, 10)  #
		next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'.//button[@class="fieldBtn fieldBtn_altHover m-fieldBtn_iconRt m-fieldBtn_tight m-fieldBtn_full"]')))
		next_button.click()
		time.sleep(1)   #1-second wait while page loads

	except Exception as e:
		print(e)
		csv_file.close()
		driver.close()
		driver2.close()
		break
