import streamlit as st

st.set_page_config(
    page_title='수민이의 streamlit',
    page_icon='❤️',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get help':'https://docs.streamlit.io',
        'Report a bug':'https://streamlit.io',
        'About':'### 김수민 학부생 \n - [홍익대학교 산업 데이터 공학과]'
    }
)

st.title("✨ 수민이의 첫 Streamlit 앱")
st.write("여기에 텍스트, 그래프, 데이터프레임 등을 점점 추가해 나가면 돼요!")
