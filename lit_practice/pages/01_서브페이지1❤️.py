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



st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.markdown('# 마크다운 : st.markdown()')


#st.write() : 텍스트, Markdown, 데이터, Matplotlib 수치, Altair 차트 등 거의 모든 것을 출력하는 함수

'### st.write()'
st.write('# 마크다운 H1 : st.write()')
st.write('## 마크다운 H3 : st.write()')
st.write('') # 빈 줄 추가

'### 색상이 있는 텍스트'
st.write('1. :red[빨간색 텍스트]')
st.write('- :blue[파란색 텍스트!]')

'### 코드 블록: st.code()'
st.code('print("Hello, World!")', language='python', line_numbers=True)

'### 코드+결과: st.echo()'
with st.echo():
    # 이 블록의 코드와 결과를 출력
    name = 'sumin Kim'
    st.write("Hello, Streamlit!", name)

'### Latex 수식 작성: st.latex()' #레이텍스, 수학기호
st.latex(r'\int_a^b f(x)dx')
st.latex(r'\int_0^\infty \frac{1}{x^2}dx=[\frac{-1}{x}]_0^\infty')
"### 구분선 st.divider()"
with st.echo():
    st.divider()
'''
### 마크다운 링크
- [네이버](https://www.naver.com)

### 마크다운 인용
> 인용문: '스트림릿은 정말 재미있어요!'

### 마크다운 표
| 이름   | 나이 | 전공           |
| ------ | ---- | -------------- |
| 김수민 | 22   | 산업 데이터 공학과 |

### 마크다운 코드 블록
```python
def hello_world():
    print("Hello, World!")
```
'''

'# : 미디어 삽입'

st.audio(
    r"C:\Users\paint\OneDrive\Desktop\Githubproject\Dataviz\데이터 시각화\data\FunkyGiraffe.mp3",
    format="audio/mpeg",
    loop=True
)

#고급기능
#캐싱, st.session_state
#캐싱> 데코레이터 @st.cache_data, @st.cache_resource 사용
#값 안에 데이터들이 다 들어있는 것: 직렬화
# 직렬화는 데이터 전송 시에 나오는 개념
#json, xml이 대표적 직렬화 포맷, dtype도 가능/ csv는 dtype지정 불가, 2차원 데이터만 가능

'# : Streamlit Magic'

'''
### 마크다운 헤더 3
- 마크다운 목록1. **굵게**표시
- 마크다운 목록2. *기울임*표시
    - 마크다운 목록2-1
    - 마크다운 목록 2-2
### 마크다운 링크
- [네이버](https://naver.com)
- [구글](https://google.com)
'''

'# 콜아웃'
st.info('This is a purely information message')
st.warning('warning massage')
st.error('error')
st.success('success')

'### :orange[Pandas Dataframe]'
import pandas as pd
df=pd.DataFrame(
    {'id':[1,2,3],
     'name':['Alice','Bob','Charlie'],
     'age':[24,34,45]}
)
df

'### :orange[지표(Metric)]'
col1,col2,col3=st.columns(3)
col1.metric('Temperature','70','1.2')
col2.metric('wind','9mph','-8%')
col3.metric('humidity','86','4')

import numpy as np

chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.area_chart(chart_data)
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.scatter_chart(chart_data)

df=pd.DataFrame(
    np.random.randn(100,2)/[100,100]+[37.55,126.92],
    columns=['lat','lon']
)
st.map(df)

import matplotlib.pyplot as plt

x=np.linspace(0,10,100)
y=np.sin(x)
fig,ax=plt.subplots()
ax.plot(x,y)
st.pyplot(fig)
st.divider()




'### :orange[컬럼: st.columns()]'
col_1,col_2,col_3=st.columns([1,2,1]) #1:2:1 비율로 컬럼을 나눔

with col_1:
    st.write('## 1번컬럼')
    st.checkbox('체크박스1')
    st.checkbox('체크박스2')
with col_2:
    st.write('## 2번컬럼')
    st.radio('라디오버튼',['radio1','radio2','radio3'])
col_3.write('## 3번컬럼')
col_3.selectbox('셀렉트박스',['select1','select2','select3'])

'### 탭'
tab1,tab2,tab3=st.tabs(['Python','R','Julia'])
with tab1:
    st.write(
        '''
        ```python
        import pandas as pd
        ```
        '''
    )

with tab2:
    st.write(
        '''
    ```r
    df<-data.frame(
    )
    ```
    '''
    )
tab3.write(
    '''
    ```julia
    using DataFrames
    ```
    '''
)

'### :orange[확장레이아웃]'
with st.expander('확장레이아웃'):
    st.write('이곳은 확장레이아웃입니다')
    st.write('확장 레이아웃은 특정 컨텐츠를 숨기거나 보여줄 때 사용됩니다')

'### :orange[피드백 버튼: st.feedback()]'
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"당신은 {sentiment_mapping[selected]} star(s)을 선택하였습니다.")

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"당신은 {sentiment_mapping[selected]}을 선택하였습니다.")

'### :orange[링크 버튼: st.link_button()]'
st.link_button("Golden(K팝 데몬 헌터스) 뮤직비디오", "https://youtu.be/UkFLk0-xf58?si=tXNAsriFnI4r6ron")


df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.write('### :orange[session_state를 사용하지 않은 경우]')
color1 = st.color_picker("Color1", "#FF0000")
st.divider()  # 구분선
st.scatter_chart(df, x="x", y="y", color=color1)

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.write('### :orange[session_state를 사용한 경우]')
color2 = st.color_picker("Color2", "#FF0000")
st.divider()  # 구분선
st.scatter_chart(st.session_state.df, x="x", y="y", color=color2)
st.write('📌 :green[session_state를 사용하면, 저장된 state를 사용하므로 값이 고정됨]')