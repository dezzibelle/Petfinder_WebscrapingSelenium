from selenium import webdriver
import time

driver = webdriver.Chrome()

# Start page to scrape
#driver.get("https://www.petfinder.com/search/dogs-for-adoption/us/ny/white-plains/?distance=10&sort%5B0%5D=recently_added")
driver.get("https://www.petfinder.com/search/dogs-for-adoption/us/pa/state-college/?distance=10&sort%5B0%5D=recently_added")

#STEPS:
# 1 - From search result page - Click dog's pic (pet_tile) to go to its page
# 2 - Scrape individual pages
# 3 - Click "Next Pet"
# 4 - Repeat 2-3 until no more pages

pet_tile = driver.find_element_by_xpath('//a[@class="petCard-overlay-link"]').get_attribute("href")
driver.get(pet_tile)

index = 1  #First pet
# while True:  #until no Next button appears
while index <=2:
    try:
        print("Scraping Pet # " + str(index))
        index = index + 1
        # Find all the info on the page
        pet_dict = {}

        name = driver.find_element_by_xpath('.//h1[@id="Detail_Main"]').text
        organization = driver.find_element_by_xpath('.//pf-truncate[@line-count="3"]').text

        pet_dict['name'] = name
        pet_dict['organization'] = organization
        print(pet_dict.values())


        # next_pet = driver.find_element_by_xpath('(.//a[@pf-ensighten])[2]').get_attribute("href")  #bad link
        #next_pet = driver.find_element_by_class_name("pdpNav-inner-btn").get_attribute("href")
        elems = driver.find_elements_by_tag_name("script")
        # for elem in elems:
        #     print("NEXT +", elem.get_attribute("innerHTML"))
        # need to search this for the publish date  -- think it's the 41st element

        #driver.get(next_pet)

    except Exception as e:
        print(e)
        driver.close()
        break
