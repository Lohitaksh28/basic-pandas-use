import pandas as pd
data = pd.read_csv('cpuStats.csv')

# Calculate average CPU usage
print(f"Average CPU usage: {data['cpu_usage']. mean() :.2f}%")

# Filter high CPU usage days and high memory usage days
high_cpu_days = data[data[ 'cpu_usage' ] > 80]
high_memory_days = data[data['memory_usage'] > 80]

print("High CPU usage days:")
print(high_cpu_days)

print("High memory usage days:")
print(high_memory_days)