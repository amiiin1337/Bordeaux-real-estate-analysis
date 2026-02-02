"""
Bordeaux Real Estate Analysis - Sprint 1
Data Loading and Initial Exploration
"""

import pandas as pd

def load_and_filter_data(input_file='33.csv', output_file='bordeaux_data.csv'):
    """
    Load DVF dataset and filter for Bordeaux city
    
    Args:
        input_file: Path to raw DVF CSV file
        output_file: Path to save filtered dataset
    """
    
    # Load data
    print("Loading data...")
    print(f"Source file: {input_file}")
    
    try:
        df = pd.read_csv(input_file, low_memory=False)
        print(f"Loaded successfully: {len(df):,} rows, {len(df.columns)} columns")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        print("Download from: https://files.data.gouv.fr/geo-dvf/latest/csv/")
        return
    
    # Display available columns
    print("\nAvailable columns:")
    for i, col in enumerate(df.columns, 1):
        print(f"   {i:2d}. {col}")
    
    # Filter for Bordeaux
    print(f"\nFiltering for Bordeaux...")
    
    if 'code_commune' in df.columns:
        # Convert to string for reliable comparison
        df['code_commune'] = df['code_commune'].astype(str)
        df_bordeaux = df[df['code_commune'] == '33063']
        print(f"Found {len(df_bordeaux):,} sales in Bordeaux")
        
    elif 'nom_commune' in df.columns:
        df_bordeaux = df[df['nom_commune'].str.upper() == 'BORDEAUX']
        print(f"Found {len(df_bordeaux):,} sales in Bordeaux")
        
    else:
        print("Error: Cannot find commune column")
        return
    
    if len(df_bordeaux) == 0:
        print("Warning: No data found for Bordeaux")
        return
    
    # Display preview
    print("\nFirst 5 rows:")
    print(df_bordeaux.head())
    
    # Basic statistics
    print("\nQuick statistics:")
    
    if 'valeur_fonciere' in df_bordeaux.columns:
        values = df_bordeaux['valeur_fonciere'].dropna()
        if len(values) > 0:
            print(f"\nPrices:")
            print(f"   Mean: {values.mean():,.0f} EUR")
            print(f"   Median: {values.median():,.0f} EUR")
            print(f"   Min: {values.min():,.0f} EUR")
            print(f"   Max: {values.max():,.0f} EUR")
    
    if 'type_local' in df_bordeaux.columns:
        print(f"\nProperty types:")
        types = df_bordeaux['type_local'].value_counts()
        for property_type, count in types.items():
            print(f"   {property_type}: {count:,}")
    
    if 'nature_mutation' in df_bordeaux.columns:
        print(f"\nTransaction types:")
        natures = df_bordeaux['nature_mutation'].value_counts()
        for nature, count in natures.head(5).items():
            print(f"   {nature}: {count:,}")
    
    if 'date_mutation' in df_bordeaux.columns:
        df_bordeaux_copy = df_bordeaux.copy()
        df_bordeaux_copy['year'] = pd.to_datetime(df_bordeaux_copy['date_mutation']).dt.year
        print(f"\nYears:")
        years = df_bordeaux_copy['year'].value_counts().sort_index()
        for year, count in years.items():
            print(f"   {int(year)}: {count:,}")
    
    # Save filtered data
    print(f"\nSaving filtered data to: {output_file}")
    df_bordeaux.to_csv(output_file, index=False)
    print(f"Saved: {len(df_bordeaux):,} rows")
    print(f"\nSuccess! You can now work with '{output_file}'")

if __name__ == "__main__":
    print("=" * 60)
    print("   BORDEAUX REAL ESTATE ANALYSIS - SPRINT 1")
    print("=" * 60)
    print()
    
    load_and_filter_data()