
# NaijaMart Sales Data Cleaning and Exploratory Data Analysis

## Project Overview

NaijaMart is a retail sales data project built with Python and Pandas. It focuses on cleaning raw sales data, validating data quality, creating useful analytical features, and identifying business insights from transaction records.

## Objectives

- Clean and standardise raw sales data.
- Handle duplicate records, missing values, invalid dates, and inconsistent formats.
- Convert prices into numeric values.
- Flag suspicious quantity values for further investigation.
- Create revenue and date-based features.
- Analyse sales performance across products, cities, months, payment methods, and customers.
- Export a cleaned dataset for future analysis.

## Tools Used

- Python
- Pandas
- CSV
- GitHub

## Dataset

The original dataset contained 1,625 rows and 9 columns. After removing 25 duplicate records, the cleaned dataset contained **1,600 rows and 17 columns**.

## Data Cleaning and Transformation

The workflow included:

1. Removing duplicate records and checking order ID uniqueness.
2. Standardising categorical values.
3. Handling missing customer and email information where a reliable mapping was available.
4. Converting currency-formatted prices to numeric values.
5. Converting dates to datetime format and preserving invalid dates as missing.
6. Flagging negative quantities rather than automatically deleting them.
7. Creating `Revenue`, `Transaction_Value`, `Year`, `Month`, `Month_Name`, `Day_Name`, and `Quarter` columns.
8. Validating revenue calculations against quantity multiplied by price.
9. Exporting the cleaned dataset to CSV.

## Key Findings

### Product Performance
- Smartphones had the highest order count, with 180 orders.
- Laptops generated the highest total revenue, at ₦197,982,818.

### City Performance
- Lagos had the highest order count among the identified cities, with 236 orders.
- Benin City generated the highest total revenue, at ₦86,259,471.

### Monthly Performance
- March recorded the highest monthly revenue, at ₦91,619,581.
- July recorded the highest order count, with 253 orders.
- February had the highest average revenue per order among the months analysed.

### Payment Methods
- USSD generated the highest total revenue among the identified payment methods, at ₦168,618,732.

### Customer Analysis
- Aisha Musa generated the highest total revenue among the named customers, at ₦67,503,780.
- Tunde Bello recorded the highest order count, with 182 orders.
- The top three named customers contributed approximately 34.32% of total dataset revenue.

## Data Quality and Limitations

The final dataset contains 1,600 rows and 17 columns, with no duplicate order IDs and no revenue calculation mismatches.

Remaining data-quality issues:
- 15 records have invalid or missing dates.
- 2 records have missing email addresses.
- 20 records have negative quantities. These were retained and flagged because the dataset does not establish whether they represent returns, refunds, or data-entry errors.
- Records with missing dates cannot be reliably assigned to monthly or quarterly groups.
- Revenue uses signed quantities, so negative-quantity records reduce total revenue and affect averages and contribution percentages.

## Project Files

- `explore_data.py` — Python cleaning, transformation, and analysis script.
- `naijamart_raw_sales.csv` — Original raw dataset.
- `naijamart_cleaned_sales.csv` — Cleaned dataset exported by the script.

## How to Run

Install Pandas:

```bash
pip install pandas
```

Ensure the raw CSV is in the location expected by the script, then run:

```bash
python explore_data.py
```

The script should recreate the cleaned CSV when it completes successfully.

## Skills Demonstrated

- Data cleaning and preprocessing
- Missing-value handling
- Duplicate detection
- Data type conversion
- Date feature engineering
- Conditional flags and calculated columns
- Pandas grouping and aggregation
- Exploratory data analysis
- Data-quality validation
- CSV export and verification
