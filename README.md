# Customer Churn Analytics Pipeline (dbt-ready skeleton + Streamlit)

This project is a starter implementation for a Customer Churn Analytics pipeline
using Python, Streamlit, and SQLite. It ingests a churn CSV, performs basic
transformations, and loads the results into a local SQLite database, with a
Streamlit UI for running the pipeline and viewing data.

## Quickstart

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py  # runs pipeline on sample data
streamlit run app/streamlit_app.py
```
