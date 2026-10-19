import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Retail Operations Intelligence", page_icon="📊", layout="wide")
ROOT = Path(__file__).parent
DATA = ROOT / "data"

@st.cache_data
def load_data():
    sales_path = DATA / "sales_transactions.csv"
    inventory_path = DATA / "inventory_snapshot.csv"
    products_path = DATA / "product_catalog.csv"
    if sales_path.exists() and inventory_path.exists() and products_path.exists():
        return (pd.read_csv(sales_path, parse_dates=["order_date"]),
                pd.read_csv(inventory_path),
                pd.read_csv(products_path))
    # Streamlit Cloud fallback: create clearly synthetic demo data if CSVs are not present.
    rng = np.random.default_rng(42)
    categories = {
        "Electronics": ["Wireless Mouse", "USB-C Hub", "Bluetooth Speaker", "Webcam", "Keyboard"],
        "Home": ["Desk Lamp", "Storage Box", "Water Bottle", "Bedsheet Set", "Air Purifier"],
        "Office": ["Notebook Pack", "Office Chair", "Monitor Stand", "Pen Set", "Paper Ream"],
        "Lifestyle": ["Backpack", "Travel Mug", "Yoga Mat", "Lunch Box", "Fitness Band"],
    }
    products = []
    for cat, names in categories.items():
        for name in names:
            cost = int(rng.integers(120, 2500))
            products.append({"product_id": f"P{len(products)+1:03d}", "product_name": name,
                             "category": cat, "unit_cost": cost, "unit_price": int(cost*rng.uniform(1.25,1.85)),
                             "reorder_point": int(rng.integers(12,35)), "target_stock": int(rng.integers(50,120))})
    products = pd.DataFrame(products)
    dates = pd.date_range("2025-01-01", "2025-12-31", freq="D")
    regions = ["West", "North", "South", "East"]
    rows = []
    for i in range(6000):
        p = products.iloc[int(rng.integers(0,len(products)))]
        qty = int(rng.integers(1,6))
        discount = float(rng.choice([0,0,0,.05,.10,.15]))
        revenue = round(p.unit_price*qty*(1-discount),2)
        cost = int(p.unit_cost)*qty
        rows.append({"order_id":f"O{i+1:06d}", "order_date":dates[int(rng.integers(0,len(dates)))],
                     "region":regions[int(rng.integers(0,len(regions)))], "product_id":p.product_id,
                     "product_name":p.product_name, "category":p.category, "quantity":qty,
                     "unit_price":int(p.unit_price), "unit_cost":int(p.unit_cost), "discount_pct":discount,
                     "revenue":revenue, "cost":cost, "profit":round(revenue-cost,2),
                     "channel":str(rng.choice(["Online","Retail Store","Marketplace"]))})
    sales = pd.DataFrame(rows)
    inventory_rows = []
    for _, p in products.iterrows():
        for region in regions:
            on_hand = int(rng.integers(0,int(p.target_stock)+1))
            inventory_rows.append({"snapshot_date":"2025-12-31","region":region,"product_id":p.product_id,
                "product_name":p.product_name,"category":p.category,"on_hand_units":on_hand,
                "reorder_point":int(p.reorder_point),"target_stock":int(p.target_stock),
                "units_sold_year":int(sales[(sales.product_id==p.product_id)&(sales.region==region)].quantity.sum()),
                "unit_cost":int(p.unit_cost),"inventory_value":on_hand*int(p.unit_cost),
                "stock_status":"Reorder" if on_hand<=int(p.reorder_point) else ("Overstock" if on_hand>int(p.target_stock) else "Healthy")})
    return sales, pd.DataFrame(inventory_rows), products

sales, inventory, products = load_data()
st.title("📊 Retail Operations Intelligence")
st.caption("Portfolio demonstration • Synthetic data only • Revenue, profitability, and inventory decisions")

with st.sidebar:
    st.header("Filters")
    min_d, max_d = sales.order_date.min().date(), sales.order_date.max().date()
    dates = st.date_input("Order date range", value=(min_d,max_d), min_value=min_d, max_value=max_d)
    regions = sorted(sales.region.unique())
    region_filter = st.multiselect("Region", regions, default=regions)
    cats = sorted(sales.category.unique())
    category_filter = st.multiselect("Category", cats, default=cats)
    channels = sorted(sales.channel.unique())
    channel_filter = st.multiselect("Channel", channels, default=channels)

