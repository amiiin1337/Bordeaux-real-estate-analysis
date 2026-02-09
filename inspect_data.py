
import pandas as pd
import numpy as np

def inspect_data(file_path):
    with open('inspection_results.txt', 'w', encoding='utf-8') as f:
        import sys
        original_stdout = sys.stdout
        sys.stdout = f
        
        print(f"Inspecting {file_path}...")
        try:
            df = pd.read_csv(file_path, low_memory=False)
        except FileNotFoundError:
            print("File not found.")
            return

        print(f"Shape: {df.shape}")
        print("-" * 30)

        # Missing values
        missing = df.isnull().sum()
        missing_pct = (missing / len(df)) * 100
        print("\nMissing Values (>0%):")
        print(missing_pct[missing_pct > 0].sort_values(ascending=False).map('{:.2f}%'.format))

        # Nature mutation
        print("\nNature Mutation:")
        print(df['nature_mutation'].value_counts())

        # Type local
        print("\nType Local:")
        print(df['type_local'].value_counts(dropna=False))

        # Numerical stats
        numeric_cols = ['valeur_fonciere', 'surface_reelle_bati', 'surface_terrain']
        print("\nNumeric Stats:")
        print(df[numeric_cols].describe())

        # Check for duplicates (id_mutation) purely
        print(f"\nUnique Mutations: {df['id_mutation'].nunique()}")
        
        # Check for potential price outliers (e.g. < 1000 or > 10M)
        if 'valeur_fonciere' in df.columns:
            low_price = df[df['valeur_fonciere'] < 1000]
            high_price = df[df['valeur_fonciere'] > 10000000]
            print(f"\nPrices < 1000: {len(low_price)}")
            print(f"Prices > 10,000,000: {len(high_price)}")
        
        sys.stdout = original_stdout
        print("Inspection complete. Results saved to inspection_results.txt")

if __name__ == "__main__":
    inspect_data('bordeaux_data.csv')
