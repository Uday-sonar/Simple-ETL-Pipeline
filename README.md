# Simple-ETL-Pipeline
This project is a simple ETL (Extract, Transform, Load) pipeline implemented using Python. It demonstrates the process of extracting data from a source, transforming it into a suitable format, and loading it into a target destination.


## Features

- Data Extraction : Extracts stock data from Alpha Vantage API.
- Data Transformation : Cleans and transforms the stock data.
- Data Loading : Loads the transformed data into a CSV file.

## Requirements

- Python 3.8 and above
- requests
- pandas


## Usage

1. Modify the `config.json` file to specify the API details and target file path.

2. Run the ETL script:

    ```bash
    python newetl.py
    ```

3. The transformed data will be saved in the `data/target` directory.


## File Structure

```plaintext
simple-etl-pipeline/
│
├── data/
│   ├── source/
│   └── target/
│
├── newetl.py
├── config.json
├── requirements.txt
├── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.


