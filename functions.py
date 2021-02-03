from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import datetime
import time


def openCoin(driver):
    driver.get("https://coinmarketcap.com/currencies/dogecoin/")
    window_before = driver.window_handles[0]
    return window_before


def getDoge(driver, window_before):
    if driver.current_window_handle == window_before:
        precioDoge = driver.find_element_by_class_name("priceValue___11gHJ").text
        print(precioDoge)
        return precioDoge
    else:
        driver.switch_to.window(window_before)


def openWhatsapp(driver):
    driver.execute_script('''window.open("https://web.whatsapp.com", "_blank");''')
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    return window_after


def sendMessage(driver, precioDoge):
    contact = "Notas Whatsapp"
    text = "La fecha y hora es: " + str(
        datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")) + " || DOGECOIN: U$DT " + str(precioDoge)
    text2 = "-------------------------------------------------------"
    inp_xpath_search = "//*[@id='side']/div[1]/div/label/div/div[2]"
    input_box_search = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
    input_box_search.click()
    time.sleep(1)
    input_box_search.send_keys(contact)
    time.sleep(1)

    selected_contact = driver.find_element_by_xpath("//span[@title='" + contact + "']")
    selected_contact.click()

    inp_xpath = "//*[@id='main']/footer/div[1]/div[2]/div/div[2]"
    input_box = driver.find_element_by_xpath(inp_xpath)
    time.sleep(1)

    input_box.send_keys(text + Keys.ENTER)
    input_box.send_keys(text2 + Keys.ENTER)

    time.sleep(1)