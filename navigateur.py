from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



def ouvrir_session_chrome():
	chrome_options = webdriver.ChromeOptions()
	# service = webdriver.ChromeService(executable_path="chromedriver.exe")
	# A telecharger ici : https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json
	# chrome_options.add_argument('--ignore-certificate-errors')
	# chrome_options.add_argument('--allow-insecure-localhost')
	# chrome_options.add_argument('--disable-web-security')
	# chrome_options.add_argument("--headless")
	chrome_options.add_argument("--mute-audio")
	chrome_options.add_argument('--log-level=3')
	# chrome_options.add_argument("--remote-debugging-port=12345") # select a port
	# chrome_options.add_argument('--incognito')
	# chrome_options.add_argument("start-maximized")
	chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
	chrome_options.add_argument("--disable-blink-features=AutomationControlled")
	chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
	chrome_options.add_experimental_option("useAutomationExtension", False)
	# path_to_extension = r"ublock/uBlock-Origin.crx"
	# chrome_options.add_extension(path_to_extension)
	global driver
	driver = webdriver.Chrome(options=chrome_options) # add service=service if local path is used
	driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
	global wait
	wait = WebDriverWait(driver, 20)


def fermer_session_chrome():
	driver.quit()

def refresh():
	driver.refresh()

def open_newtab(url):
    driver.switch_to.new_window('tab')
    driver.get(url)
