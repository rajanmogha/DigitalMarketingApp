import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

def app():
    st.title('Post Message')
    df = pd.read_csv("data/twitter.csv")
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(enabled=True)
    gb.configure_default_column(editable=False)
    gb.configure_selection(selection_mode="multiple",use_checkbox=True)
    gb.configure_column("AccountType",headerCheckboxSelection=True )
    gb.configure_column("Password",hide=True)
    gb_option = gb.build()
    ag = AgGrid(df,height=250,gridOptions=gb_option,update_mode= GridUpdateMode.SELECTION_CHANGED)

    post_form = st.form("add_account_form")
    message = post_form.text_area("Message")
    is_ip_change = post_form.checkbox(label="Is IP Change", value=False)
    time_interval = post_form.text_input(label="Time Interval")
    add_data = post_form.form_submit_button()

    if add_data:
        sel_row = ag['selected_rows']
        st.write(len(sel_row))
        # st.write(sel_row)
        if len(sel_row) == 0:
            # st.write('Please select atleast one user')
            st.warning("Please select atleast one user")
        else:
            for i in sel_row:
                st.write(i)
                st.write(i["Name"])
                st.write(i["Password"])

