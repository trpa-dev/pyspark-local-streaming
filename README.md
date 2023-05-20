# pyspark-local-streaming
PySpark Data Streaming project using a local streaming source.

## About
Data streaming script for Python Spark. Also available in Jupyter Notebook format. Bank transactions
are simulated to have a streaming target for generating credit flow. This is due to the difficulty in
finding data streaming sources as Twitter API is now charging $100 monthly for access.

### Implementation
Python native libraries to generate random transactions and sent to a local socket. Transaction data is
generated in real-time and complies to a certain format. Account ID is a 7-digit number code, Account Region
is distributed over 5 regions and Transfer Value is at least 0.01 credits up to 10000 max. PySpark to
stream the data and perform simple calcs (sum of transactions per region since stream start).

## Getting Started
To get a local copy up and running follow these simple example steps.

### Prerequisites
* PySpark 3.4.0
  * Python 3.7+
  * Spark 3.4.0
  * Java 11.0.19
* Jupyter Notebook (not needed if not using notebooks)

### Installation
* Clone the repo to get the files
* Edit the ports in the scripts as needed
* Add or edit region names and probabilities in the scripts as needed

## Usage
* Run bank_transfer_server_stub.py to start generating data
  * Run bank_transfer_listen_client.py in another terminal to view the messages as is (optional)
  * Run bank_transfer_spark_client.py in another terminal to view Spark Stream output (credit flow)
  * Run 'jupyter notebook' in another terminal and open spark_stream_explore_df_api.ipynb if you prefer a notebook environment

## Roadmap
* Initial MVP - X
* Code Cleanup/Refactoring
* Additional fields for streaming data
* Other types of data streams to simulate (GPS, POS)
  * Faker can be used for more "people" related data sets
* Better data visualization and analysis
  * Better graphing of result data (matplotlib, other graphing libraries)
  * Highest traffic region (by transaction count) (should return as 'North American Trade Zone' due to 40% weight set in distribution)
  * Highest traffic (in volume) region in a given timeframe (in the last X minutes)
  * Top 3 regions in average transaction volumne
* Kafka intermediary between Data Source and Spark
  * Pub/Sub will allow for replication so you could feed data into multiple notebooks(reports)

## License
Licensed under GPL-3.0.

## Contact
