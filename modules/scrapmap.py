import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class Scrapping:
    '''
        une fonction qui scrapp les donner de map!!
        
    '''
    
    def __init__(self,origine,destination):
        self.origine = origine 
        self.destination = destination
        

        #def isConnected():
            #eturn requests.get(env.get("LINK")).status_code == 200
    def scrap(self):
        browser = webdriver.Firefox()
        browser.get('https://maps.google.com')

        element_input_lieu = browser.find_element(By.ID,"searchboxinput")
        element_input_lieu.send_keys(self.origine)
        element_input_lieu.send_keys(Keys.ENTER)
        
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")))
            itenerary_button = browser.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button')
            itenerary_button.click()
                
            second_input = True
                
            WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")))
            element_input_lieu = browser.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
            element_input_lieu.send_keys(self.destination)
            element_input_lieu.send_keys(Keys.ENTER)
                    
                    #WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div/div[1]/div[3]/div[2]/h1[1]/span")))
                    #resultats = browser.find_element(by.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div/div[1]/div[3]/div[2]/h1[1]/span")
                    
            sleep(4)
            driver.get_screenshot_as_file("screenshot.png")
                    #driver.quit()
            print("end...")
                    
            go = False
                
        except:
            pass
'''
element_mail = browser.find_element(By.NAME,"email")
element_mail.send_keys("angelo21.aps2b@gmail.com")

element_pass = browser.find_element(By.NAME, "password")
element_pass.send_keys("angelokratos.260702//")

browser.find_element(By.NAME, "submit").click()

WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.ID,"searchFieldx")))
element_search = browser.find_element(By.ID, "searchFieldx")
element_search.send_keys("psychologie")
element_search.send_keys(Keys.ENTER)

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Psychol")))
ex = browser.find_element(By.PARTIAL_LINK_TEXT, "Psychol").text
for book in ex:
    print(book)'''
    
if __name__ == '__main__':
    origine = 'FJKM Ambatoroka'
    destination = "ZaraTany-CABINET GEOMETRE EXPERT, Sampanan'i, Tananarive"
    execute = Scrapping(origine, destination)
    execute.scrap()