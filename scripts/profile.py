import pandas as pd
from ydata_profiling import ProfileReport
import zipfile
import os

zip_file_path = './wine.zip'
csv_file_name = 'wine.data' 

# Unzip the file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('data')

extracted_csv_path = os.path.join('data', csv_file_name)

# Read the dataset into a DataFrame
df = pd.read_csv(extracted_csv_path)

feature_names = [
    "Class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium",
    "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
    "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"
]

df.columns = feature_names

# Generate the profiling report
profile = ProfileReport(df, title='Profiling Report', explorative=True)

# Ensure the directory for the report exists
report_dir = 'profiling'
if not os.path.exists(report_dir):
    os.makedirs(report_dir)

# Write the report to an HTML file
report_path = os.path.join(report_dir, 'report.html')
profile.to_file(report_path)

print(f'Profile report written to {report_path}')


