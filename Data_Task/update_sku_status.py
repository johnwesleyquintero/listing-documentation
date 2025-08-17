import pandas as pd

def update_sku_status(input_csv_path, output_csv_path):
    # Read the input CSV file
    input_df = pd.read_csv(input_csv_path)

    # Read the output CSV file
    output_df = pd.read_csv(output_csv_path)

    # Create a dictionary mapping seller-sku to status from the input file
    # Ensure 'seller-sku' and 'status' columns exist in input_df
    if 'seller-sku' not in input_df.columns or 'status' not in input_df.columns:
        print("Error: 'seller-sku' or 'status' column not found in the input CSV.")
        return

    sku_status_map = input_df.set_index('seller-sku')['status'].to_dict()

    # Update the 'Status' column in the output DataFrame based on the 'SKU' column
    # Ensure 'SKU' and 'Status' columns exist in output_df
    if 'SKU' not in output_df.columns or 'Status' not in output_df.columns:
        print("Error: 'SKU' or 'Status' column not found in the output CSV.")
        return

    output_df['Status'] = output_df['SKU'].map(sku_status_map).fillna(output_df['Status'])

    # Save the updated DataFrame back to the output CSV file
    output_df.to_csv(output_csv_path, index=False)
    print(f"Successfully updated SKU statuses in {output_csv_path}")

if __name__ == "__main__":
    input_file = 'c:\\Users\\johnw\\listing-documentation\\Data_Task\\Input\\STK_Data_Dump - BR Raw.csv'
    output_file = 'c:\\Users\\johnw\\listing-documentation\\Data_Task\\Output\\STK_Data_Dump - Disable_Brazil (BR).csv'
    update_sku_status(input_file, output_file)