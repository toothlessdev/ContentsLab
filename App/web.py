import os
import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import url as URL

# Exceptions
class TooManySearchResultsException(Exception):
    def __init__(self):
        super().__init__(f"[ERR!] Too manay Elements !")

class InputFieldVerifyingException(Exception):
    def __init__(self):
        super().__init__(f"[WARN!] Input Field is Different! Replacing ... ")



class Web:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.browser = webdriver.Chrome(options=options, executable_path="./driver/chromedriver")
        self.progression = 0

    def FindElement(self, by, path):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((by, path)))

    def Login(self, id, pw):
        self.browser.get(url=URL.main_url)
        self.browser.implicitly_wait(time_to_wait=5)

        INTRO_USER_ID = self.FindElement(By.ID, URL.Login.ID_intro_user_id)
        INTRO_USER_PW = self.FindElement(By.ID, URL.Login.ID_intro_user_pw)
        INTRO_USER_LOGIN_BTN = self.FindElement(By.XPATH, URL.Login.XPATH_intro_user_login)

        INTRO_USER_ID.send_keys(id)
        INTRO_USER_PW.send_keys(pw)
        INTRO_USER_LOGIN_BTN.click()

        # Access Main WorkSpace
        TOURISM_CONTENTS_MANAGEMENT = self.FindElement(By.XPATH, URL.WorkSpace.XPATH_TOURISM_CONTENTS_MANAGEMENT)
        TOURISM_CONTENTS_TRANSLATION = self.FindElement(By.ID, URL.WorkSpace.ID_TOURISM_CONTENTS_TRANSLATION)

        TOURISM_CONTENTS_MANAGEMENT.click()
        TOURISM_CONTENTS_TRANSLATION.click()

        SUBCATEGORY = self.FindElement(By.XPATH, URL.WorkSpace.XPATH_SUBCATEGORY)
        SUBCATEGORY.click()

        SUBCATEGORY_SHOP = self.FindElement(By.XPATH, URL.WorkSpace.XPATH_SUBCATEGORY_SHOP)
        SUBCATEGORY_SHOP.click()
        
        SUBCATEGORY_DUTYFREE = self.FindElement(By.XPATH, URL.WorkSpace.XPATH_SUBCATEGORY_DUTYFREE)
        SUBCATEGORY_DUTYFREE.click()

    def SearchContents(self, name, addr, contents_type="en"):
        
        try:
            CONTENTS_NAME = self.browser.find_element(By.ID, "contentsName").send_keys(name)
            CONTENTS_ADDR = self.browser.find_elements(By.ID, "searchAddress")[1].send_keys(addr)
            time.sleep(2)

            CONTENTS_SEARCH_BTN = self.browser.find_element(By.XPATH, URL.Search.XPATH_CONTENTS_SEARCH_BTN)
            CONTENTS_SEARCH_BTN.click()
            time.sleep(2)
            
            RENDERING_ZONE = self.browser.find_elements(By.CSS_SELECTOR, ".MuiDataGrid-renderingZone > div")
            if len(RENDERING_ZONE) > 1:
                print(f"[ERR!] Too manay Elements : { len(RENDERING_ZONE) }")
                raise TooManySearchResultsException

        except Exception as e:
            print(e)
            print(f"[ERR!] Cannot find '{name}', '{addr}' at 'conlab.visitkorea.or.kr'")
            print(f"[ERR!] Please Click the Contents Element And Continue")
            os.system("pause")
            return False

        else:
            return True

    def AccessEditPage(self):
        time.sleep(3)
        CONTENTS_EDIT_FRAME = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_EDIT_FRAME)
        CONTENTS_EDIT_FRAME.click()
        time.sleep(1.5)

    def Replace(self, element, data):
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)
        if data == None:
            element.send_keys("")
        else:
            element.send_keys(data)

    def ReplaceTranslatedData(self, translated_data):
        
        try:
            while True:
                READY_STATE = self.browser.execute_script("return document.readyState")
                if READY_STATE == "complete":
                    break
                else:
                    continue

            if self.progression == 0:
                print("Collecting Elements ... ")
                self.CONTENTS_NAME = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_NAME)
                self.CONTENTS_ADDR = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_ADDR)
                self.CONTENTS_ADDR_DETAIL = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_ADDR_DETAIL)
                self.CONTENTS_PRODUCT = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_PRODUCT)
                self.CONTENTS_TEL = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_TEL)
                self.CONTENTS_OPEN = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_OPEN)
                self.CONTENTS_CLOSE = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_CLOSE)
                self.CONTENTS_REFUND_INFO = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_REFUND_INFO)
                self.CONTENTS_LANG_INFO = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_LANG_INFO)
                self.CONTENTS_PARKING_LOT = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_PARKING_LOT)


            if self.progression < 1:
                print(f"[1/16] Replacing 'contents_name' to '{translated_data['name']}' ... ")
                self.Replace(self.CONTENTS_NAME, translated_data['name'])
               
                # verify
                verification = self.VerifyInputField(self.CONTENTS_NAME, translated_data['name'])
                if verification:
                    self.progression = 1
                else:
                    os.system("pause")

            if self.progression < 2:
                print(f"[2/16] Select language to 'English(ENU)' ... ")
                self.LANG_SELECT_FIELD = self.FindElement(By.XPATH, URL.Edit.XPATH_LANG_SELECT_FIELD)
                self.LANG_SELECT_FIELD.send_keys(Keys.ENTER)

                self.LANG_SELECT = self.FindElement(By.XPATH, URL.Edit.XPATH_LANG_SELECT)
                self.LANG_SELECT.send_keys(Keys.ENTER)
                self.progression = 2

            if self.progression < 3:
                print(f"[3/16] Replacing 'addr' to '{translated_data['addr']}' ... ")
                self.Replace(self.CONTENTS_ADDR, translated_data['addr'])

                verification = self.VerifyInputField(self.CONTENTS_ADDR, translated_data['addr'])
                if verification:
                    self.progression = 3
                else:
                    os.system("pause")

            
            if self.progression < 4:
                print(f"[4/16] Replacing 'addr_detail' to '{translated_data['addr_detail']}' ... ")
                self.Replace(self.CONTENTS_ADDR_DETAIL, translated_data['addr_detail'])

                verification = self.VerifyInputField(self.CONTENTS_ADDR_DETAIL, translated_data['addr_detail'])
                if verification:
                    self.progression = 4
                else:
                    os.system("pause")

            if self.progression < 5:
                print(f"[5/16] Replacing 'product' to '{translated_data['product']}' ... ")
                self.Replace(self.CONTENTS_PRODUCT, translated_data['product'])

                verification = self.VerifyInputField(self.CONTENTS_PRODUCT, translated_data['product'])
                if verification:
                    self.progression = 5
                else:
                    os.system("pause")

            if self.progression < 6:
                print(f"[6/16] Replacing 'tel' to '{translated_data['tel']}' ... ")
                self.Replace(self.CONTENTS_TEL, translated_data['tel'])
                
                verification = self.VerifyInputField(self.CONTENTS_TEL, translated_data['tel'])
                if verification:
                    self.progression = 6
                else:
                    os.system("pause")

            if self.progression < 7:
                print(f"[7/16] Replacing 'open' to '{translated_data['open']}' ... ")
                self.Replace(self.CONTENTS_OPEN, translated_data['open'])
                
                verification = self.VerifyInputField(self.CONTENTS_OPEN, translated_data['open'])
                if verification:
                    self.progression = 7
                else:
                    os.system("pause")

            if self.progression < 8:
                print(f"[8/16] Replacing 'close' to '{translated_data['close']}' ... ")
                self.Replace(self.CONTENTS_CLOSE, translated_data['close'])
                
                verification = self.VerifyInputField(self.CONTENTS_CLOSE, translated_data['close'])
                if verification:
                    self.progression = 8
                else:
                    os.system("pause")

            if self.progression < 9:
                print(f"[9/16] Replacing 'refund_counter_operator and refund_method ... ")
                contents_refund_info = translated_data['refund_counter_operator'] + '\n' + translated_data['refund_method']
                self.Replace(self.CONTENTS_REFUND_INFO, contents_refund_info)

                verification = self.VerifyInputField(self.CONTENTS_REFUND_INFO, contents_refund_info)
                if verification:
                    self.progression = 9
                else:
                    os.system("pause")

            if self.progression < 10:
                print(f"[10/16] Replacing 'lang_info' to {translated_data['lang_info']} ... ")
                self.Replace(self.CONTENTS_LANG_INFO, translated_data['lang_info'])

                verification = self.VerifyInputField(self.CONTENTS_LANG_INFO, translated_data['lang_info'])
                if verification:
                    self.progression = 10
                else:
                    os.system("pause")

            if self.progression < 11:
                print(f"[11/16] Replacing 'parking_lot' to {translated_data['parking_lot']} ... ")
                self.Replace(self.CONTENTS_PARKING_LOT, translated_data['parking_lot'])

                verification = self.VerifyInputField(self.CONTENTS_PARKING_LOT, translated_data['parking_lot'])
                if verification:
                    self.progression = 11
                else:
                    os.system("pause")

            if self.progression < 12:
                print("[12/16] Opening SubCategory Elements ... ")
                self.CONTENTS_STORAGE_BTN = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_STORAGE_BTN)
                self.CONTENTS_STORAGE_BTN.send_keys(Keys.ENTER)

                self.CONTENTS_PAYMENT_METHOD_BTN = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_PAYMENT_METHOD_BTN)
                self.CONTENTS_PAYMENT_METHOD_BTN.send_keys(Keys.ENTER)

                self.CONTENTS_TOILET_BTN = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_TOILET_BTN)
                self.CONTENTS_TOILET_BTN.send_keys(Keys.ENTER)
                self.progression = 12

            if self.progression < 13:
                print("[13/16] Getting innerHTML from 'Storage', 'Payment', 'Toilet' field ... ")
                self.CONTENTS_MULTI_SELECT_ROOT = self.browser.find_elements(By.CLASS_NAME, "MuiSelect-root")
                self.CONTENTS_STORAGE_FIELD = self.CONTENTS_MULTI_SELECT_ROOT[15].get_attribute("innerHTML")
                self.CONTENTS_PAYMENT_FIELD = self.CONTENTS_MULTI_SELECT_ROOT[16].get_attribute("innerHTML")
                self.CONTENTS_TOILET_FIELD = self.CONTENTS_MULTI_SELECT_ROOT[19].get_attribute("innerHTML")
                self.progression = 13

            if self.progression < 14:
                print("[14/16] Verifying 'storage' field ... ", end="")
                if self.CONTENTS_STORAGE_FIELD == "none" and translated_data['storage'] == "없음":
                    print("true!")
                elif self.CONTENTS_STORAGE_FIELD == "able" and translated_data['storage'] == "있음":
                    print("true!")
                else:
                    print("false!")
                    raise Exception(f"[Error] 'storage' field is different with DataFrame !")
                self.progression = 14

            if self.progression < 15:
                print("[15/16] Verifying 'payment method' field ... ", end="")
                if self.CONTENTS_PAYMENT_FIELD == "none" or self.CONTENTS_PAYMENT_FIELD == "unable":
                    raise Exception(f"[Error] Payment Method is {self.CONTENTS_PAYMENT_FIELD} !")
                print("true!")
                self.CONTENTS_PAYMENT_METHOD = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_PAYMENT_METHOD)
                self.Replace(self.CONTENTS_PAYMENT_METHOD, translated_data['payment_method'])

                verification = self.VerifyInputField(self.CONTENTS_PAYMENT_METHOD, translated_data['payment_method'])
                if verification:
                    self.progression = 15
                else:
                    os.system("pause")

            if self.progression < 16:
                print("[16/16] Verifying 'toilet' field ... ", end="")
                if self.CONTENTS_TOILET_FIELD == "none" and translated_data['toilet_kr'] == "없음":
                    print("true!")
                elif self.CONTENTS_TOILET_FIELD == "able" and translated_data['toilet_kr'] == "있음":
                    print("true!")
                else:
                    print("false!")
                    raise Exception(f"[Error] 'toilet' field is different with DataFrame !")

                self.CONTENTS_TOILET_INFO = self.FindElement(By.XPATH, URL.Edit.XPATH_CONTENTS_TOILET_INFO)
                self.Replace(self.CONTENTS_TOILET_INFO, translated_data['toilet'])

                self.progression = 16

        except ElementNotInteractableException as e:
            self.ReplaceTranslatedData(translated_data=translated_data)
        else:
            self.progression = 0

    def VerifyInputField(self, element, value):
        try:
            value = "" if value == None else value
            if element.get_attribute("value") == value:
                return True
            else:
                self.Replace(element, value)
                raise InputFieldVerifyingException
        except InputFieldVerifyingException as e:
            print(e)
            return self.VerifyInputField(element, value)
        

    def Save(self):
        SAVE_BTN = self.FindElement(By.XPATH, URL.Edit.XPATH_SAVE_BTN)
        SAVE_BTN.send_keys(Keys.ENTER)

        while True:
            try:
                CONFIRM_BTN = self.browser.find_elements(By.XPATH, URL.Edit.XPATH_CONFIRM_BTN)[-1]
                CONFIRM_BTN.send_keys(Keys.ENTER)
            except:
                continue
            else:
                break

        time.sleep(10)

        while True:
            try:
                CONFIRM_BTN = self.browser.find_elements(By.XPATH, URL.Edit.XPATH_CONFIRM_BTN)[-1]
                CONFIRM_BTN.send_keys(Keys.ENTER)
            except:
                continue
            else:
                break

        time.sleep(1)

    def ClearSearchContents(self):
        self.FindElement(By.ID, "contentsName").clear()
        time.sleep(0.5)
        self.browser.find_elements(By.ID, "searchAddress")[-1].send_keys(Keys.CONTROL + 'a') 
        self.browser.find_elements(By.ID, "searchAddress")[-1].send_keys(Keys.DELETE) 

        SEARCH_BTN = self.FindElement(By.XPATH, URL.Search.XPATH_CONTENTS_SEARCH_BTN)
        INIT_BTN = self.FindElement(By.XPATH, URL.Search.XPATH_CONTETNS_SEARCH_INIT_BTN)

        INIT_BTN.click()