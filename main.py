import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('Display Image')

text = st.text_input(
    'あなたが好きな数字を教えてください'
)
'あなたの好きな数字は', text , 'です。'

condition = st.slider('あなたの今の調子は',0,100,50)
'コンディション', condition

# if st.checkbox('Show Image'):
#     img = Image.open('lena_std.bmp')
#     st.image(img, caption='Sample', use_column_width=True)
