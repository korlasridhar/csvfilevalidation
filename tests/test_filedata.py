import pytest

import pandasql as ps
from src.data_connection.csv_reader import get_csv_data
from src.data_comparison.compare_data import compare_df


def test_filedata():
    source_df = get_csv_data(r'C:\Users\sridh\PycharmProjects\csvFileValidation\data\source.csv')
    target_df = get_csv_data(r'C:\Users\sridh\PycharmProjects\csvFileValidation\data\target.csv')
    result = compare_df(source_df, target_df)
    assert result

def test_filedata1():
    source_df = get_csv_data(r'C:\Users\sridh\PycharmProjects\csvFileValidation\data\source.csv')
    target_df = get_csv_data(r'C:\Users\sridh\PycharmProjects\csvFileValidation\data\target.csv')
    result = compare_df(source_df, target_df)
    assert result

def test_branch1_update():
    print('Conflict Scenario')
    pass