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
st.text('이제부터 다시 입력하겠습니다._ver2.입니다.')

# ECDF
train_df = pd.read_csv('C:/Users/jeong hee lee/Desktop/심화 프로젝트/train_flattened.csv')

train_df2 = copy(train_df)

train_df2['visitStartTime_UTC'] = pd.to_datetime(train_df2['visitStartTime'], unit='s')

train_df2['visitStartTime_UTC_time'] = train_df2['visitStartTime_UTC'].dt.time

group = train_df2.groupby(['date', 'fullVisitorId'])
result = group.agg({'visitStartTime_UTC_time' : [np.min, np.max]})

result2 = result[result['visitStartTime_UTC_time']['max'] > result['visitStartTime_UTC_time']['min']]
result2.reset_index(inplace=True)

result2['min'] = result2['visitStartTime_UTC_time']['min']
result2['max'] = result2['visitStartTime_UTC_time']['max']
result2['min2'] = result2['min'].apply(lambda x: datetime.strptime(str(x), '%H:%M:%S'))
result2['max2'] = result2['max'].apply(lambda x: datetime.strptime(str(x), '%H:%M:%S'))
result2['max_min_minus'] = result2['max2'] - result2['min2']

result2['max_min_minus'] = result2['max_min_minus'] / pd.Timedelta(1, 'h')

id_max_min_minus_mean = pd.DataFrame(result2.groupby('fullVisitorId')['max_min_minus'].mean())

total_max_min_minus_mean = result2['max_min_minus'].sum() / 47217

ecdf = id_max_min_minus_mean / total_max_min_minus_mean
ecdf.reset_index(inplace=True)

fig, ax = plt.subplots()

displot = sns.displot(data=ecdf, x='max_min_minus', kind='ecdf')
fig = displot.get_figure()

st.pyplot(fig)