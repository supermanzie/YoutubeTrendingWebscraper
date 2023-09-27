from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/feed/trending")
    titles = driver.find_elements(By.ID, 'video-title')
    titles = [a.get_attribute('title') for a in titles]
    num = 1
    for title in titles:
        if len(title)>0:
            print("The #" + str(num) +" trending video is " + title)
            num += 1
    driver.quit()

main()