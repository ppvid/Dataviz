import streamlit as st

st.set_page_config(
    page_title='K팝 데몬 헌터스 온라인 데이터 분석',
    page_icon='✨',
    layout='wide',
    initial_sidebar_state='collapsed',
    menu_items={
        'Get help':'https://docs.streamlit.io',
        'Report a bug':'https://streamlit.io',
        'About':'### 김수민 학부생 \n - [홍익대학교 산업 데이터 공학과]'
    }
)

st.title("✨K팝 데몬 헌터스 온라인 데이터 분석 보고서")
st.caption('C221011 김수민')
'### 1. 뉴스 본문 키워드 빈도 시각화-Seaborn,Altair,Plotly 활용'
st.caption('출처: 네이버 뉴스')
tab1,tab2,tab3=st.tabs(['Seabron','Altair','Plotly'])
with tab1:
    st.caption('seaborn으로 그래프 그리기')
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    df=pd.read_csv(r'C:\Users\paint\OneDrive\Desktop\Githubproject\Dataviz\데이터 시각화\키워드카운트.csv')
    plt.rcParams["font.family"] = "Malgun Gothic"
    fig,ax= plt.subplots(figsize=(6,4))
    sns.barplot(data=df,y='keyword',x='count')
    ax.set_title('K팝 데몬 헌터스 뉴스 키워드 상위 20개')
    ax.set_xlabel('Count')
    ax.set_ylabel('Keyword')
    plt.tight_layout()
    st.pyplot(fig)
with tab2:
    st.caption('altair로 그래프 그리기, tooltip 적용')
    import altair as alt

    c = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X('count:Q', title='Count'),
            y=alt.Y('keyword:N', title='Keyword',
                    sort=alt.SortField(field='count', order='descending')),
            tooltip=['keyword:N', 'count:Q']
        ).properties(
        title="K팝 데몬 헌터스 뉴스 키워드 상위 20개"
    )
    )
    st.altair_chart(c, use_container_width=True)

with tab3:
    st.caption('plotly로 그래프 그리기, 인터랙티브 시각화')
    import plotly.express as px
    fig=px.bar(df.sort_values('count',ascending=True),
            x='count',
            y='keyword',
            orientation='h',
            hover_data={'keyword':True,"count":True},
            title="K팝 데몬 헌터스 뉴스 키워드 상위 20개",
            height=800
    )
    st.plotly_chart(fig,use_container_width=True)

'## 2. 뉴스 제목 키워드 워드 클라우드'
st.caption('출처: 네이버 뉴스')
st.image(r'C:\Users\paint\OneDrive\Desktop\Githubproject\Dataviz\데이터 시각화\워드클라우드.png',use_container_width=True)
'글로벌, 3개 부분, 마마 어워즈 및 여러 걸그룹이 언급되는 걸 보아 최근에 글로벌 시상식인 마마 어워즈에 나가 수상을 한 것이 이슈가 되었다. 또한 강감독과 매기강 등의 언급을 보면 케데헌의 감독의 역할이 주목받고 있음을 알 수 있다.'

'## 3. 뉴스 본문 키워드 네트워크 시각화'
st.caption('출처: 네이버 뉴스')
'### 네트워크 시각화'
st.image(r'C:\Users\paint\OneDrive\Desktop\Githubproject\Dataviz\데이터 시각화\네트워크그래프.png',use_container_width=True)
'### circular 네트워크 시각화'
st.image(r'C:\Users\paint\OneDrive\Desktop\Githubproject\Dataviz\데이터 시각화\circulara_네트워크.png',use_container_width=True)
'뉴스 내용에는 케이팝 데몬 헌터스의 설명인 넷플릭스 애니메이션 콘텐츠를 언급하고 있다. 골든, 차트, 트랙 사운드 등의 키워드를 보아 해당 영화의 ost가 많은 주목을 받고 있음을 알 수 있다.'
st.divider()
'## 추가 정보 및 게임'
st.caption('확장 컨테이너 사용')
with st.expander('K팝 데몬 헌터스의 대표 OST'):
    st.caption('버튼 누를 시 뮤직비디오 링크로 이동')
    st.link_button("Golden(K팝 데몬 헌터스) 뮤직비디오", "https://youtu.be/UkFLk0-xf58?si=tXNAsriFnI4r6ron")
with st.expander('K팝 데몬 헌터스 퀴즈'):
    st.caption('틀릴 시 fail 콜아웃, 정답 시 success, 풍선 애니매이션 효과')
    st.write('다음 중 K팝 데몬 헌터스의 멤버가 아닌 것은?')

    choice = st.radio('정답을 선택하세요', ['루미','미라','애니','조이'], index=None)

    if choice is not None:
        if choice == '애니':
            st.success('success')
            st.balloons()
        else:
            st.error('fail')


