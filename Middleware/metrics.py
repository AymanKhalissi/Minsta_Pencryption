# metrics.py

import csv

def calculate_metrics(start_time, end_time, user_data, encryption_start_time, encryption_end_time):
    overhead = end_time - start_time
    encryption_speed = len(user_data) / (encryption_end_time - encryption_start_time)
    return overhead, encryption_speed

def save_metrics_to_csv(metrics, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Overhead', 'Original Table Size', 'Encrypted Table Size', 'Encryption Speed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(metrics)

def log_and_save_metrics(overhead, original_table_size, encrypted_table_size, encryption_speed, filename):
    metrics = {
        'Overhead': overhead,
        'Original Table Size': original_table_size,
        'Encrypted Table Size': encrypted_table_size,
        'Encryption Speed': encryption_speed
    }

    save_metrics_to_csv(metrics, filename)

    print(f"Data transfer completed in {overhead} seconds")
    print(f"Original table size: {original_table_size} rows")
    print(f"Encrypted table size: {encrypted_table_size} rows")
    print(f"Encryption speed: {encryption_speed} rows/second")