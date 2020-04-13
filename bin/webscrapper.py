from bs4 import BeautifulSoup
from selenium import webdriver
import json

#browser = webdriver.Chrome('D:/dataextraction/chromedriver.exe')
#browser.get('https://www.moneycontrol.com/stocks/marketstats/hourly_gain/bse/hour_1/index.php')
#html = browser.page_source
#soup = BeautifulSoup(html, 'html.parser')
#results = soup.find_all("table")[1]
#file1 = open("dad.php","w")
#file1.write(str(results)) 
#file1.close()
#browser.close()

#def table_to_2d(table_tag):
#    rows = table_tag("tr")
#    cols = rows[0](["td", "th"])
#    table = [[None] * len(cols) for _ in range(len(rows))]   
#    for row_i, row in enumerate(rows):
#        for col_i, col in enumerate(row(["td", "th"])):
#            insert(table, row_i, col_i, col)
#    return table


#def insert(table, row, col, element):
#    if row >= len(table) or col >= len(table[row]):
#        return
#    if table[row][col] is None:
#        value = element.get_text()
#        table[row][col] = value
#       if element.has_attr("colspan"):
#            span = int(element["colspan"])
#            for i in range(1, span):
#                table[row][col+i] = value
#        if element.has_attr("rowspan"):
#            span = int(element["rowspan"])
#            for i in range(1, span):
#                table[row+i][col] = value
#    else:
#        insert(table, row, col + 1, element)
#
soup = BeautifulSoup('''
    <table>
    <tr>
        <th class="PR" width="215">
            e<a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/punjabalkalieschemicals/PAC01" style="text-decoration:none;color:#333333">
                Punj Alkalies
            </a>
        </th>
        <th colspan="2">Price at</th>
        <th rowspan="2">Change*</th>
        <th rowspan="2">%Gain*</th>
        <th rowspan="2">Current price</th>
    </tr>
    <tr>
        <td>09:00</td>
        <td>10:00</td>
    </tr>
</table>''', 'html.parser')

#head = table_to_2d(soup.table)
#final_head = head[1]
#resultdata = [dict(zip(table, i)) for i in data]





#for i in soup(["th", "td"]):
#	if i.has_attr("colspan"):
#		print(int(i["colspan"]))
#	if i.has_attr("rowspan"):
#		print(int(i["rowspan"]))




#for count,i in enumerate(soup(["th", "td"])):
#	print(count,i )

"""

for count, row in enumerate(rows):
	if row.has_attr("colspan"):
		span = int(row["colspan"])
		for i in range(0, span):
		       table[count + i] = "replace"
"""


rows = soup("tr")
cols = soup(["th", "td"])

header = []

for i in soup(["th", "td"]):
    a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")





	if i.has_attr("colspan"):
		span = int(i["colspan"])
		for j in range(0,span):
                    header.append("replace")

        else:
            if i.has_attr("rowspan"):
                span = int(i["rowspan"])
                for j in range(0,span):
                    header.append(i.text)
        

