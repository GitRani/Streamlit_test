# streamlit template test

import streamlit as st
import time

# Initialize session state
if 'slider_value' not in st.session_state:
    st.session_state.slider_value = 0

# Placeholder for the slider
slider_placeholder = st.empty()

# Function to render the slider
def render_slider():
    slider_placeholder.slider('Move the slider', 0, 100, st.session_state.slider_value, key='slider')

# Initial render of the slider
render_slider()

# Function to automate the slider movement
def move_slider():
    for i in range(st.session_state.slider_value, 101):
        st.session_state.slider_value = i
        render_slider()
        time.sleep(0.1)
        st.experimental_rerun()  # Re-run the script to update the slider

# Check if the slider has reached the end value
if st.session_state.slider_value < 100:
    move_slider()
else:
    st.write("Slider reached the end value!")

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
