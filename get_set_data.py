import json
import requests
import urllib.parse
import http.client
import key_cipher as kc
token=kc.token()
shift = 1000
URL_get='http://external.phuocthienpharma.net/v1/get-data'
URL_post='http://external.phuocthienpharma.net/v1/save-data'

# df=cf.get_data_bank('ABB')

# rows=df.loc[0]
# myObj={
#     "bankCode":"ABB",
#     "open": int(rows["Open"]),
#     "high": int(rows["High"]),
#     "low": int(rows["Low"]),
#     "close":int(rows["Close"])
# }
# data=[myObj]
#key

#encrypt data

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# encrypted_text=caesar_cipher(str(data),shift)
# print(encrypted_text) 
#decrypt data
def caesar_decipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result
# decrypted_text=caesar_decipher(encrypted_text,shift)
# print(decrypted_text)
#Lấy dữ liệu
def get_data(ticker,token,shift):
    daa=[]
    session = requests.Session()
    response = session.get('http://external.phuocthienpharma.net/v1/get-data',headers={"source":token})
    data=json.loads(response.text)['data']
    decrypted_text = caesar_decipher(data, shift)
    new_data=json.loads(decrypted_text)
    for i in range(len(new_data)):
        if new_data[i]['bankcode'].upper()==ticker:
            daa.append([int(new_data[i]['high']),int(new_data[i]['low'])])
    return daa
#upload dữ liệu
def set_data(data,token,shift):
    encrypted_text=caesar_cipher(str(data),shift)
    conn = http.client.HTTPConnection("external.phuocthienpharma.net")
    payload = urllib.parse.urlencode({"data": encrypted_text.replace("'","\"")})

    headers = {
            'source': token,
            'Content-Type': 'application/x-www-form-urlencoded'
                }           
    conn.request("POST", "/v1/save-data", payload, headers)
    res = conn.getresponse()
    data = res.read()
# MaNH=cf.get_ticket()
# for mh in MaNH:
#     df=cf.stock_historical_data(mh,'2023-04-01','2023-04-30')
#     k=random.randint(0,len(df)-1)
#     rows=df.loc[k]
#     myObj={
#     "bankCode":mh,
#     "open": int(rows["Open"]),
#     "high": int(rows["High"]),
#     "low": int(rows["Low"]),
#     "close":int(rows["Close"])
#             }
#     data=[myObj]
#     set_data(data,token,shift)

