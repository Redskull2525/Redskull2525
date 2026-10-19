# Retail Operations Intelligence Dashboard

**Portfolio project for Data Analyst / BI Analyst roles.** Interactive retail reporting built with Python, Pandas, Plotly and Streamlit, with a Power BI model and DAX guide.

> **Data honesty:** the included/generated records are synthetic demonstration data, not real company records. The project demonstrates analytical workflow and design, not proven business savings.

## Business problem
Retail teams need a consistent view of sales, profitability, product performance and stock exceptions. This dashboard combines transaction KPIs with an illustrative inventory snapshot.

## Features
- Revenue, gross profit, gross margin, order count and units sold
- Date, region, category and sales-channel filters
- Monthly revenue/profit and regional comparisons
- Product revenue-vs-profit analysis
- Reorder and overstock exception queue
- CSV export for filtered transactions
- Power BI data-model and DAX guidance in [docs/POWER_BI_GUIDE.md](docs/POWER_BI_GUIDE.md)
- Interview explanation and question bank in [docs/INTERVIEW_GUIDE.md](docs/INTERVIEW_GUIDE.md)

## Run locally
```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy
1. Open https://share.streamlit.io/ and sign in with GitHub.
2. Select repository `Redskull2525/Redskull2525`.
3. Set the main file path to `portfolio/retail-operations-intelligence/app.py`.
4. Deploy and test the app. A deployment URL should only be shared after the deployment is confirmed.

## Metrics
- Revenue = quantity × unit price × (1 − discount)
- Gross profit = revenue − product cost
- Gross margin % = gross profit / revenue
- Reorder alert = on-hand units ≤ reorder point
- Overstock alert = on-hand units > target stock

Gross profit is not net profit. A production version would require validated source data, stock refreshes, access control, demand/lead-time logic, and operational monitoring.

## Resume bullets (use after running and understanding the project)
- Built an interactive Streamlit dashboard using Python, Pandas and Plotly to analyze synthetic retail transaction data across revenue, gross profit, product performance and regional trends.
- Implemented multi-dimensional filters, CSV exports and an inventory exception view; documented a Power BI-ready model and DAX measures for business KPI reporting.

Do not claim real-world financial impact, savings or model accuracy from synthetic data.
