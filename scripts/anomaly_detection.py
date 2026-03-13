import pandas as pd
from datetime import datetime

# Load sample logs (realistic security events)
df = pd.read_json('sample_logs/sample_auth_logs.json')

# Anomaly detection: unusual login times + high failed attempts
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
anomalies = df[
    (df['event'] == 'failed_login') & 
    ((df['hour'] < 6) | (df['hour'] > 22)) & 
    (df['count'] > 5)
]

print(f"🚨 Detected {len(anomalies)} anomalies (off-hour brute force)")
anomalies.to_csv('anomalies_detected.csv', index=False)
print("Report saved: anomalies_detected.csv")
