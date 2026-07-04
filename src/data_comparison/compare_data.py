import pandas as pd
import pandasql as ps
from src.data_connection import*
from src.data_connection.csv_reader import get_csv_data


def compare_df(df1, df2):
    return df1.equals(df2)


# print(compare_df(get_csv_data(r'C:\Users\sridh\PycharmProjects\csvFileValidation\data\source.csv'),
#            get_csv_data(r'C:\Users\sridh\PycharmProjects\csvFileValidation\data\target.csv')))