import streamlit as st
import pandas as pd

@st.cache
def read_data(file_name):
    df = pd.read_csv(file_name)
    return df
    
# Streamlit User Interface part
st.set_page_config(page_title="GlobalHRIS", page_icon=":guardsman:", layout="wide")
st.image("logo.png", width=400)
st.title("Global HR Implementation Services Limited \n Employee Data Search")
emp_number = st.text_input("Enter Employee Number")
# Reading the February employee data  

# Read CSV files from List
df = pd.concat(map(pd.read_csv, ['Feb_Data.csv', 'March_Data.csv']))
if emp_number:
    emp_data = df[df['Employee Number'] == int(emp_number)]
    st.write(emp_data)
    
import itertools

d = {}

for fi, f in enumerate(df):
    fh = open(f)
    for line in fh:
        sl = line.split()
        name = sl[0]
        val = int(sl[1])
        if name not in d:
            d[name] = {}
        if fi not in d[name]:
            d[name][fi] = []
        d[name][fi].append(val)
    fh.close()

for name, vals in d.items():
    if len(vals) == len(files):
        for var in itertools.product(*vals.values()):
            if max(var) - min(var) <= 20:
                out = '{}\t{}'.format(name, "\t".join(map(str, var)))
                st.write(out)
                break
   

