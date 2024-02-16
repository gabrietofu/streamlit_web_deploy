import streamlit as st
view = [100,150,30]
st.write('# Changed View_version2')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.DataFrame(view)
sview