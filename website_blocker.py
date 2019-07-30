import time
from datetime import datetime as dt
import os

host_temp = 'hosts'
host_path = os.path.join('hosts')
redirect = '127.0.0.1'
website_list = ['https://facebook.com', 'www.twitter.com', 'www.instagram.com','facebook.com','twitter.com','instagram.com']


while True:
	if dt(dt.now().year, dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print('working hours')
		with open(host_path,'r+') as file:
			content = file.read()
			print(content)
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + ' ' + website + '\n')

	else:
		with open(host_path, 'r+') as file: 
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
		print('free to roam')
	time.sleep(5)