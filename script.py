import time
 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# web driver manager: https://github.com/SergeyPirogov/webdriver_manager
# will help us automatically download the web driver binaries
# then we can use `Service` to manage the web driver's state.
from webdriver_manager.chrome import ChromeDriverManager

def extract(element):
    title = element.find_element(By.CSS_SELECTOR, "div.preview-title").text
    author = element.find_element(By.CSS_SELECTOR, "div.preview-author").text
    rating = element.find_element(By.CSS_SELECTOR, "div.preview-details p.preview-rating").text
    price = element.find_element(By.CSS_SELECTOR, "div.preview-details p.preview-price").text

    return {"title": title, 'author': author, 'rating': rating, 'price': price}        

# start the timer
start = time.time()
 
options = webdriver.ChromeOptions()
options.headless = True
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
# define the chrome service and pass it to the driver instance
chrome_service = Service(chrome_path)
driver = webdriver.Chrome(service=chrome_service, options=options)
 
url = "https://danube-webshop.herokuapp.com/"
 
driver.get(url)
# get the first page and click to the its link
# first element will be the Crime & Thrillers category
time.sleep(1)
crime_n_thrillers = driver.find_element(By.CSS_SELECTOR, "ul[class='sidebar-list'] > li")
print(crime_n_thrillers)
crime_n_thrillers.click()
time.sleep(1)
# get the data div and extract the data using beautifulsoup
books = driver.find_elements(By.CSS_SELECTOR, "div.shop-content li.preview")

extracted_data = []
print(books)
for element in books:
    data = extract(element)
    extracted_data.append(data)
    print(data)

end = time.time()
 
print(f"The whole script took: {end-start:.4f}")
 
driver.quit()
