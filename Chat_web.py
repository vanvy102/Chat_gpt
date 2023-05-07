import streamlit as st
import openai
import config
import datetime
import linear
import time
from streamlit_chat import message
import crawl_link as cr
# Cài đặt thông tin model
api_gpt=st.secrets["api_GPT"]
token=st.secrets["token"]
shift=st.secrets["shift"]
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
tk=config.get_ticket()
for i in tk:
    ticket.append(i)
# #Container1:
with st.container():
   st.markdown("<h1 style='text-align: center; color: grey;'>SMART TRADING GPT</h1>", unsafe_allow_html=True)
   st.markdown('####')
#containcer2:
with st.container():
    string_chat ='chào bạn!'
    #chia container 2 thành 2 cột: 30% - 70%
    column1,column2=st.columns([0.3,0.7])
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
        Y_train=linear.linear_data(selected_stock,token,shift)

        # questions=[f'với những thông tin và giá mở phiên {int(Y_train[0])} thì mã cổ phiếu này có ưu thế gì?']
        # selected_question=st.selectbox('câu hỏi:',questions)
        # print(selected_question)
        # if 'bot' not in st.session_state:
        #     st.session_state['bot']=[]
        # if 'user' not in st.session_state:
        #     st.session_state['user']=[]
        # response_text=get_response_from_chatgpt(selected_question)
        # st.session_state.bot.append(response_text)
        # st.session_state.user.append(selected_question)
    with column2:
        #tao ban tom tat
        container1=st.container()
        container2=st.container()
        container3=st.container()
        if 'bot' not in st.session_state:
            st.session_state['bot']=[]
        if 'user' not in st.session_state:
            st.session_state['user']=[]
        with container3:
            q1="với những thông tin đó thì mã ngân hàng "+selected_stock+" và giá của mã này là "+str(Y_train[0])+" có những rủi ro về mặt đầu tư nào?"
            q2='dựa vào những thông tin gì về thị trường, nhà nước, lĩnh vực liên quan đến ngân hàng '+ selected_stock+ ' để bạn có thể đưa ra các rủi ro như vậy?'
            q3="với những thông tin và giá mở phiên "+ str(Y_train[0]) +" thì mã cổ phiếu "+ selected_stock+" có ưu thế gì?"
            q4= "dựa vào những thông tin nào của nhà nước, thị trường và mã ngân hàng "+selected_stock+" để bạn có thể đưa ra được những ưu thế như vậy?"
            q5="Mã ngân hàng "+selected_stock+" có những chính sách tích cực, khả quan trong năm 2023 để giúp cho tình hình tài chính của ngân hàng phát triển tốt hơn không?"
            q6="Trong ba tháng gần nhất trong năm 2023 ở Việt Nam, ngân hàng "+selected_stock+" có những thông tin tiêu cực nào không ?"
            selected_question=st.selectbox('câu hỏi:',(q1,q2,q3,q4,q5,q6))
            print(selected_question)
            #du lieu du doan
            #tao thu vien chat
        # if 'bot' not in st.session_state:
        #     st.session_state['bot']=[]
        # if 'user' not in st.session_state:
        #     st.session_state['user']=[]
            current_time= datetime.date.today()
            current_year=current_time.year
            smr='tóm tắt bài viết, dữ liệu cho năm '+ str(current_year)
            data=cr.get_link_cafef(selected_stock)
            for i in range(len(data)):
                data[i]=smr +' '+data[i]
            print(data)
            summary=get_response_from_chatgpt(data[0])
            print(summary)
            summary1=get_response_from_chatgpt(data[1])
            print(summary1)
            summary2=get_response_from_chatgpt(data[2])
            print(summary2)
            total_sum=summary+'\n'+summary1+'\n'+summary2
        #total_sum=get_response_from_chatgpt('Kết hợp ba bài viết trên thành một bài viết')
            container1.write(f"{total_sum}")
        
            # st.session_state.bot.append(response_text)
            # st.session_state.user.append(user_question)
        
            response_text=get_response_from_chatgpt(selected_question)
            st.session_state.bot.append(response_text)
            st.session_state.user.append(selected_question)
            with container2:
                if st.session_state['user']:
                    for i in range(len(st.session_state['user'])):
                        message(st.session_state["user"][i],is_user=True, key=str(i)+'_user')
                        if i == len(st.session_state['user'])-1:
                            with st.spinner('Đang xử lý...'):
                                time.sleep(1)
                        message(st.session_state['bot'][i], key=str(i))    
     
    
