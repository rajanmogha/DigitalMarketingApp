from optparse import Option
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

def app():
  st.title('Add User Account')

  add_account_form = st.form("add_account_form")
  account_type = add_account_form.selectbox(label="Account Tuype",options=["All","Twitter","Facebook","Youtube"])
  user_name = add_account_form.text_input("Username")
  password = add_account_form.text_input("Password",type="password")
  refrence_name = add_account_form.text_input("Refrence Name")
  client_id = add_account_form.text_input("Client ID")
  app_id = add_account_form.text_input("Twitter App ID")
  add_data = add_account_form.form_submit_button()
  df = pd.read_csv("data/twitter.csv")
  # st.dataframe(df)

  if add_data:
      new_data = {"AccountType":account_type,"Name": user_name,"Password": password,"RefrenceName": refrence_name,"ClientID": client_id,"TwitterID": app_id}
      df = df.append(new_data,ignore_index=True,)
      st.header("User")
      df.to_csv("data/twitter.csv",index=False)
      df = pd.read_csv("data/twitter.csv")
  
  gb = GridOptionsBuilder.from_dataframe(df)
  gb.configure_pagination(enabled=True)
  gb.configure_default_column(editable=True,min_column_width=150)
  gb.configure_column("Password",hide=True)
  gb_option = gb.build()
  ag = AgGrid(df,editable=True,height=250,gridOptions=gb_option)
  
  # df2 = ag['data']
  # print(df2)
  # st.dataframe(df2)
  # st.table(df)