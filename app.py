import streamlit as st
from monitor import get_system_data
from visualize import create_dataframe

st.title("AI-Based Cloud Resource Monitoring Dashboard")

system_data = get_system_data()

cpu = system_data["CPU Usage"]
memory = system_data["Memory Usage"]

st.subheader("System Performance")

st.write(f"CPU Usage: {cpu}%")
st.write(f"Memory Usage: {memory}%")

df = create_dataframe(cpu, memory)

st.bar_chart(df.set_index("Resource"))

st.success("Monitoring Completed Successfully")
