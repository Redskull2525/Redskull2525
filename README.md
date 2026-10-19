# Hi, I'm Abhishek Shelke 👋

**Data Analyst / Data Engineer (entry level)** · Pune, India · M.Sc. Computer Science (2025–2027) · open to full-time roles

I use SQL, Python and PostgreSQL to clean, validate and analyse data, and I turn the results into reports, dashboards and reliable pipelines.

### 💼 Experience
**Freelance Data Engineer at [Minaro](https://minaroapp.com)** (Sep 2026 – present, paid). I build Python pipelines that load community discussions into PostgreSQL, use LLM APIs (OpenAI / Anthropic Claude) to turn them into structured FAQ content, and keep the process reliable with validation, tests and safe publishing. This is client work, so the code is private.

### 📂 Featured projects
| Project | What it shows | Live demo |
|---|---|---|
| ⭐ [Retail Operations Intelligence](https://github.com/Redskull2525/retail-operations-intelligence) | **ETL + SQL + BI.** Pandas pipeline that validates and cleans data into a SQLite star schema; 10 business SQL queries (CTEs, window functions); Streamlit KPI dashboard; a 4-page **Power BI** report (PBIP) whose DAX measures were checked against SQL (126/126 match); 26 pytest tests in CI. *Synthetic data, clearly labelled.* | [Open](https://retail-operations-intelligence-abhishek.streamlit.app) |
| [Customer Churn Prediction](https://github.com/Redskull2525/Customer-Churn-Prediction-ML-Model) | **ML evaluation done properly.** scikit-learn Pipeline + Random Forest on 3,333 customers. Test: 94% accuracy, ROC-AUC 0.93, churn recall 0.61, including an evaluation bug I found and fixed. | [Open](https://customer-churn-prediction-ml-model-abhi.streamlit.app) |
| [Stock Prediction Dashboard](https://github.com/Redskull2525/stock-prediction) | **Time-series done carefully.** Live market-data API, 40+ technical indicators, time-ordered split, naive-baseline comparison and directional accuracy; four date-alignment bugs found and fixed with unit tests; CI. | needs an API key, see README |
| [Credit Risk Scoring](https://github.com/Redskull2525/credit-risk-analysis-ml) | **Decisions, not just scores.** German Credit data (public, CC BY 4.0): Logistic Regression vs Random Forest with 5-fold CV, test ROC-AUC 0.79, cost-based threshold (bad-loan recall 0.73 → 0.93), protected attributes excluded with an ablation, model card, 20 tests in CI. | [Open](https://credit-risk-analysis-ml-abhishek.streamlit.app) |
| [Spam Email Detection](https://github.com/Redskull2525/Spam-Email-Detection) | NLTK text cleaning + LSTM classifier. Balanced test set of 600 emails: 97.8% accuracy, spam recall 0.997. | [Open](https://spam-email-detection-abhi.streamlit.app) |
| [Boston Housing Model Comparison](https://github.com/Redskull2525/boston-housing-ml-model-comparison) | Linear Regression vs Random Forest vs Gradient Boosting (best test R² 0.77) with an honest note on the dataset's problems. | [Open](https://boston-housing-ml-model-comparison-abhishek.streamlit.app) |
| [Time-Series Anomaly Detection](https://github.com/Redskull2525/time-series-anomaly-detection) | Isolation Forest and One-Class SVM on Reliance Industries stock data. | – |

Live demos run on Streamlit Community Cloud and take about a minute to wake up after a quiet period. Each featured repo has a `docs/INTERVIEW_GUIDE.md` explaining the design decisions, metrics and limitations.

### 🛠 Skills
- **SQL:** joins, aggregation, CTEs, window functions · PostgreSQL, SQLite
- **Python:** Pandas, NumPy, scikit-learn, Plotly, Streamlit, pytest
- **BI & reporting:** Power BI (star schema, DAX, PBIP), Excel (pivot tables, lookups), KPI dashboards
- **Data engineering:** ETL, data validation, incremental loads, GitHub Actions

📫 [LinkedIn](https://www.linkedin.com/in/abhishek-s-b98895249) · abhishekbalkrishnashelke5555@gmail.com

<sub>Synthetic data is labelled wherever it's used. Metrics come from each repo's own notebook, script or test output.</sub>
