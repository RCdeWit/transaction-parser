import argparse
import polars as pol

def read_transaction_file(file_path: str) -> pol.DataFrame:
    with open(file_path) as transaction_file:
        return pol.read_csv(transaction_file)
    
def parse_transaction_file(transactions: pol.DataFrame, bank: str) -> pol.DataFrame:
    schema = ["date", "name", "category", "tags", "amount"]
    return

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--bank', dest='bank', required=True)
    args_parser.add_argument('--file', dest='file', required=True)
    args = args_parser.parse_args()

    transactions = read_transaction_file(args.file)