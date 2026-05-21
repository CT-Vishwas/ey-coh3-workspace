import pandas as pd
import matplotlib.pyplot as plt
from src.data_ingestion import read_raw_data
from src.data_cleaning import clean_data
from src.reporting import generate_report

if __name__ == "__main__":
    # read the raw data from the csv file and return a pandas dataframe
    df = read_raw_data('.\data\cap_app_inventory.csv')
    df_compliance = read_raw_data('.\data\cap_compliance_status.csv')

    # clean the data
    df = clean_data(df)
    df_compliance = clean_data(df_compliance)

    # merge the two dataframes on the 'App_ID' column
    df_merged = pd.merge(df, df_compliance, on='App_ID')

    # calculate the percentage of compliant and non-compliant applications
    compliant_percentage = df_merged['Status'].value_counts()

    # generate pie chart to show the percentage of compliant and non-compliant applications
    plt.figure(figsize=(6, 6))
    plt.pie(compliant_percentage, labels=compliant_percentage.index, autopct='%1.1f%%')
    plt.title('Compliance Status of Applications')
    plt.savefig('./output/compliance_status_pie_chart.png')
    # print(df_merged.head())

    # call the function to generate a report in pdf format using the reportlab library
    report_data = {
        'Total Applications': len(df_merged),
        'Compliant Applications': compliant_percentage.get('Compliant', 0),
        'Non-Compliant Applications': compliant_percentage.get('Non-Compliant', 0)
    }
    generate_report(report_data, './output/compliance_report.pdf')
    