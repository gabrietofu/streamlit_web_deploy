import streamlit as st
view = [100,150,30]
st.write('# NEW NAME')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.DataFrame(view)
sview