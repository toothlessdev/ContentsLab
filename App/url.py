main_url = "https://conlab.visitkorea.or.kr/kto-rms"

# Elements

class Login:
    ID_intro_user_id = "intro-user-id"
    ID_intro_user_pw = "intro-user-password"
    XPATH_intro_user_login = "/html/body/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/button"

class WorkSpace:
    XPATH_TOURISM_CONTENTS_MANAGEMENT = "/html/body/div/div[3]/div[1]/div/div/div[3]/div[2]/div[1]"
    ID_TOURISM_CONTENTS_TRANSLATION = "tourism-contents-translation"

    
    XPATH_SUBCATEGORY = "/html/body/div/div[3]/div[2]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/ul/li/li[8]/div/button/span[1]/span"
    XPATH_SUBCATEGORY_SHOP = "/html/body/div/div[3]/div[2]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/ul/li/li[8]/ul/li[4]/div/button/span[1]/span"
    XPATH_SUBCATEGORY_DUTYFREE = "/html/body/div/div[3]/div[2]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/ul/li/li[8]/ul/li[4]/ul/li[3]/div/button/span[1]/span"

class Search:
    XPATH_CONTENTS_SEARCH_BTN = "/html/body/div/div[3]/div[2]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[2]/button[1]"
    XPATH_CONTETNS_SEARCH_INIT_BTN = "/html/body/div/div[3]/div[2]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[2]/button[2]"

class Edit:
    XPATH_CONTENTS_EDIT_FRAME = '//*[@id="__next"]/div[3]/div[2]/div/div/div/div/div/div[3]/div/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[7]'
    XPATH_CONTENTS_NAME = "/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div[1]/div/div/input"
    XPATH_CONTENTS_ADDR = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[19]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div/input"
    XPATH_CONTENTS_ADDR_DETAIL = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[19]/div/div/div[2]/div/div/div[2]/div[2]/div/input"
    XPATH_CONTENTS_PRODUCT = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[22]/div/div/div[2]/div[3]/div/div[2]/div/input"
    XPATH_CONTENTS_TEL = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[22]/div/div/div[2]/div[4]/div/div[2]/div/textarea"
    XPATH_CONTENTS_OPEN = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[22]/div/div/div[2]/div[8]/div/div[2]/div/input"
    XPATH_CONTENTS_CLOSE = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[25]/div/div/div[2]/div[3]/div/div[2]/div/input"
    XPATH_CONTENTS_REFUND_INFO = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[27]/div/div/div[2]/div[3]/div/div[2]/div/textarea"
    XPATH_CONTENTS_LANG_INFO = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[27]/div/div/div[2]/div[4]/div/div[2]/div/input"
    XPATH_CONTENTS_PARKING_LOT = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[27]/div/div/div[2]/div[5]/div/div[2]/div/input"

    XPATH_LANG_SELECT_FIELD = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[15]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div"
    XPATH_LANG_SELECT = '//*[@id="menu-"]/div[3]/ul/li[3]'

    XPATH_CONTENTS_STORAGE_BTN = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[29]/div/div/div[1]/div[2]/button"
    XPATH_CONTENTS_PAYMENT_METHOD_BTN = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[30]/div/div/div[1]/div[2]/button"
    XPATH_CONTENTS_TOILET_BTN = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[33]/div/div/div[1]/div[2]/button"

    XPATH_CONTENTS_PAYMENT_METHOD = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[30]/div/div/div[2]/div[2]/div/div[2]/div/input"
    
    XPATH_CONTENTS_TOILET_INFO = "/html/body/div[2]/div[3]/div[2]/div[5]/div[2]/div/div[3]/div/div/div[2]/div[33]/div/div/div[2]/div[2]/div/div[2]/div/textarea"
    
    XPATH_SAVE_BTN = "/html/body/div[2]/div[3]/div[2]/div[6]/button[2]"
    XPATH_CONFIRM_BTN = ".//button"