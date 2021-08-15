# autoimagepost.py

import os
import wikipedia
import time
# import sys
# print(sys.path)
# import re = regularexpression
#help(re) ดู help

wikipedia.set_lang('th')


# print(imgfile)
imgfile = os.listdir()
print('-------')

wordlist = []
pathlist = []
mainpath = os.getcwd()
for img in imgfile:
	if img[-3:] == 'jpg' or img[-3:] == 'png':  
		# less than -3 is 3 letter สุดท้าย ที่เป็น file jpg
		# print(img)
		fn = img.split('.')[0]
		wordlist.append(fn)
		path = os.path.join(mainpath,img)
		# print(path)
		pathlist.append(path)




alltitle = []
alldata = []
allprice = [550,1000,200,500]

for wl in wordlist:
	try:
		# ลองให้โปรแกรมค้นหา ถ้ารันแล้วติด error จะแจ้งว่าไม่มีข้อมูล
		data = wikipedia.summary(wl)
		page = wikipedia.page(wl)
		title = page.title
	except:
		title = wl 
		data = 'ไม่มีข้อมูล'
		
	alltitle.append(title)
	alldata.append(data)
	print('Topic: {}'.format(wl))
	print(data)
	print('===========')
	print('----------')

print(alltitle)

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

# add product

for pn,pp,pd,pt in zip(alltitle,allprice,alldata,pathlist):
	pdname = driver.find_element_by_id('name')
	pdprice = driver.find_element_by_id('price')
	pddetail = driver.find_element_by_id('detail')
	photo = driver.find_element_by_id('photo')

	pd1_name = pn
	pd1_price = pp
	pd1_detail = pd
	photopath = pt
	# photopath = r'C:\Users\benchawan\OneDrive - IRPC\Desktop\UncEng_2021\EP4\ขนุน.jpg'

	pdname.send_keys(pd1_name)
	pdprice.send_keys(pd1_price)
	pddetail.send_keys(pd1_detail)
	photo.send_keys(photopath)
	time.sleep(5)

	button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
	button.click()






