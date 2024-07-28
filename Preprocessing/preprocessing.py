"""
Pipeline code for preprocessing EEG data
This code preprocesses the EEG(csv) data and converts it to jsonl format at once.
================================================
1. Load the csv file of EEG data
2. Preprocess the loaded data (refer to feature_extraction.py)
3. Convert the preprocessed data to json format (refer to csv_to_json_4o.py)
4. Save the converted data to the specified path
5. Convert the preprocessed json to jsonl format and save it
"""
from csv_to_json_4o import csv_to_json, json_to_jsonl
from feature_extraction import load_eeg_data
import pandas as pd
import numpy as np
import json


def pipeline(csv_path, json_path, jsonl_path, window_size, selected_columns):
    """
    Load the EEG data csv file, convert the preprocessed data to json format, and convert the json to jsonl format and save it.
    :param csv_path:  EEG 데이터의 csv 파일 경로
    :param json_path:  전처리된 데이터를 저장할 json 파일 경로
    :param jsonl_path:  전처리된 데이터를 저장할 jsonl 파일 경로
    :param window_size:  EEG 데이터의 윈도우 사이즈
    :param selected_columns:  사용할 EEG 채널 선택
    """
    # EEG(csv) load
    data, label = load_eeg_data(csv_path)

    # Preprocess the loaded data and convert it to json format
    json_data = csv_to_json(data, window_size, selected_columns, label)

    # Save the converted data to the specified path
    with open(json_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
    print(f"Data has been successfully saved to {json_path}")

    # Convert the preprocessed json to jsonl format and save it
    json_to_jsonl(json_path, jsonl_path)


def main():
    train_csv_path = '/Users/imdohyeon/Documents/PythonWorkspace/EEG-LLM/Dataset/train.csv'
    val_csv_path = '/Users/imdohyeon/Documents/PythonWorkspace/EEG-LLM/Dataset/val.csv'
    test_csv_path = '/Users/imdohyeon/Documents/PythonWorkspace/EEG-LLM/Dataset/test.csv'

    train_json_path = '/Users/imdohyeon/Documents/PythonWorkspace/EEG-LLM/Dataset/json/train.json'
    train_jsonl_path = '/Users/imdohyeon/Documents/PythonWorkspace/EEG-LLM/Dataset/jsonl/train.jsonl'

    val_json_path = '/Users/imdohyeon/Documents/PythonWorkspace/EEG-LLM/Dataset/json/val.json'
    val_jsonl_path = '/Users/imdohyeon/Documents/PythonWorkspace/EEG-LLM/Dataset/jsonl/val.jsonl'

    test_json_path = '/Users/imdohyeon/Documents/PythonWorkspace/EEG-LLM/Dataset/json/test.json'
    test_jsonl_path = '/Users/imdohyeon/Documents/PythonWorkspace/EEG-LLM/Dataset/jsonl/test.jsonl'

    window_size = 1000
    selected_columns = [0, 7, 8, 14, 15, 20, 30, 35, 37, 38, 43, 44, 45, 54, 58]  # 사용할 EEG 채널 선택

    pipeline(train_csv_path, train_json_path, train_jsonl_path, window_size, selected_columns)
    pipeline(val_csv_path, val_json_path, val_jsonl_path, window_size, selected_columns)
    pipeline(test_csv_path, test_json_path, test_jsonl_path, window_size, selected_columns)


if __name__ == '__main__':
    main()