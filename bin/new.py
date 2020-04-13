from bs4 import BeautifulSoup

soup = BeautifulSoup('''
    <table>
        <tr>
            <th rowspan="2" align="left" valign="top" class="TAL" width="215">Company Name</th>
            <th colspan="2" width="260">Price at</th>
            <th rowspan="2" valign="top" width="140">Change*</th>
            <th rowspan="2" valign="top" width="140">%Gain*</th>
            <th rowspan="2" valign="top" width="140">Current price</th>
        </tr>
        <tr>
            <th align="center" style="text-align:center;">10:00</th>
            <th align="center" style="text-align:center;">10:24</th>
        </tr>
    </table>''', 'html.parser')

header = []

for element in soup(["th","td"]):
    if element.has_attr("colspan"):
        span = int(element["colspan"])
        for j in range(0,span):
            header.append("replace")  
    elif element.has_attr("rowspan"):
        header.append(element.text)
    else:
        for count,update in enumerate(soup(["th","td"])):
            if count >= 5:
                break
            if header[count] == "replace":
                header[count] = element.text
            
print(header)
