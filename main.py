import pytest
from src.data_connection import *
from src.data_connection.csv_reader import get_csv_data
from src.data_comparison.compare_data import compare_df
import pandas as pd
import duckdb


source_df = get_csv_data('data/source.csv')
target_df = get_csv_data('data/target.csv')

