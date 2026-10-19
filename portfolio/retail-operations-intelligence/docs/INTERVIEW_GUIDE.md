# Interview guide

## 60-second pitch
"I built a retail operations intelligence dashboard to demonstrate how a data analyst can connect sales reporting with inventory decisions. I used a clearly labeled synthetic dataset and Python/Pandas to calculate revenue, gross profit, margin, order count and units sold. The Streamlit interface provides date/region/category/channel filters, monthly and regional trends, product profitability views, and an inventory exception queue. I also documented a Power BI model and DAX measures. Since the data is synthetic, I describe this as a portfolio demonstration rather than claiming real company savings."

## Remember
- Revenue = quantity × unit price × (1 − discount).
- Gross profit = revenue − cost of goods sold; it is not net profit.
- Gross margin % = gross profit / revenue × 100.
- Sales rows are transaction-level; inventory rows are product-region-snapshot-level.
- Keep separate fact tables to avoid duplicated totals.
- A slicer filters the report interactively.
- Synthetic data demonstrates the workflow but cannot prove real-world impact.

## Common questions
1. **What problem does it solve?** It demonstrates how to monitor revenue/profit and surface inventory exceptions in one reporting view.
2. **Why Streamlit?** Fast way to build an interactive Python analytics app. Production needs authentication, monitoring, data refresh and tests.
3. **How do you validate the data?** Recompute totals independently, check nulls/duplicates, validate the revenue formula, and reconcile Power BI with Python.
4. **How would you improve reorder logic?** Include supplier lead time, demand variability, service level, open purchase orders and safety stock.
5. **What are limitations?** Synthetic data, no returns/shipping expenses, no live stock feed and simplified thresholds.
6. **What would you do with real data?** Profile quality, confirm KPI definitions with stakeholders, clean and validate records, automate refresh, reconcile totals and document caveats.
7. **How do you calculate average order value?** Total revenue divided by distinct order count, with safe division for zero orders.
8. **What is a star schema?** A dimensional model where fact tables hold measurable events and dimensions hold descriptive attributes.

## Practice before interview
1. Run the app and use every filter.
2. Explain each KPI without reading this document.
3. Modify one chart and add one measure yourself.
4. Import equivalent data into Power BI and validate totals.
5. Explain limitations honestly. Do not claim measured savings or real company outcomes.
