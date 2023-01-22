# Packet Analyzer

This code is used to extract and analyze packet data from a pcap file. It reads packets from a file and uses regular expressions to extract the following information from each packet:
- Time
- Protocol
- Source IP address
- Destination IP address

The extracted information is then stored in a list of lists, where each sublist contains the information for a single packet.

The code then uses the pandas and seaborn libraries to create a dataframe and visualize the extracted information. It also uses the matplotlib library to create plots.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have the following python packages installed:
- pandas
- matplotlib
- seaborn
- re

You can install these packages using pip by running the following command:

pip install pandas matplotlib seaborn re

### Running the code

1. Clone this repository to your local machine using `https://github.com/<username>/Packet-Analyzer.git`
2. Open the `Packet-Analyzer` folder and locate the file `PacketAnalyzer.py`
3. In the `PacketAnalyzer.py` file, change the file path on line 15 to the location of your pcap file.
4. Run the code by executing the command `python PacketAnalyzer.py` in the terminal

## Authors

* - erwsau (https://github.com/erwsau)
