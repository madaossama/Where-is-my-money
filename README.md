# Where Is My Money (WIMMY)

## Description
WIMMY is a Python-based application that helps users manage their financial transactions. It allows users to view, filter, and add transactions stored in CSV files. The program is designed to be simple and interactive, making it a great tool for personal finance management.

## Features
- View all transactions
- Filter transactions by category, date, or destination
- Add new transactions to the database

## Requirements
- Python 3.x
- CSV files for categories (`Categories.csv`) and transactions (`Transactions.csv`)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/madaossama/Where-is-my-money.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Where-is-my-money
   ```
3. Ensure you have the required CSV files (`Categories.csv` and `Transactions.csv`) in the project directory.

## Usage
1. Run the program:
   ```bash
   python wimmy.py
   ```
2. Follow the on-screen instructions to view or add transactions.

## Example CSV Files
### Categories.csv
```
name,type
Housing,Expense
Transportation,Expense
Food,Expense
Salary,Income
```

### Transactions.csv
```
date,amount,destination
2025-05-01,1000,Housing
2025-05-02,500,Food
2025-05-03,200,Transportation
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
