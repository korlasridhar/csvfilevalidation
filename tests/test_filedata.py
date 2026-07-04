import pytest

from  pandasql import sqldf
from src.data_connection.csv_reader import get_csv_data
from src.data_comparison.compare_data import compare_df

source_df = get_csv_data(r'C:\Users\sridh\PycharmProjects\csvFileValidation\data\source.csv')
target_df = get_csv_data(r'C:\Users\sridh\PycharmProjects\csvFileValidation\data\target.csv')

def test_filedata():
    result = compare_df(source_df, target_df)
    assert result

def test_filedata1():
    result = sqldf("select age from source_df where age < 30")
    assert result['age'].iloc[0] ==20

def test_filedata2():
    result = sqldf("select age from source_df where age < 100")
    assert len(result) == 3
