from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl.workbook import Workbook

import datetime
import json
import pandas as pd
import numpy as np
import xlsxwriter

urls = [
        'https://www.moneycontrol.com/stocks/marketstats/hourly_gain/bse/hour_1/index.php',
        'https://www.moneycontrol.com/stocks/marketstats/hourly_gain/bse/hour_2/index.php',
        'https://www.moneycontrol.com/stocks/marketstats/hourly_gain/bse/hour_3/index.php',
        'https://www.moneycontrol.com/stocks/marketstats/hourly_gain/bse/hour_4/index.php',
        'https://www.moneycontrol.com/stocks/marketstats/hourly_gain/bse/hour_5/index.php',
        'https://www.moneycontrol.com/stocks/marketstats/hourly_gain/bse/hour_6/index.php'
    ]


writer = pd.ExcelWriter('hour.xlsx', engine='xlsxwriter')

for count,url in enumerate(urls):
    
    browser = webdriver.Chrome()
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.find_all("table")[1]
    browser.close()

    inc = 0
    head = soup.find("thead")
    body = soup.find("tbody")   

    def bodydata(body):
        data = [[cell.find("a").text if cell.find(["a", ""]) != None else cell.text for cell in row.find_all(["th", "td"])] for row in body.find_all("tr")]
        return data

    def heading(head):
        inc = 0
        rows = head("tr")
        cols = rows[0](["td", "th"])
        table = [None for i in range(0,len(cols)+1)]
        for count, element in enumerate(head.find_all(["th", "td"])):
            insert(table,count,element,inc)
        return table

    def insert(table,count,element, inc):
        if count >= 7 or inc >= 7:
            return
        if element.has_attr("colspan"):
            if table[count] == None:
                span = int(element["colspan"])
                for counter,i in enumerate(range(0, span)):
                    table[count+counter] = "replace"
        elif element.has_attr("rowspan"):
            if table[count] == None:
                table[count] = element.text
            else:
                insert(table, count+1, element, inc)
        else:
            if table[inc] == "replace":
                table[inc] = element.text
            else:
                inc = inc + 1
                insert(table, inc , element, inc)


    head = heading(head)

    body = bodydata(body)
                
    data = [dict(zip(head, i)) for i in body]

    df2 = pd.DataFrame(np.array(body),columns=head)

    df2.to_excel(writer, sheet_name='hr '+ str(count+1), index=False)


writer.save()
