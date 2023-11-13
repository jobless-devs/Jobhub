import pandas as pd
import os
from glob import glob
from typing import List

def aggregate_csv_files(source_dir: str, output_dir: str) -> str:
    """
    Aggregate all CSV files from the source directory into a single file in the output directory.
    Duplicate entries are identified by the 'job_url' column and removed.
    Returns the path of the aggregated CSV file
    Optional: After successful aggregation, individual CSV files are deleted.
    """
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
    
    # Concatenate all DataFrames into one
    if df_list:
        combined_df: pd.DataFrame = pd.concat(df_list, axis=0, ignore_index=True)
        
        # Count the number of rows before removing duplicates
        rows_before = combined_df.shape[0]
        
        # Drop duplicates based on the 'job_url' column
        combined_df.drop_duplicates(subset='job_url', inplace=True)
        
        # Count the number of rows after removing duplicates
        rows_after = combined_df.shape[0]
        
        # Calculate and print the number of removed duplicates
        duplicates_removed = rows_before - rows_after
        print(f"Initial number of data rows: {rows_before}")
        print(f"Number of duplicates removed: {duplicates_removed}")
        print(f"Final number of data rows: {rows_after}")
        
        # Create the full path for the output file
        output_file: str = os.path.join(output_dir_abs, 'aggregated_jobs.csv')
        
        # Save the combined DataFrame to the CSV file
        combined_df.to_csv(output_file, index=False)
        print(f"Aggregated data saved to {output_file}")
        
        # Delete individual run files after successful aggregation
        # for f in all_files:
        #     try:
        #         os.remove(f)
        #         print(f"Deleted file: {f}")
        #     except OSError as e:
        #         print(f"Error deleting file {f}: {e.strerror}")
        return output_file
    else:
        print("No data to write.")

if __name__ == "__main__":
    # Directories for the source of individual CSV files and the output for the aggregated file
    source_dir = 'data/individual_run'
    output_dir = '/app/data/aggregated'
    
    # Call the function to aggregate CSV files
    aggregate_csv_files(source_dir, output_dir)
