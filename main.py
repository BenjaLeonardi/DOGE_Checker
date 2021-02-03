#Sera mejor meter el webdriver en el main o en el otro py?
from selenium import webdriver
import functions

#Abro el driver (Ver si es mejor aca o en otro lado
driver = webdriver.Chrome()

#Mensaje de precaucion
print("Scanee el codigo QR antes de seguir!!!")

#Defino precioDoge y Abro whatsapp por primera vez
window_before = functions.openCoin(driver)
precioDoge = functions.getDoge(driver, window_before)
window_after = functions.openWhatsapp(driver)

#Loop pedorro para manejar de forma prolija
opc = 1
while opc == 1:
    #Llamo a la funcion para mandar el mensaje
    functions.sendMessage(driver, precioDoge)
else:
    driver.quit()
