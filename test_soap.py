import requests
url="https://web.cbr.ru/GetCursOnDate/DailyInfoWebServ/DailyInfo.asmx"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetCursOnDate xmlns="http://web.cbr.ru/">
      <On_date>dateTime</On_date>
    </GetCursOnDate>
  </soap:Body>
</soap:Envelope>"""

response = requests.post(url,data=body,headers=headers)
print(response.content)