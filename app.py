import streamlit as st
from multiapp import MultiApp
from apps import add_user,post

app = MultiApp()

# st.markdown("""
# Welcome to Advertisement by social media backend panel ....""")

# Add all application

app.add_app("Add User", add_user.app)
app.add_app("Post", post.app)
# The main app
app.run()