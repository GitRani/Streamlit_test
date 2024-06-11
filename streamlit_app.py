# streamlit template test

import streamlit as st
import time

import streamlit as st
import time

# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Placeholder for the counter
placeholder = st.empty()

# Function to update the counter
def update_counter():
    for i in range(st.session_state.counter, 101):
        st.session_state.counter = i
        placeholder.text(f"Counter: {st.session_state.counter}")
        time.sleep(0.1)
        st.experimental_rerun()  # Re-run the script to update the counter

# Check if the counter has reached the end value
if st.session_state.counter < 100:
    update_counter()
else:
    st.write("Counter reached the end value!")

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
