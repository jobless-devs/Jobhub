import pandas as pd
import os
from glob import glob
from datetime import datetime
from typing import List

def aggregate_csv_files(source_dir: str, output_dir: str) -> None:
    # Convert relative paths to absolute paths
    source_dir_abs = os.path.abspath(source_dir)
    output_dir_abs = os.path.abspath(output_dir)
    
    # Print the absolute paths
    print(f"Source directory: {source_dir_abs}")
    print(f"Output directory: {output_dir_abs}")
    
    # Ensure the output directory exists
    os.makedirs(output_dir_abs, exist_ok=True)
    
    # Get all CSV files from the source directory
    all_files: List[str] = glob(os.path.join(source_dir_abs, '*.csv'))
    
    # Exit if no CSV files are found
    if not all_files:
        print("No CSV files found to aggregate.")
        return
    
    # Generate a list of DataFrames by reading each CSV file
    df_list = [pd.read_csv(f, index_col=None, header=0) for f in all_files]
    
    # Concatenate all DataFrames into one and drop duplicates based on the 'job_url' column
    if df_list:
        combined_df: pd.DataFrame = pd.concat(df_list, axis=0, ignore_index=True).drop_duplicates(subset='job_url')
        
        # Generate a date prefix for the filename based on the current date
        date_prefix: str = datetime.now().strftime('%Y%m%d')  # Format: 'YYYYMMDD'
        
        # Create the full path for the output file with the date prefix
        output_file: str = os.path.join(output_dir_abs, f'aggregated_jobs_{date_prefix}.csv')
        
        # Save the combined DataFrame to the CSV file
        combined_df.to_csv(output_file, index=False)
        print(f"Aggregated data saved to {output_file}")
    else:
        print("No data to write.")

# Usage
source_dir = 'data/individual_scrapers'
output_dir = '/app/data/aggregated'
aggregate_csv_files(source_dir, output_dir)