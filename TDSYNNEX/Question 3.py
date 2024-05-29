import pandas as pd

class DataProcessor:
    def __init__(self, client_list):
        self.df = pd.DataFrame(client_list[1:], columns=client_list[0])

    def remove_rows_by_date(self, date):
        #Its missing
        try:
            self.df = self.df[self.df['Date of billing'] != date]
        except KeyError:
            print(f"Error: 'Date of billing' column not found.")


    def remove_column(self, column_name):
        if column_name in self.df.columns:
            self.df.drop(columns=[column_name], inplace=True)
        else:
            print(f"Column '{column_name}' not found.")

    def create_new_dataframe(self):
        new_df = self.df.groupby('id client')['Amount'].mean().reset_index()
        new_df.columns = ['id_client', 'average_amount']
        return new_df


class Main:
    @staticmethod
    def main():
        clientList = [['id billing', 'id client', 'Date of billing', 'Amount'],
                      [1, 1, 'Thursday 22:00', 123],
                      [2, 2, 'Thursday 10:00', 35],
                      [3, 3, 'Wednesday 15:00', 100],
                      [4, 3, 'Friday 16:00', 456]]

        processor = DataProcessor(clientList)
        print("Original DataFrame:")
        print(processor.df)

        # Remove rows by date
        processor.remove_rows_by_date('Wednesday 15:00')
        print("\nDataFrame after removing rows by date:")
        print(processor.df)

        # Remove column
        processor.remove_column('id billing')
        print("\nDataFrame after removing column 'id billing':")
        print(processor.df)

        # Create new dataframe with id_client and average amounts
        new_df = processor.create_new_dataframe()
        print("\nNew DataFrame with id_client and average amounts:")
        print(new_df)


# Call Main class main function
Main.main()
