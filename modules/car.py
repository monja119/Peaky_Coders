import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import cv2


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
                
            WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")))
            element_input_lieu = browser.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
            element_input_lieu.send_keys(self.destination)
            element_input_lieu.send_keys(Keys.ENTER)
            
            car = browser.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/button')
            car.click()
            browser.save_screenshot("image.png")
            sleep(6)
            #WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]")))
            
            resultat = browser.find_element(By.ID,"section-directions-trip-0")
            resultat = resultat.text
            
            resultat = resultat.split('\n')
            resultat = [i for i in resulta if i != 'Détails']
            print(resultat)
            print(type(resultat))
            print(resultat[0])
            browser.save_screenshot("image.png")
                    
            #WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div/div[1]/div[3]/div[2]/h1[1]/span")))
            #resultats = browser.find_element(by.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div/div[1]/div[3]/div[2]/h1[1]/span")
            
            
        except:
            pass
        
        #browser.close()


def croppingImage(name):
    '''
        Une fonction qui croppe l'image
    '''
    image = cv2.imread('image.png')
    shape = image.shape
    w = image.shape[0]
    h = image.shape[1]
    print(shape)
    cropped_image = image[80:w-80, int((h/2))-50:int((h)-50)]
    shape = cropped_image.shape
    print(shape)
    cv2.imwrite(f"{name}.png", cropped_image)
    return name


    
if __name__ == '__main__':
    origine = 'Université Catholique de Madagascar, 3GHR+3VG, Antananarivo'
    destination = "Mahamasina, Tananarive"
    execute = Scrapping(origine, destination)
    execute.scrap()
    name = str(origine + destination)
    croppingImage(name)
    