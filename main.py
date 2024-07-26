import streamlit as st
st.title('나의 퀸네임은?')
name-st.text_input('지금 입고 있는 옷 색 : ')
menu = st. selectbox('지금 먹고 싶은 음식:', ['마라탕', '꿔바로우', '포케', '반미' ])
if. st.button('퀸네임 생성') :
  st.write(name+menu)
