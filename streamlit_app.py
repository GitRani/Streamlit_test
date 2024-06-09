# streamlit template test

import streamlit as st

st.title('Streamlit text')

# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('스마일 :sunglasses:')

st.header('헤더')

st.subheader('이것은 subheader 입니다')

st.caption('캡션')

code = '''
def sample_func():
    print("Sample 함수")
'''
st.code(code, language="python")

st.text('')

st.markdown('## 마크다운 ## ** 마크다운 **')
