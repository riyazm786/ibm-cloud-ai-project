import streamlit as st
import psutil
import pandas as pd
import time

st.title("AI-Based Cloud Resource Monitoring Dashboard")

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent

st.subheader("System Performance")

st.write(f"CPU Usage: {cpu}%")
st.write(f"Memory Usage: {memory}%")

data = {
    "Resource": ["CPU", "Memory"],
    "Usage": [cpu, memory]
}

df = pd.DataFrame(data)

st.bar_chart(df.set_index("Resource"))
