from selenium import webdriver
import time

driver = webdriver.Chrome()
# Go to the page that we want to scrape
#driver.get("https://www.petfinder.com/search/dogs-for-adoption/us/ny/white-plains/")

#FOR SCRAPING 1ST PET PAGE:
driver.get("https://www.petfinder.com/dog/brody-42351895/ny/white-plains/snarr-northeast-ny1298/#story")

# Click dog's pic to go to its page
# pet_tile = driver.find_element_by_xpath('//a[@class="petCard-link"]')
# pet_tile.click()


# Page index used to keep track of where we are.
# index = 1
# # We want to start the first two pages.
# # If everything works, we will change it to while True
# while index <=2:
# 	try:
# 		print("Scraping Page number " + str(index))
# #		index = index + 1
# 		# Find all the dogs on page. The find_elements function will return a list of selenium select elements.
# 		# Check the documentation here: http://selenium-python.readthedocs.io/locating-elements.html
# 		pets = driver.find_elements_by_xpath('//div[@itemprop="review"]')
# 		# Iterate through the list and find the details of each review.
# 		for pet in pets:
# 			# Initialize an empty dictionary for each pet
#			pet_dict = {}
# 			# Use relative xpath to locate the title, content, username, date, rating.
# 			# Once you locate the element, you can use 'element.text' to return its string.
# 			# To get the attribute instead of the text of each element, use `element.get_attribute()`
# 			title = review.find_element_by_xpath('.//div[@itemprop="headline"]').text
# 			# Your code here

pet_dict = {}
name = driver.find_element_by_xpath('.//h1[@id="Detail_Main"]').text
testcase = driver.find_element_by_css_selector('#Site > div > div > div.tier.tier_flush\40 maxLg.u-vr8x.u-vrTop6x > div > div.grid-col.grid-col_2\2f 3\40 minLg > div > div:nth-child(1) > div > div.hrTitle.u-isHidden\40 minLg.u-vr3x > span > span > ul > li:nth-child(2)').text
#Site > div > div > div.tier.tier_flush\40 maxLg.u-vr8x.u-vrTop6x > div > div.grid-col.grid-col_2\2f 3\40 minLg > div > div:nth-child(1) > div > div.hrTitle.u-isHidden\40 minLg.u-vr3x > span > span > ul > li:nth-child(2)
#animal = driver.find_element_by_xpath('(.//ul[@class="hrArray hrArray_bulletDivided u-vr4x"])')
#breed = driver.find_element_by_xpath('.//span[@class="txt m-txt_bold m-txt_lg m-txt_colorPrimaryS2"]/li').text
age_range = driver.find_element_by_xpath('//span[@class="txt m-txt_lg m-txt_colorPrimaryS2"]').text
#testcase = driver.find_element_by_xpath('.//span[@class="hrTitle-body"]')

#gender =  driver.find_element_by_xpath('//span[contains(text(),'Male')]').text
#size = driver.find_element_by_xpath('//span[@class="txt m-txt_lg m-txt_colorPrimaryS2"]')
# colors =
coat_length = driver.find_element_by_xpath('.//dd[@class="txt u-vr4x"][2]').text
health = driver.find_element_by_xpath('.//dd[@class="txt"]').text
characteristics = driver.find_element_by_xpath('.//dd[@class="txt u-vr4x"]').text
house_train = driver.find_element_by_xpath('.//dd[@class="txt u-vr4x"][3]').text
# good_with =
# location = driver.find_element_by_xpath('//span[@class="txt m-txt_bold m-txt_lg m-txt_colorPrimaryS2"]').text
# story =
# contact_info =
# list_date = driver.find_element_by_link_text("published_at")
# photo_link =

#print("name=",name, "age=",age_range, "health=",health, "char=",characteristics)
#print("coatlength=",coat_length,"housetrain=",house_train)
print("--> testing==",testcase)
		# # Locate the next button element on the page and then call `button.click()` to click it.
		# button = driver.find_element_by_xpath('//button[@class="fieldBtn fieldBtn_altHover m-fieldBtn_iconRt m-fieldBtn_tight m-fieldBtn_full"]')
		# button.click()
		# time.sleep(2)

	# except Exception as e:
	# 	print(e)
	# 	driver.close()
	# 	break
