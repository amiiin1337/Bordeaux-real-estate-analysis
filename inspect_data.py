
import pandas as pd
import numpy as np

def inspect_data(file_path):
    with open('inspection_results.txt', 'w', encoding='utf-8') as f:
        import sys
        original_stdout = sys.stdout
        sys.stdout = f
        
        print(f"inspecting {file_path}...")
        try:
            df = pd.read_csv(file_path, low_memory=False)
        except FileNotFoundError:
            print("File not found.")
            return

        print(f"shape: {df.shape}")
        print("-" * 30)

        # missing values
        missing = df.isnull().sum()
        missing_pct = (missing / len(df)) * 100
        print("\nmissing values (>0%):")
        print(missing_pct[missing_pct > 0].sort_values(ascending=False).map('{:.2f}%'.format))

        # nature mutation
        print("\nnature mutation:")
        print(df['nature_mutation'].value_counts())

        # type local
        print("\ntype local:")
        print(df['type_local'].value_counts(dropna=False))

        # numerical stats
        numeric_cols = ['valeur_fonciere', 'surface_reelle_bati', 'surface_terrain']
        print("\nnumeric stats:")
        print(df[numeric_cols].describe())

        # check for duplicates (id_mutation) purely
        print(f"\nunique mutations: {df['id_mutation'].nunique()}")
        
        # check for potential price outliers (e.g. < 1000 or > 10M)
        if 'valeur_fonciere' in df.columns:
            low_price = df[df['valeur_fonciere'] < 1000]
            high_price = df[df['valeur_fonciere'] > 10000000]
            print(f"\nprices < 1000: {len(low_price)}")
            print(f"prices > 10,000,000: {len(high_price)}")
        
        sys.stdout = original_stdout
        print("inspection complete. results saved to inspection_results.txt")

if __name__ == "__main__":
    inspect_data('bordeaux_data.csv')
