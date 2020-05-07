from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import csv


#browser = webdriver.Chrome('/Users/luthfi/python/automatelogin/chromedriver');
browser = webdriver.Chrome('./chromedriver');

usernamess = [
	"mynameistobi@gmail.com", 
	"wuriwijayanti29@yahoo.co.id", 
	"anindya.aisyah.bintoro@gmail.com", 
	"diandraalmirabintoro@gmail.com"
	]
usernames = []

with open('./hectorlist.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
			line_count += 1

        else:
			line_count += 1
            
			usernameStr = row[0];
			passwordStr = row[1];

			if not passwordStr:
				continue
				
			browser.get( 'https://hectortrade.co/login/login' );

			checklogin = WebDriverWait(browser, 20).until(
				EC.presence_of_element_located( (By.ID, "loginx" ) )
			);

			try:
				checkallload = WebDriverWait(browser, 1).until( EC.presence_of_element_located( (By.ID, "onlywait1second" ) ) );
			except TimeoutException:
				print "It's ok"
			
			username = browser.find_element_by_css_selector("input[name='email']" );
			username.send_keys(usernameStr);

			password = browser.find_element_by_id('password');
			password.send_keys(passwordStr);

			button = browser.find_element_by_id('loginx');
			button.click();

			sidebar_menu = WebDriverWait(browser, 20).until(
				EC.presence_of_element_located( (By.CLASS_NAME, "sidebar-menu" ) )
			);

			logout = browser.find_element_by_partial_link_text('LogOut');
			logout.click();

			about = WebDriverWait(browser, 20).until(
				EC.presence_of_element_located( (By.ID, "about" ) )
			);
    #print(f'Processed {line_count} lines.')

for i in range(len(usernames)):
    
	usernameStr = usernames[i];
	passwordStr = 'pass123qwe';

	browser.get( 'https://hectortrade.co/login/login' );

	checklogin = WebDriverWait(browser, 20).until(
		EC.presence_of_element_located( (By.ID, "loginx" ) )
	);

	try:
		checkallload = WebDriverWait(browser, 1).until( EC.presence_of_element_located( (By.ID, "adsfadfasdf" ) ) );
	except TimeoutException:
		print "It's ok"
	
	username = browser.find_element_by_css_selector("input[name='email']" );
	username.send_keys(usernameStr);

	password = browser.find_element_by_id('password');
	password.send_keys(passwordStr);

	button = browser.find_element_by_id('loginx');
	button.click();

	sidebar_menu = WebDriverWait(browser, 20).until(
		EC.presence_of_element_located( (By.CLASS_NAME, "sidebar-menu" ) )
	);

	logout = browser.find_element_by_partial_link_text('LogOut');
	logout.click();

	about = WebDriverWait(browser, 20).until(
		EC.presence_of_element_located( (By.ID, "about" ) )
	);