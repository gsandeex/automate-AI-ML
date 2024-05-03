'''import pandas as pd

# Load the CSV file (replace 'your_file.csv' with your actual file path)
csv_file = 'C:\\Users\\GSANDEEX\\Downloads\\sandeep-gptj-c3d-standard-8_GPT-J_custom_run.csv'
df = pd.read_csv(csv_file)
column_names = df.columns.tolist()
print("===========================")
print(column_names)
# Get unique values from the "precision" column
unique_precisions = df[' Precision'].unique()
print("=============================")
print(unique_precisions)

# Initialize an empty DataFrame to store the final results
final_filtered_data = pd.DataFrame()

# Iterate through each unique precision value
for precision_value in unique_precisions:
    # Filter by "precision" value
    precision_filtered = df[df[' Precision'] == precision_value]
    
    # Filter by "Batch size" == 1
    batch_size_filtered = precision_filtered[precision_filtered[' BS'] == 1]
    
    # Filter by "latency" close to 15 (adjust threshold as needed)
    latency_threshold = 0.5
    # latency_filtered = batch_size_filtered[
    #     (batch_size_filtered[' Latency(s)'] >= 15 - latency_threshold) &
    #     (batch_size_filtered[' Latency(s)'] <= 15 + latency_threshold)
    # ]
    latency_filtered = batch_size_filtered[
        (batch_size_filtered[' Latency(s)'] <= 10) 
    ]

    
    # Append the filtered data to the final results
    #final_filtered_data = final_filtered_data.append(latency_filtered)
    final_filtered_data = pd.concat([final_filtered_data, latency_filtered], ignore_index=True)
print(final_filtered_data)
import pdb;pdb.set_trace()

# Save the final filtered data to separate Excel files
for precision_value in unique_precisions:
    output_file = f'filtered_data_{precision_value}.xlsx'
    precision_data = final_filtered_data[final_filtered_data[' Precision'] == precision_value]
    precision_data.to_excel(output_file, index=False)
    print(f"Filtered data for precision '{precision_value}' saved to {output_file}")

print("All filtered data saved successfully!")
'''

'''
import pandas as pd

# Load the CSV file (replace 'your_file.csv' with the actual file path)
csv_file = 'C:\\Users\\GSANDEEX\\Downloads\\sandeep-gptj-c3d-standard-8_GPT-J_custom_run.csv'
df = pd.read_csv(csv_file)

# Filter by "Batch size" == 1
batch_size_filtered = df[df[' BS'] == 1]

# Filter by "latency" below 15
latency_threshold = 15
latency_filtered = batch_size_filtered[batch_size_filtered[' Latency(s)'] < latency_threshold]

# Find the row with the highest throughput
max_throughput_row = latency_filtered.loc[latency_filtered[' Throughput(tokens/s)'].idxmax()]

# Save the final row to a new Excel file
output_file = 'highest_throughput_below_15.xlsx'
max_throughput_row.to_excel(output_file, index=False)
print(f"Highest throughput row (latency < 15) saved to {output_file}")

'''

################ 

def Resnet_50_v1_5_src():
    pass

def BertLarge_src():
    pass

def DLRM_src():
    pass

def gptj_src():
    pass

def llama_src():
    pass

##############

def Resnet_50_v1_5_paiv():
    pass

def BertLarge_paiv():
    pass

def DLRM_paiv():
    pass

def gptj_paiv():
    pass

def llama_paiv():
    pass

###############

def golden_config_maker(csv_file_path):
    import pandas as pd

    # Load the CSV file (replace 'your_file.csv' with the actual file path)
    csv_file = "C:\\Users\\GSANDEEX\\OneDrive - Intel Corporation\\Documents\\AI-ML runs\\Sienna-test\\Quanta-48C\\quanta-18-AI_resnet50v1_5_custom_run.csv"
    #"C:\\Users\\GSANDEEX\\Downloads\\temp\\Genoa 96c\\Zendnn-Latest-sweep-genoa27_resnet50v1_5AT_BS1_custom_run.csv" #'C:\\Users\\GSANDEEX\\Downloads\\sandeep-gptj-c3d-standard-8_GPT-J_custom_run.csv'
    df = pd.read_csv(csv_file)
    df[' Latency(ms)']=df[' Latency(ms)'].str.replace(' ','')
    #df[' Latency(ms)'] = df[' Latency(ms)'].astype(float)
    df[' Latency(ms)'] = df[' Latency(ms)'].apply(lambda x: float(x) if x.strip() else None)


    column_names = df.columns.tolist()

    for name in column_names:
        lower_name = name.lower()
        if 'throughput' in lower_name:
            throughput_column_name = name
        if 'latency' in lower_name:
            latency_column_name = name
        if 'bs' in lower_name or 'batch' in lower_name or 'batch size' in lower_name or 'batchsize' in lower_name:
            batchsize_column_name = name
        if 'precision' in lower_name:
            precision_column_name = name


    #import pdb;pdb.set_trace()
    ##### this line for removing spaces in the column names. #####
    #df.columns = df.columns.str.replace(' ', '')

    # Get unique values from the "precision" column
    unique_precisions = df[precision_column_name].unique()

    # Initialize an empty DataFrame to store the final results
    final_filtered_data = pd.DataFrame()

    # Iterate through each unique precision value
    for precision_value in unique_precisions:
        # Filter by "precision" value
        precision_filtered = df[df[precision_column_name] == precision_value]
        
        # Filter by "Batch size" == 1
        batch_size_filtered = precision_filtered[precision_filtered[batchsize_column_name] == 1]
        
        # Filter by "latency" close to 15 (adjust threshold as needed)
        latency_threshold = 15
        latency_filtered = batch_size_filtered[batch_size_filtered[latency_column_name] < latency_threshold]

        # Find the row with the highest throughput
        max_throughput_row = latency_filtered.loc[latency_filtered[throughput_column_name].idxmax()]
        max_throughput_row_horizontal = max_throughput_row.to_frame().T
        
        
        # Append the filtered data to the final results
        print(max_throughput_row_horizontal)
        final_filtered_data = pd.concat([final_filtered_data, max_throughput_row_horizontal], ignore_index=True)

    for precision_value in unique_precisions:
        # Filter by "precision" value
        precision_filtered = df[df[precision_column_name] == precision_value]
        
        # Filter not by "Batch size" == 1
        batch_size_filtered = precision_filtered[precision_filtered[batchsize_column_name] != 1]
        max_throughput_row_bsn = batch_size_filtered.loc[batch_size_filtered[throughput_column_name].idxmax()]
        max_throughput_row_horizontal_bsn = max_throughput_row_bsn.to_frame().T
        final_filtered_data = pd.concat([final_filtered_data, max_throughput_row_horizontal_bsn], ignore_index=True)

    print(final_filtered_data)


    output_file = f'just-data.xlsx'
    final_filtered_data.to_excel(output_file, index=False)

    # for precision_value in unique_precisions:
    #     output_file = f'filtered_data_{precision_value}.xlsx'
    #     precision_data = final_filtered_data[final_filtered_data[' Precision'] == precision_value]
    #     precision_data.to_excel(output_file, index=False)
    #     print(f"Filtered data for precision '{precision_value}' saved to {output_file}")

golden_config_maker(csv_file_path= "C:\\Users\\GSANDEEX\\OneDrive - Intel Corporation\\Documents\\AI-ML runs\\Sienna-test\\Quanta-48C\\quanta-18-AI_resnet50v1_5_custom_run.csv")
print("All filtered data saved successfully!")



