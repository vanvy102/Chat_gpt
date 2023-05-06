import streamlit as st
import openai
import config
import time
import linear
from streamlit_chat import message
import crawl_link as cr
# Cài đặt thông tin model
api_gpt=st.secrets["api_GPT"]
openai.api_key=api_gpt
#Hàm để gọi đến OpenAPI / Phần ChatGPT
def get_response_from_chatgpt(user_question):
    response = openai.Completion.create(
        engine= config.model,
        prompt = user_question,
        max_tokens = 3000,
        n = 1,
        temperature = 0.5
    )
    response_text = response.choices[0].text
    return response_text
ticket=['...']
with open('MaNH.txt','r') as f:
    h=f.read()
    h=h.splitlines()
    for i in h:
        ticket.append(i)
# #Container1:
with st.container():
   st.markdown("<h1 style='text-align: center; color: grey;'>SMART TRADING GPT</h1>", unsafe_allow_html=True)
   st.markdown('####')
#containcer2:
with st.container():
    string_chat ='chào bạn!'
    #chia container 2 thành 2 cột: 30% - 70%
    column1,column2=st.columns([0.3,0.7]);
    # Hàng 2: Tab và bảng trống
    def clear_session():
        st.session_state.clear()
    with column1:
        # Tạo tab cho các mã chứng khoán:
        selected_stock=st.selectbox("Chọn mã chứng khoán",ticket)
        buuttons=st.button('Xoa',use_container_width=True)
        if selected_stock=='...' or buuttons:
            clear_session()
            st.stop()
        
        with column2:
        #tao ban tom tat
            container1=st.container()
            container2=st.container()
            container3=st.container()
            #du lieu du doan
            ln= linear.linear_data(selected_stock)
            #tao thu vien chat
            if 'bot' not in st.session_state:
                st.session_state['bot']=[]
            if 'user' not in st.session_state:
                st.session_state['user']=[]
            smr='tóm tắt bài viết '
            data=cr.get_link_cafef(selected_stock)
            Y_train=linear.linear_data(selected_stock)
            summary=get_response_from_chatgpt(data[0])
            summary1=get_response_from_chatgpt(data[1])
            summary2=get_response_from_chatgpt(data[2])
            total_sum=get_response_from_chatgpt('Kết hợp ba bài viết trên thành một bài viết tóm tắt')
            container1.write(f"{total_sum}")
            user_question = container3.text_input("Nhập câu hỏi vào đây:")          
            if container3.button("Chat với em đi")or user_question:
                response_text = get_response_from_chatgpt(user_question)
                st.session_state.bot.append(response_text)
                st.session_state.user.append(user_question)
            with container2:
                message('Chào bạn!')
                if st.session_state['user']:
                    for i in range(len(st.session_state['user'])):
                        message(st.session_state["user"][i],is_user=True, key=str(i)+'_user')
                        if i == len(st.session_state['user'])-1:
                            with st.spinner('Đang xử lý...'):
                                time.sleep(1)
                        message(st.session_state['bot'][i], key=str(i))    
     
    
