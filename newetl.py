import requests
import pandas as pd
import json
import os

def extract_data(url, headers, querystring):
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data

def transform_data(data):
    # Extract the time series data
    time_series = data.get('Time Series (Daily)', {})
    transformed_data = []
    
    for date, metrics in time_series.items():
        transformed_data.append({
            'date': date,
            'open': float(metrics['1. open']),
            'high': float(metrics['2. high']),
            'low': float(metrics['3. low']),
            'close': float(metrics['4. close']),
            'volume': int(metrics['5. volume'])
        })
    
    df = pd.DataFrame(transformed_data)
    df.sort_values('date', inplace=True)
    return df

def load_data(df, target_path):
    # Create the target directory if it doesn't exist
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    df.to_csv(target_path, index=False)
    print(f"Data loaded successfully to {target_path}")

def main():
    # Load configuration
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    url = config['url']
    headers = config['headers']
    querystring = config['querystring']
    target_path = config['target_path']
    
    # Extract
    data = extract_data(url, headers, querystring)
    
    # Transform
    transformed_data = transform_data(data)
    
    # Load
    load_data(transformed_data, target_path)

if __name__ == "__main__":
    main()
