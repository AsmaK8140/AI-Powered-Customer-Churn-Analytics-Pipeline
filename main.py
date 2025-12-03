from src.data_ingestion import ingest_csv
from src.transformations import transform_churn_data
from src.db_utils import init_db, load_to_db
from src.config_loader import load_config
import os

def run_pipeline(input_csv: str):
    config = load_config()
    raw_dir = config["paths"]["raw_dir"]
    processed_dir = config["paths"]["processed_dir"]
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(processed_dir, exist_ok=True)

    print("Ingesting CSV...")
    raw_path = ingest_csv(input_csv, raw_dir)

    print("Transforming data...")
    processed_path = transform_churn_data(raw_path, processed_dir)

    print("Loading to database...")
    engine = init_db(config["database"]["url"])
    load_to_db(engine, processed_path, table_name="churn_customers")

    print("Pipeline completed successfully.")
    return processed_path

if __name__ == "__main__":
    sample_file = "data/sample_churn_data.csv"
    if not os.path.exists(sample_file):
        raise FileNotFoundError(
            f"Sample file {sample_file} not found. "
            "Place a churn CSV at data/sample_churn_data.csv"
        )
    run_pipeline(sample_file)
