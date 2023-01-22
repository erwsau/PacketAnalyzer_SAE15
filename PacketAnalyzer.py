import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

import re
import seaborn as sns

# Read packets from a pcap file
packets = []
with open('D:\Cours\SAE15\SAE\DumpFile.txt', 'r') as f:
    # Browse each line of the file

    packet_data = []
    for line in f:

        if "IP" in line:
            destination = 0
            # Use a regular expression to extract the desired information
            time_match = re.search(r'(\d{2}:\d{2}:\d{2}\.\d{6})', line)
            protocol_match = re.search(r'(\w+):', line)
            source_match = re.search(r'(\d{3}-\d{3}-\d{3}-\d{3}\.\w+\.\w+\.\w+) >', line)
            if source_match:
                source = source_match.group(1)
            else:
                source_match = re.search(r'([\w-]+\.[\w-]+\.[\w-]+\.[\w-]+\.[\w-]+) >', line)
                if source_match:
                    source = source_match.group(1)
                else:
                    source_match = re.search(r'([\w-]+\.[\w-]+\.[\w-]+\.[\w-]+) >', line)
                    if source_match:
                        source = source_match.group(1)
                    else:
                        source_match = re.search(r'([\w-]+\.[\w-]+) >', line)
                        if source_match:
                            source = source_match.group(1)
                        else:
                            source_match = re.search(r'(\d+\.\d+\.\d+\.\d+) >', line)
                            if source_match:
                                source = source_match.group(1)


            destination_match = re.search(r'([\w-]+\.[\w-]+\.[\w-]+\.[\w-]+):', line) or re.search(r'([\w-]+\.[\w-]+):', line) or re.search(r'(\d+\.\d+\.\d+\.\d+) :', line)

            # Check if a match was found for each information
            if time_match:
                time = time_match.group(1)
            else:
                time = None
            if protocol_match:
                protocol = protocol_match.group(1)
            else:
                protocol = None
            if source_match:
                source = source_match.group(1)
            else:
                source = None
            if destination_match:
                destination = destination_match.group(1)
            else:
                destination = None
            if all(val is not None for val in [time, protocol, source, destination]):

                packet_data.append([time, protocol, source, destination])




# Initialize an empty dictionary to store the packet counts for grouped IPs
grouped_ip_counts = {}

# Iterate through the packet data
for packet in packet_data:
    # Get the source IP address
    source_ip = packet[2]
    # group the IP address
    grouped_ip = ".".join(source_ip.split(".")[:3]) + ".*"
    # Check if the IP address is already in the dictionary
    if grouped_ip in grouped_ip_counts:
        # If it is, increment the count
        grouped_ip_counts[grouped_ip] += 1
    else:
        # If not, add the IP address to the dictionary with a count of 1
        grouped_ip_counts[grouped_ip] = 1
    
    


# Sort the dictionary by value
sorted_ip_counts = sorted(grouped_ip_counts.items(), key=lambda x: x[1], reverse=True)

# Print the top 10 IP addresses
for ip, count in sorted_ip_counts[:10]:
    print(f"IP address {ip} sent {count} packets")
    
# Plot the top 10 IP addresses that sent the most packets
df = pd.DataFrame(sorted_ip_counts, columns=['IP', 'Packets'])

# Create a stacked bar chart of the top 10 IP addresses with seaborn
df = df.sort_values(by='Packets',ascending=False)
df = df.head(10)


bars = sns.barplot(x='IP', y='Packets', data=df, label='IP addresses')

# Create a list of the bars
bar_list = bars.patches

# Add labels to the bars
for i in range(len(bar_list)):
    bar_list[i].set_label(df['IP'].iloc[i])

# Create the legend
plt.legend(handles=bar_list)
plt.xticks(rotation=90)
plt.legend(df['IP'])

plt.savefig("ip")
