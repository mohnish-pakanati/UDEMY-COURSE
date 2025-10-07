import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv:str, processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv
    
    def load_and_process(self):
        df = pd.read_csv(self.original_csv, enccoding='utf-8', error_bad_lines=False).dropna() #skips any bad lines, deprecated warning
        required_cols = {'Name', 'Genres', 'synopsis'}

        missing = required_cols - set(df.columns)

        if missing:
            raise ValueError(f"Missing column in CSV File : {missing}")
        df['combined_info'] = ("title: " + df['Name'] + " Overview" + df["synopsis"] + "Genres : " + df['Genres'])
        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv