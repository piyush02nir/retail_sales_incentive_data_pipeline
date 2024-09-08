import os

key = "youtube_project"
iv = "youtube_encyptyo"
salt = "youtube_AesEncryption"

#AWS Access And Secret key
aws_access_key = "AWS_ACCESS_KEY"
aws_secret_key = "AWS_SECRET_KEY"
bucket_name = "ecom-data-de"
s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"


# Database credential
# MySQL database connection properties
database_name = "ecom_data_mart"
host = "localhost"
user = "root"
password = os.getenv('MYSQL_PASSWORD')
url = f"jdbc:mysql://{host}:3306/{database_name}"
driver = "com.mysql.cj.jdbc.Driver"

properties = {
    "user": user,
    "password": password,
    "driver": driver
}


# Table name
customer_table_name = "customer"
product_staging_table = "product_staging_table"
product_table = "product"
sales_team_table = "sales_team"
store_table = "store"

#Data Mart details
customer_data_mart_table = "customers_data_mart"
sales_team_data_mart_table = "sales_team_data_mart"

# Required columns
mandatory_columns = ["customer_id","store_id","product_name","sales_date","sales_person_id","price","quantity","total_cost"]


# File Download location
local_directory = "D:\\Data_Engineer\\DE_Projects\\ecome_sparkdata\\file_from_s3\\"
customer_data_mart_local_file = "D:\\Data_Engineer\\DE_Projects\\ecome_sparkdata\\customer_data_mart\\"
sales_team_data_mart_local_file = "D:\\Data_Engineer\\DE_Projects\\ecome_sparkdata\\sales_team_data_mart\\"
sales_team_data_mart_partitioned_local_file = "D:\\Data_Engineer\\DE_Projects\\ecome_sparkdata\\sales_partition_data\\"
error_folder_path_local = "D:\\Data_Engineer\\DE_Projects\\ecome_sparkdata\\error_files\\"
