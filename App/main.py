import os
import time
import selenium

from web import Web
from data import Data

if __name__ == "__main__":
    
    PATH = input("XLSX File Path : ")
    SHEET_NAME = input("XLSX File Sheet Name : ")

    data = Data(path=PATH, sheet_name=SHEET_NAME)
    Browser = Web()

    LOGIN_ID = input("ID : ")
    LOGIN_PW = input("PW : ")

    Browser.Login(id=LOGIN_ID, pw=LOGIN_PW)

    begin_index = int(input("Input Start ROW index : "))
    end_index = int(input("Input Start ROW index : "))

    for idx in range(begin_index, end_index+1):
        origin_data = data.GetOriginalData(row=idx)
        translated_data = data.GetTranslatedData(row=idx)

        print(f"=== Working On Index : {idx}, Name : {origin_data['name']} ===")

        hasContentsFounded = Browser.SearchContents(name=origin_data['name'], addr=origin_data['addr'])

        if hasContentsFounded:
            Browser.AccessEditPage()

        Browser.ReplaceTranslatedData(translated_data=translated_data)

        Browser.Save()
        Browser.ClearSearchContents()

        print("")