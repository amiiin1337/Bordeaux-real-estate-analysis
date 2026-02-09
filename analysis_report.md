
# 📊 Bordeaux Real Estate Data Analysis Report

## 1. Dataset Overview
- **Total Rows**: 11,660
- **Unique Transactions (Mutations)**: 5,445
- **Year**: 2024
- **Location**: Bordeaux (33063)

> [!NOTE]
> There are significantly more rows than unique transactions. This is because a single sale (mutation) often contains multiple rows (one for each "lot", e.g., Apartment + Parking + Cellar).

## 2. Data Structure & Quality

### ❗ Critical Observation: Multi-Row Transactions
The column `valeur_fonciere` (Property Value) is **repeated** on every row of a transaction.
- **Example**: If an apartment is sold for €300,000 with a garage, there will be 2 rows, both showing €300,000.
- **Implication**: simply summing or averaging `valeur_fonciere` column directly will lead to **massive double-counting**. You must aggregate by `id_mutation` first.

### Missing Values
| Column | Missing % | Impact |
|--------|-----------|--------|
| `valeur_fonciere` | 0.17% | Very Low (Excellent) |
| `type_local` | 18.20% | Moderate. Rows with NaN are often land or mixed components. |
| `surface_reelle_bati` | 55.66% | High. Expected for "Dépendance" or land-only sales, but requires careful filtering for price/m² analysis. |
| `surface_terrain` | 75.51% | High. Many apartments do not have a specific land surface attached. |

### Property Types (`type_local`)
- **Dépendance** (Garage, cellar, etc.): 4,356 (37%)
- **Appartement**: 3,725 (32%)
- **Maison**: 967 (8%)
- **Local commercial**: 490 (4%)
- **NaN / Other**: 2,122 (18%)

## 3. Price Analysis (Preliminary)

> [!WARNING]
> Statistics below are based on raw rows. Due to the multi-row structure, the Mean is skewed.
> **True Median Price**: ~€296,500 (Representative of the market)

### Outliers
- **High End**: 705 rows have a value > €10,000,000.
    - *Cause*: Large commercial deals, building complexes, or data artifacts where total batch price is applied to individual small lots.
- **Low End**: 40 rows < €1,000.
    - *Cause*: Symbolic sales, small land strips, or errors.

## 4. Recommendations for Sprint 2 (Cleaning & Visualization)

1.  **Filtering Strategy**:
    - To analyze Housing Prices: Filter for `type_local` IN ('Appartement', 'Maison') AND `nature_mutation` == 'Vente'.
2.  **Deduplication**:
    - When analyzing **Price Distribution**: Drop duplicates based on `id_mutation`.
    - When analyzing **Price/m²**: You must sum the `surface_reelle_bati` of all parts of the home (if split) OR more commonly, just take the row corresponding to the main dwelling.
3.  **Feature Engineering**:
    - Create `price_per_sqm`: `valeur_fonciere / surface_reelle_bati`.
    - *Caution*: Only calculate this for rows where `type_local` is living space.
4.  **Handling "Dépendances"**:
    - Do not analyze distinct prices for dependencies, as the value usually covers the whole transaction.

## 5. Next Steps
- Implement a cleaning pipeline to handle the multi-row issue.
- Calculate accurate Price/m² for Apartments and Houses.
- Visualize price distribution excluding extreme outliers.
