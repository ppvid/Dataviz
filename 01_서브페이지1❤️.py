import streamlit as st
st.set_page_config(
    page_title='서브페이지',
    page_icon='✨ ',
    layout='centered',
)

st.write('서브페이지')

st.sidebar.title('다양한사이드바')


st.sidebar.checkbox('20대')
st.sidebar.checkbox('30대')