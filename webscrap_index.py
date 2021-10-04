import pandas as pd
from selenium import webdriver
from read_excel import get_Tags
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import transformdates


#Webdriver exe
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
# Go to the Dell website
driver.get('https://www.dell.com/support/home/en-us?app=warranty')
print(driver.title)

#get data
TAGS_LIST = get_Tags()

#get data from the for loop
modelo_for= list()
warranty_for =list()

for tag in TAGS_LIST:
    try:
        # Seacrh tag box
        SEARCH_TAG_BOX = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="inpEntrySelection"]'))
        )
        #SEARCH_TAG_BOX = driver.find_element_by_xpath('//*[@id="inpEntrySelection"]')
        # Colocar texto en un input
        SEARCH_TAG_BOX.send_keys(tag)
        # Tecla enter (key return)
        SEARCH_TAG_BOX.send_keys(Keys.RETURN)
    except:
        print('Error al hacer una busqueda')
    try:
        # Hacemos un wait, pero un elemento padre que ocupemos
        time.sleep(5)
        car_element = driver.find_element_by_xpath('//*[@id="site-wrapper"]/div/div[5]/div/div[2]/div[1]/div[2]/div/div')
        ##Obtener info del tag buscado
        get_TAG_MODEL = car_element.find_element_by_xpath('//*[@id="site-wrapper"]/div/div[5]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/h1')
        get_TAG_Warranty= car_element.find_element_by_xpath('//*[@id="ps-inlineWarranty"]/div[1]/div/p[2]')

        #Append to a list
        warranty_for.append(get_TAG_Warranty.text)
        modelo_for.append(get_TAG_MODEL.text)

        driver.get("https://www.dell.com/support/home/en-us?app=products")
    except:
        print("Un error al guardar las etiquetas")


driver.quit()
time.sleep(3)
warranty_date = transformdates.get_Date(warranty_for)


df = pd.DataFrame({'TAGS': TAGS_LIST,'MODEL': modelo_for, 'Warranty': warranty_date,  })

print(df)

file_path = input('Ingrese la direccion donde quiere que se guarde:\n')
file_name = input('\nIngrese el nombre del file: ')

file= file_path+"\\"+file_name+'.xlsx'

if file_name != 0 or file_name != None and file_path != 0 or file_path != None:
    df.to_excel(file, index=False)
    print(' \nEl file se guardo en la siguinete ruta: '+file_name)
else :
    df.to_excel('C:\\Users\\test.xlsx', index=False)
    print(' \nEl file se guardo en la siguinete ruta: C:\\Users ')
