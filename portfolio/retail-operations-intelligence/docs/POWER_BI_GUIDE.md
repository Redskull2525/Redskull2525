# Power BI build guide

## Model
Import:
- FactSales: sales transaction table
- DimProduct: product catalog
- FactInventorySnapshot: product-region snapshot
- Optional DimDate: calendar table related to FactSales[order_date]

Relationships:
- DimProduct[product_id] 1 → * FactSales[product_id]
- DimProduct[product_id] 1 → * FactInventorySnapshot[product_id]
- DimDate[Date] 1 → * FactSales[order_date]

Keep sales and inventory as separate fact tables because they have different grains. Directly joining facts can duplicate sales and inflate measures.

## DAX measures
```DAX
Total Revenue = SUM ( FactSales[revenue] )
Total Cost = SUM ( FactSales[cost] )
Gross Profit = [Total Revenue] - [Total Cost]
Gross Margin % = DIVIDE ( [Gross Profit], [Total Revenue], 0 )
Units Sold = SUM ( FactSales[quantity] )
Order Count = DISTINCTCOUNT ( FactSales[order_id] )
Average Order Value = DIVIDE ( [Total Revenue], [Order Count], 0 )
Inventory Units = SUM ( FactInventorySnapshot[on_hand_units] )
Inventory Value = SUM ( FactInventorySnapshot[inventory_value] )
Reorder Alert Count =
CALCULATE ( COUNTROWS ( FactInventorySnapshot ),
    FactInventorySnapshot[stock_status] = "Reorder" )
Overstock Alert Count =
CALCULATE ( COUNTROWS ( FactInventorySnapshot ),
    FactInventorySnapshot[stock_status] = "Overstock" )
```

## Suggested report pages
1. Executive Overview: KPI cards, monthly trend, region and category comparison.
2. Product Performance: top products, revenue-vs-profit scatter, margin table.
3. Inventory Exceptions: reorder alerts, overstock value, region/category slicers.
4. Data Quality: nulls, duplicates, date coverage, reconciliation checks.

## Validation
- Format revenue/profit as INR currency and margin as percentage.
- Check order count uses distinct order IDs.
- Reconcile totals against source CSVs.
- Do not sum inventory snapshots across dates without defining time logic.
- Label the dataset synthetic.
