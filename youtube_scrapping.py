# Import libraries:
from selenium import webdriver
from time import sleep

# Set Search words:
search_for = input('Search You tube for :')

# Create web driver instannce & Open You Tube:
path = r'C:\Users\hp\Downloads\Compressed\chromedriver.exe'       # path of chrome driver
driver = webdriver.Chrome(path)
driver.maximize_window()                                          # Maximize window for better appearance
driver.get('https://www.youtube.com/')

# Type our search words in you tube search bar & click on search button:
sleep(3)
search_input = driver.find_element_by_xpath('//input[@id="search"]')
search_input.send_keys(search_for)
sleep(4)
search_button = driver.find_element_by_xpath("""//button[@id='search-icon-legacy']""")
search_button.click()

# Then filter Videos by date (first video is most recent one):
sleep(10)
filter_button = driver.find_element_by_link_text('FILTER')
filter_button.click()
sleep(10)
upload_date_filter = driver.find_element_by_link_text('Upload date')

# Navigate with browser to the page of recent related videos:
filter_link = upload_date_filter.get_attribute('href')        # get the link of filtered page
driver.get(filter_link)

# iterate through videos and print required data:
new_videos = driver.find_elements_by_xpath("""//a[@id="video-title"]""")[0:10]
for video in new_videos:
    print(video.text, ':', video.get_attribute('href'))

driver.close()