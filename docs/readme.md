# Retail Sales & Incentive Data Pipeline

This project aims to simulate a real-time retail sales data pipeline that calculates employee incentives based on their sales performance. The code is designed to handle large volumes of data by leveraging **Apache Spark** for distributed processing and **AWS S3** for cloud storage, ensuring scalability and efficiency. Through this project, you'll gain hands-on experience in building a data pipeline, managing real-time data, and handling partitioned data in Spark.

## Key Features:
- Real-time data processing with Spark.
- Integration with AWS S3 for data storage and retrieval.
- Partitioned data handling to efficiently manage large datasets.
- Comprehensive incentive calculation system based on employee sales performance.

---

## Entity Relationship Diagram (ERD)

```plaintext
Project structure:-
my_project/
├── docs/
│   └── readme.md
├── resources/
│   ├── __init__.py
│   ├── dev/
│   │    ├── config.py
│   │    └── requirement.txt
│   └── qa/
│   │    ├── config.py
│   │    └── requirement.txt
│   └── prod/
│   │    ├── config.py
│   │    └── requirement.txt
│   ├── sql_scripts/
│   │    └── table_scripts.sql
├── src/
│   ├── main/
│   │    ├── __init__.py
│   │    └── delete/
│   │    │      ├── aws_delete.py
│   │    │      ├── database_delete.py
│   │    │      └── local_file_delete.py
│   │    └── download/
│   │    │      └── aws_file_download.py
│   │    └── move/
│   │    │      └── move_files.py
│   │    └── read/
│   │    │      ├── aws_read.py
│   │    │      └── database_read.py
│   │    └── transformations/
│   │    │      └── jobs/
│   │    │      │     ├── customer_mart_sql_transform_write.py
│   │    │      │     ├── dimension_tables_join.py
│   │    │      │     ├── main.py
│   │    │      │     └──sales_mart_sql_transform_write.py
│   │    └── upload/
│   │    │      └── upload_to_s3.py
│   │    └── utility/
│   │    │      ├── encrypt_decrypt.py
│   │    │      ├── logging_config.py
│   │    │      ├── s3_client_object.py
│   │    │      ├── spark_session.py
│   │    │      └── my_sql_session.py
│   │    └── write/
│   │    │      ├── database_write.py
│   │    │      └── parquet_write.py
│   ├── test/
│   │    ├── scratch_pad.py.py
│   │    └── generate_csv_data.py
```


---

## How to Run the Program in PyCharm

1. **Open PyCharm**: Launch the PyCharm IDE on your system.
2. **Clone the Project**: 
   - Use the terminal or PyCharm’s Git integration to clone the project from GitHub:
     ```bash
     git clone https://github.com/piyush02nir/retail_sales_incentive_data_pipeline.git
     ```
3. **Set Up Virtual Environment**:
   - Create or activate a virtual environment (if not already done):
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     cd venv/Scripts
     ./activate
     ```
   *(If `activate` doesn't work, try using `source activate` on UNIX-like systems.)*

4. **Install Dependencies**:
   - Install the required Python packages listed in the `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

5. **Create `main.py`**:
   - Follow the instructions outlined in the accompanying YouTube tutorial to set up the `main.py` script, which will execute the data pipeline.

6. **Configure AWS S3 Access**:
   - Set up an AWS user with full access to S3.
   - Add the **secret key** and **access key** to the configuration file to allow the script to read from and write to S3.

7. **Run the Program**:
   - Execute the `main.py` script using the green play button in PyCharm or by typing the following command in the terminal:
     ```bash
     python main.py
     ```

8. **Troubleshooting**:
   - If the program doesn't execute as expected, review the code and ensure all configurations (AWS, PyCharm, virtual environment) are set up correctly.

---

Enjoy building a scalable and real-time data pipeline for retail sales and employee incentives!
