import streamlit as st
st.set_page_config(page_title='Pulihora')
st.header("Types of Pulihora")

col1, col2, col3,col4 = st.columns(4)
with col1:
  st.subheader("Nimakai pulihora")
  st.image("./lemon.jpeg", caption="Nimakai Pulihora", width=300,use_column_width=True)
  st.write("Made with Nimakai")
with col2:
  st.subheader("chinthapandu pulihora")
  st.image("./tamarind.jpeg", caption="chinthapandu pulihora", width=300,use_column_width=True)
  st.write("Made with chinthakai")
with col3:
  st.subheader("thiruapathi Pulihora")
  st.image("./thirupathi.jpg", caption="Thiruapathi Pulihora", width=300,use_column_width=True)
  st.write("Made in thirupathi")
with col4:
  st.subheader("Pulihora raja's pulihora ")
  st.image("./krishna.png", caption="Pulihora", width=300, height=400, use_column_width=True)
  st.write("Made by Pulihora")
