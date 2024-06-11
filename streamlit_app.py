# streamlit template test

import streamlit as st
import time

from streamlit_autorefresh import st_autorefresh

# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Increment the counter
st.session_state.counter += 1

# Display the counter
st.write(f"Counter: {st.session_state.counter}")

# Automatically refresh the page every second
st_autorefresh(interval=1000, key="counter_autorefresh")


# st.title('Streamlit text')

# # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# st.title('스마일 :sunglasses:')

# st.header('헤더')

# st.subheader('이것은 subheader 입니다')

# st.caption('캡션')

# code = '''
# def sample_func():
#     print("Sample 함수")
# '''
# st.code(code, language="python")

# st.text('')

# st.markdown('## 마크다운 ## ** 마크다운 **')

if "count" not in st.session_state:
    st.session_state["count"] = 0

st.write(f"카운터 = {st.session_state['count']}")

button = st.button("누르세요")

if button:
    st.session_state["count"] = st.session_state["count"] + 1
    st.rerun()
