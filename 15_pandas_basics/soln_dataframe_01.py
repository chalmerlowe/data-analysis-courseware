import pandas as pd

df = pd.read_csv('../universal_datasets/log_file_na.csv', names=['name',
                                                                 'email',
                                                                 'fm_ip',
                                                                 'to_ip',
                                                                 'date_time',
                                                                 'lat',
                                                                 'long',
                                                                 'payload_size'])

payloads = df.payload_size

minimum = payloads.min()
maximum = payloads.max()

print('Max minus Min:', payloads.max() - payloads.min())