import streamlit as st
st.set_page_config(page_title='Pulihora')
st.header("Types of Pulihora")

col1, col2, col3,col4 = st.columns(4)
with col1:
  st.subheader("Nimakai pulihora")
  st.image("./lemon.jpg", caption="Persian Cat", width=300,use_column_width=True)
  st.write("Made with Nimakai")
with col2:
  st.subheader("chinthapandu pulihora")
  st.image("./tamarind.jpg", caption="Ragdoll Cat", width=300,use_column_width=True)
  st.write("Made with chinthakai")
  with col3:
  st.subheader("thiruapathi Pulihora")
  st.image("./thirupathi.jpg", caption="Persian Cat", width=300,use_column_width=True)
  st.write("Made in thirupathi")
with col4:
  st.subheader("krishna Pulihora ")
  st.image("./krishna.jpg", caption="Ragdoll Cat", width=300,use_column_width=True)
  st.write("Made by Pulihora")
