import streamlit as st

if "user" in st.session_state and st.session_state.user:
    st.info(f"{st.session_state.user}님 안녕하세요!")

if "x" not in st.session_state:
    st.session_state.x = 10

if st.button("2배 증가"):
    st.session_state.x *= 2
    

st.write("현재 값:", st.session_state.x)