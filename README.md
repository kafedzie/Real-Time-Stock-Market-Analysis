# Real Time Stock Market Analysis

### Project Description

A lightweight stock market analysis producer that captures real-time intraday stock data from a configurable API, extracts the relevant pricing fields, and prepares the results for downstream streaming, monitoring, or analytics pipelines. The project is organized around a modular producer package with separate configuration, extraction, and execution logic.

This repository includes:

- `producer/config.py` for API connection settings and logging setup
- `producer/extract.py` for fetching and parsing stock market data
- `producer/main.py` as the entrypoint that runs the producer and prints extracted records

### How to Install and Run the Project

1. Install Python 3.10+.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install requests python-dotenv
   ```
4. Create a `.env` file at the repository root and add your API key:
   ```bash
   API_KEY=your_alpha_vantage_api_key
   ```
5. Run the producer:
   ```bash
   python producer/main.py
   ```

### How to Use the Project

1. Update `producer/config.py` if you need to change the API host, headers, or logging behavior.
2. Modify the stock symbols list in `producer/extract.py` to analyze different instruments.
3. Adjust the query parameters in `connect_to_api()` for a different interval or output size.
4. Run `python producer/main.py` to fetch market data, extract records, and print them to the console.
5. Extend the project by replacing the console output in `producer/main.py` with a streaming sink, database writer, or analytics consumer.
