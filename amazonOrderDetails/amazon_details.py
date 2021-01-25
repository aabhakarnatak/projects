import pandas as pd


class DataProcessing:
    def __init__(self):
        self.df = pd.read_csv('data/amazon_order_history.csv')
        self.df = self.df.fillna(0)

    def calculate_total(self):
        self.df['total'] = self.df['total'].str.replace('Rs. ', ' ')
        self.min_date = min(self.df['date'])
        self.max_date = max(self.df['date'])
        self.sum = self.df['total'].astype(float).sum()

    def print_details(self):
        self.calculate_total()
        print("\nYour Total Expenditure from %s to %s is: Rs. %s" % (self.min_date, self.max_date, self.sum))


DataProcessing().print_details()
