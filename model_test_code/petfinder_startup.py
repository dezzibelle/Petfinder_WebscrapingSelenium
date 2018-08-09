from selenium import webdriver
import time
import csv
import re

driver = webdriver.Chrome()

# Start page to scrape
#driver.get("https://www.petfinder.com/search/dogs-for-adoption/us/ny/white-plains/?distance=10&sort%5B0%5D=recently_added")
# Do I need to fill-in search form to get set of pets to scrape??

#TEST SITES FOR SCRAPING AN INDIVIDUAL PET PAGE:
#driver.get("https://www.petfinder.com/dog/cliff-42127137/ny/new-york/shelter-chic-ny1286/") #links below don't work
#driver.get("https://www.petfinder.com/dog/brody-42351895/ny/white-plains/snarr-northeast-ny1298/#story")  #links below work
driver.get("https://www.petfinder.com/dog/celine-dion-42077584/ny/new-york/shelter-chic-ny1286/")
#driver.get("https://www.petfinder.com/dog/piper-42311549/pa/state-college/centre-county-paws-pa106/")
#driver.get("https://www.petfinder.com/dog/jessie-41911810/pa/state-college/beagle911-refuge-pa462/")
#driver.get("https://www.petfinder.com/dog/sammy-41765036/ny/white-plains/animal-welfare-league-of-westchester-county-inc-ny1004/")

#STEPS:
# 1 - From search result page - Click dog's pic to go to its page
# 2 - Click 2nd time on photo
# 3 - Scrape individual pages
# 4 - Click "Next Pet"
# 5 - Repeat 3 & 4 until no more pages
# csv_file = open('pet_test.csv', 'w')
# writer = csv.writer(csv_file)

#####
pet_dict = {}
name = driver.find_element_by_xpath('.//h1[@id="Detail_Main"]').text
organization = driver.find_element_by_xpath('.//pf-truncate[@line-count="3"]').text
#contact_email =  driver.find_element_by_xpath('(.//a[@class="txt txt_link m-txt_bold"])[2]').text
story = driver.find_element_by_xpath('(.//div[@class="u-vr4x"])[2]').text
# #     long description

info1 = driver.find_element_by_xpath('.//div[@class="card-section-inner"]').text
#     name, breed, location, age_range, gender, size

info2 = driver.find_element_by_xpath('//div[@class="grid grid_gutterLg u-vr4x"]').text
#     house_train, health, good_with

# info3 = driver.find_element_by_xpath('//ul[@aria-label="Pet physical characteristics"]').text
# #     age_range, gender, size, colors
#
# info4 = driver.find_element_by_xpath('//div[@class="grid-col grid-col_1/2@minMd grid-col_1/1@minLg"]').text
# #     char, coat, house-train, health
#
# info5 = driver.find_element_by_xpath('(.//div[@class="grid-col grid-col_1/2@minMd grid-col_1/1@minLg"])[2]').text
# #     good_with, adoption fee

script_info = driver.find_elements_by_tag_name("script")
for elem in script_info:
    if "published_at" in elem.get_attribute("innerHTML"):
        info_all = elem.get_attribute("innerHTML")

print(info_all)
#info_all = (driver.find_elements_by_tag_name("script"))[42].get_attribute("innerHTML")


# photo_link = ??

# pet_dict['name'] = name
# pet_dict['organization'] = organization
# #pet_dict['contact_email'] = contact_email
# pet_dict['info1'] = info1
# pet_dict['info2'] = info2
# # pet_dict['info3'] = info3
# # pet_dict['info4'] = info4
# # pet_dict['info5'] = info5
# pet_dict['story'] = story
# pet_dict['info_all'] = info_all
# # print(pet_dict.values())
# writer.writerow(pet_dict.values())


######Print Out Variables to Check Results: #####
#print("--> testing==",testcase)




		# # Locate the next button element on the page and then call `button.click()` to click it.
		# button = driver.find_element_by_xpath('//button[@class="fieldBtn fieldBtn_altHover m-fieldBtn_iconRt m-fieldBtn_tight m-fieldBtn_full"]')
		# button.click()
		# time.sleep(2)

	# except Exception as e:
	# 	print(e)
	# 	driver.close()
	# 	break
