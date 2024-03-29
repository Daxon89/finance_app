import pandas as pd


def create_new_bill(bill, amount):
    with open('Bills.csv', 'a') as f:
        new_bills = pd.DataFrame({'Bill': [bill], 'Amount': [amount]})
        new_bills.to_csv(f, header=False, index=False, lineterminator='\n')


def get_bills():
    with open('Bills.csv', 'r') as file:
        df = pd.read_csv('Bills.csv')
        return df


def get_headers():
    with open('Bills.csv', 'r') as file:
        df = pd.read_csv('Bills.csv')
        column_list = df.columns.values.tolist()
        return column_list
