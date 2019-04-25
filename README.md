#Bitly url shorterer

Python script that either creates a bitlink of an url, or outputs total number of clicks of a bitlink , depending on user input.

##How to install

You need to get generic access token . To do so create an account at [bitly.com](https://bitly.com) , then click [generate token](https://bitly.com/a/oauth_apps)

Token is a string that looks like this : 17c09e20ad155405123ac1977542fecf00231da7

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:


	pip install -r requirements.txt

## An exapmle 
Creating a bitlink

	python main.py https://google.com

	 	
![](https://nofile.io/f/6ykhvo3QSoH/Untitled.png)


##Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.