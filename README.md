# 🏠 Bordeaux Real Estate Analysis

**Real Estate Analysis and Visualization in Bordeaux (2024)**

A real estate data analysis project based on DVF (Demandes de Valeurs Foncières) data from the French government, focusing on the Bordeaux metropolitan area.

## 🎯 Project Goals

- Analyze real estate price trends in the Bordeaux region
- Identify patterns by neighborhood and property type
- Create clear and informative visualizations
- Practice the complete Data Science project cycle (from raw data to results)

## 📊 Data Source

Data comes from the official **DVF (Demandes de Valeurs Foncières)** database:

- Source: [data.gouv.fr](https://files.data.gouv.fr/geo-dvf/latest/csv/)
- Scope: Gironde Department (33)
- Period: 2024

## 🚀 Installation and Usage

### Prerequisites

```bash
python 3.8+
pandas
matplotlib
seaborn
requests
```

### Install Dependencies

```bash
pip install pandas matplotlib seaborn jupyter requests
```

### Download Data

The script automatically downloads the data on first run. Alternatively:

1. Go to https://files.data.gouv.fr/geo-dvf/latest/csv/2024/departements/
2. Download `33.csv.gz` (Gironde department)
3. Place the file in the project folder

### Run Analysis

```bash
python analysis.py
```

## 📅 Roadmap

### ✅ Sprint 1 (Week 1-2) - IN PROGRESS

- [X] Repository setup
- [X] DVF data download
- [X] Data loading and filtering
- [X] Initial dataset exploration
- [X] **Result**: 11,660 real estate transactions in Bordeaux loaded
- [ ] Data cleaning (filter sales, houses/apartments)
- [ ] Feature engineering (price per sqm)
- [ ] Outlier management

### 📋 Sprint 2 (Week 3-4)

- [ ] Data cleaning
- [ ] Create visualizations
- [ ] Price analysis by neighborhood

### 🎨 Sprint 3 (Month 2)

- [ ] Interactive dashboard
- [ ] Final documentation
- [ ] Deployment

## 👨‍💻 Author

Project completed as part of the Master's in Computer Science (AI track) - University of Bordeaux

## 📝 License

This project uses public data from the French government.
