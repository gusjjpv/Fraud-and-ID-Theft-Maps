import streamlit as st
import pandas as pd

APP_TITLE = "Relatório de Fraude e Roubo de Identidade"
APP_SUB_TITLE = "Fonte: Comissão Federal de Comércio"

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)
    
    #LOAD DATA
    df = pd.read_csv("data/AxS-Fraud Box_Full Data_data.csv")
    
    year = 2022
    quarter = 1
    state_name = "Texas"
    report_type = "Other"
    field_name = 'State Fraud/Other Count'
    metric_title = f'# of {report_type} Reports'
    
    df = df[(df['Year'] == year) & (df['Quarter'] == quarter) & (df['Report Type'] == report_type)]
    if state_name:
        df = df[df['State Name'] == state_name]
    df.drop_duplicates(inplace=True)
    total = df[field_name].sum()
    st.metric(metric_title, '{:,}'.format(total))
    
    st.write(df.shape)
    st.write(df.head())
    st.write(df.columns)
    
    #DISPLAY FILTERS AND MAP
    
    #DISPLAY METRICS

if __name__ == "__main__":
    main()