if isinstance(dates, tuple) and len(dates)==2:
    start, end = pd.Timestamp(dates[0]), pd.Timestamp(dates[1])+pd.Timedelta(days=1)
else:
    start, end = pd.Timestamp(min_d), pd.Timestamp(max_d)+pd.Timedelta(days=1)
df = sales[(sales.order_date>=start)&(sales.order_date<end)&sales.region.isin(region_filter)&
           sales.category.isin(category_filter)&sales.channel.isin(channel_filter)].copy()
if df.empty:
    st.warning("No rows match the filters. Change your selection.")
    st.stop()

revenue, profit = df.revenue.sum(), df.profit.sum()
margin = profit/revenue*100 if revenue else 0
k = st.columns(5)
k[0].metric("Revenue",f"₹{revenue:,.0f}")
k[1].metric("Gross profit",f"₹{profit:,.0f}")
k[2].metric("Gross margin",f"{margin:.1f}%")
k[3].metric("Orders",f"{df.order_id.nunique():,}")
k[4].metric("Units sold",f"{df.quantity.sum():,}")

overview, products_tab, inventory_tab, data_tab = st.tabs(["Executive Overview","Product Performance","Inventory Actions","Data Explorer"])
with overview:
    df["month"] = df.order_date.dt.to_period("M").astype(str)
    trend = df.groupby("month",as_index=False).agg(Revenue=("revenue","sum"),Profit=("profit","sum"))
    a,b=st.columns(2)
    a.plotly_chart(px.line(trend,x="month",y="Revenue",markers=True,title="Monthly revenue"),use_container_width=True)
    b.plotly_chart(px.line(trend,x="month",y="Profit",markers=True,title="Monthly gross profit"),use_container_width=True)
    region = df.groupby("region",as_index=False).agg(Revenue=("revenue","sum"),Profit=("profit","sum"))
    a,b=st.columns(2)
    a.plotly_chart(px.bar(region,x="region",y="Revenue",title="Revenue by region"),use_container_width=True)
    b.plotly_chart(px.bar(region,x="region",y="Profit",title="Profit by region"),use_container_width=True)
with products_tab:
    perf=df.groupby(["product_id","product_name","category"],as_index=False).agg(Revenue=("revenue","sum"),Profit=("profit","sum"),Units=("quantity","sum"))
    perf["Margin %"]=(perf.Profit/perf.Revenue*100).round(1)
    a,b=st.columns(2)
    a.plotly_chart(px.bar(perf.nlargest(10,"Revenue"),x="Revenue",y="product_name",orientation="h",title="Top 10 products by revenue"),use_container_width=True)
    b.plotly_chart(px.scatter(perf,x="Revenue",y="Profit",size="Units",color="category",hover_name="product_name",title="Revenue vs profit"),use_container_width=True)
    st.dataframe(perf.sort_values("Revenue",ascending=False),use_container_width=True,hide_index=True)
with inventory_tab:
    inv=inventory[inventory.region.isin(region_filter)&inventory.category.isin(category_filter)].copy()
    inv["recommended_action"]=inv.apply(lambda r:f"Reorder {max(int(r.target_stock-r.on_hand_units),0)} units" if r.on_hand_units<=r.reorder_point else ("Review slow-moving stock" if r.on_hand_units>r.target_stock else "No immediate action"),axis=1)
    a,b,c=st.columns(3)
    a.metric("Reorder alerts",int((inv.stock_status=="Reorder").sum()))
    b.metric("Overstock alerts",int((inv.stock_status=="Overstock").sum()))
    c.metric("Inventory value",f"₹{inv.inventory_value.sum():,.0f}")
    st.dataframe(inv[inv.stock_status=="Reorder"].sort_values("on_hand_units"),use_container_width=True,hide_index=True)
    st.caption("Inventory snapshot is synthetic and dated 2025-12-31; it is not live stock data.")
with data_tab:
    st.download_button("Download filtered transactions CSV",df.to_csv(index=False).encode(),file_name="filtered_sales.csv",mime="text/csv")
    st.dataframe(df.sort_values("order_date",ascending=False),use_container_width=True,hide_index=True)

with st.expander("Methodology and limitations"):
    st.write("All data is synthetic and generated for portfolio demonstration. No real company performance or financial savings are claimed.")
    st.write("Gross profit excludes operating expenses, shipping, returns, and taxes; it is not net profit.")
