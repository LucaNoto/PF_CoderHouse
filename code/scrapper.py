from selenium import webdriver
import time


def browser_config(url):
    driver = webdriver.Chrome('chromedriver')
    driver.set_window_position(0, 0, windowHandle='current')
    driver.get(url)

    return driver

def click_button_byXpath(xpath):
    button = ''
    while not button:
        try:
            button = driver.find_element("xpath",xpath)
            button.click()
            time.sleep(1)
        except:continue



monthsArray = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']

driver = browser_config("http://www.ssp.sp.gov.br/transparenciassp/")


time.sleep(3)


dictDataCategories = {
        'FurtoVeic': "/html/body/form/div[4]/div/div[5]/div[2]/a",
        'RouboVeic': "/html/body/form/div[4]/div/div[5]/div[3]/a",
        'FurtoCel': "/html/body/form/div[4]/div/div[6]/div[1]/a",
        'RouboCel': "/html/body/form/div[4]/div/div[6]/div[2]/a"
        }


click_button_byXpath(dictDataCategories['FurtoVeic']) #CHOOSING CATEGORIES
click_button_byXpath("/html/body/form/div[4]/div/div[7]/fieldset/div[1]/select") #REGIONS DROPDOWN
click_button_byXpath("/html/body/form/div[4]/div/div[7]/fieldset/div[1]/select/option[3]") #CHOOSING "DECAP" 


for i in range(3,5):
    print(f'Ano: {2023-i}')
    click_button_byXpath(f"/html/body/form/div[4]/div/section/div[1]/ul/li[{i}]/a") #CHOOSING YEAR
    rangeMax = 13
    if i == 1:
        rangeMax = 9
    for j in range(1,rangeMax):
        print(f'    Mês: {monthsArray[j-1]}')
        click_button_byXpath(f"/html/body/form/div[4]/div/section/div[2]/ul/li[{j}]/a") #CHOOSING MONTH
        click_button_byXpath("/html/body/form/div[4]/div/section/div[3]/div[2]/div/div/button[2]") #CLICK 'EXPORT BUTTON'