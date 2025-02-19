import streamlit as st
import pandas as pd

APP_TITLE = "Relatório de Fraude e Roubo de Identidade"
APP_SUB_TITLE = "Fonte: Comissão Federal de Comércio"

def display_fraud_facts(df, year, quarter, state_name, report_type, field_name, metric_title, number_format='${:,}'):
    df = df[(df['Year'] == year) & (df['Quarter'] == quarter) & (df['Report Type'] == report_type)]
    if state_name:
        df = df[df['State Name'] == state_name]
    df.drop_duplicates(inplace=True)
    total = df[field_name].sum()
    st.metric(metric_title, number_format.format(round(total)))

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)
    
    #LOAD DATA
    df_fraud = pd.read_csv("data/AxS-Fraud Box_Full Data_data.csv")
    df_loss = pd.read_csv("data/AxS-Losses Box_Full Data_data.csv")
    
    year = 2022
    quarter = 1
    state_name = ""
    report_type = "Fraud"
    
    display_fraud_facts(df_fraud, year, quarter, state_name, report_type, 'State Fraud/Other Count', f'# of {report_type} Reports', number_format='{:,}')
    display_fraud_facts(df_loss, year, quarter, state_name, report_type, 'Total Losses', 'Total $  Loss')


    #DISPLAY FILTERS AND MAP
    
    #DISPLAY METRICS

if __name__ == "__main__":
    main()
