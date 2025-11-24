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

'## : 일반 텍스트'
st.title('제목 : st.title()')

st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.markdown('# 마크다운 : st.markdown()')
st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

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