# autoimagepost.py

import os
import wikipedia
import time
# import re = regularexpression
#help(re) ดู help

wikipedia.set_lang('th')


# print(imgfile)
imgfile = os.listdir()
print('-------')

wordlist = []

for img in imgfile:
	if img[-3:] == 'jpg' or img[-3:] == 'png':  
	# less than -3 is 3 letter สุดท้าย ที่เป็น file jpg
		print(img)
		fn = img.split('.')[0]
		wordlist.append(fn)

# print(wordlist)

alltitle = []
alldata = []

for wl in wordlist:
	data = wikipedia.summary(wl)
	page = wikipedia.page(wl)
	title = page.title
	alltitle.append(title)
	alldata.append(data)

	print('Topic: {}'.format(wl))
	print(data)
	print('===========')

	# print(page.content)

	print('----------')

##############################################
# copy from Autowebform.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverpath = r'C:\Users\benchawan\chromedriver'
driver = webdriver.Chrome(driverpath)

url = 'http://www.uncle-machine.com/login/'

driver.get(url)

username = driver.find_element_by_id('username')
username.send_keys('momotaro123@gmail.com')

password = driver.find_element_by_id('password')
password.send_keys('12345')
password.send_keys(Keys.RETURN)  # press enter after type password

# button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
# button.click()

addurl = 'http://www.uncle-machine.com/addproduct/'

driver.get(addurl) # goto addurl
pdname = driver.find_element_by_id('name')
pdprice = driver.find_element_by_id('price')
pddetail = driver.find_element_by_id('detail')
photo = driver.find_element_by_id('photo')

pd1_name = alltitle[1]
pd1_price = 1000
pd1_detail = alldata[1]
photopath = r'D:\ML_CBS\Bootcamp-Uncle_Eng_all\EP4\Avogado.jpg'

pdname.send_keys(pd1_name)
pdprice.send_keys(pd1_price)
pddetail.send_keys(pd1_detail)
photo.send_keys(photopath)
time.sleep(5)

# r คือ raw string

button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
button.click()






