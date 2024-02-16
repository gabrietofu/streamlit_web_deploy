import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title(' 이것은 타이틀입니다')
st.title('스마일 :sunglasses:')
st.header('헤더를 입력할 수 있어요! :sparkles:')
st.caption('캡션을 한 번 넣어봤습니다.')

sample_code = '''
def function():
    print('hello, world')
'''
st.code(sample_code, language='python')

st.text('일반적인 텍스트를 입력해보았습니다.')
st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
st.markdown('텍스트의 색상을 :green[초록색]으로, 그리고 **:red[빨간색]** 볼드체로 설정할 수 있습니다. ')
st.markdown(":green[$\sqrt{x^2+y^w}=1$]")