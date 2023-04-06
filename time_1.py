import requests
import json
import streamlit as st

url = "https://fiin-core.ssi.com.vn/Master/GetListOrganization?language=vi"

try:
    response = requests.get(url)
    data = json.loads(response.text)
    st.write('good')
except requests.exceptions.JSONDecodeError:
    st.error("Lỗi giải mã dữ liệu JSON")
    data = None
except Exception as e:
    st.error("Đã xảy ra lỗi: " + str(e))
data = None
print(data)