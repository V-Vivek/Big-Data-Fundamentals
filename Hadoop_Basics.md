
## Big Data

- Data which cannot be handeled by traditional databases.
- Any data related problem that satisfies 5V's criteria

## 5V's of Big Data

1. ***Volume***: Huge amount of data(Hundered's of GB, TB, PB, ...)
2. ***Variety***: Different formats of data
	- ***Structured Data***: Where schema is fixed. Example: Relational data  
	- ***Semi-structured Data***: Where schema is flexible. Example: JSON, XML  
	- ***Unstructured Data***: Where schema doesn't exist. Example: image, audio, video  
3. ***Velocity***: Speed of data generation
	- ***Batch processing***: Data ingested after specific time intervals. Example: Electricity bill, Credit card bill
	- ***Real Time processing***: Data is ingested in near real time. Example: Live gameplay, content streaming
4. ***Value***: Extracting meaningful information  
5. ***Veracity***: Related to uncertainity in the data

## Hadoop
- Distributed computation framework  
- Specially designed for batch data processing  

1. ***Distributed Storage***: Breaks data into small blocks & stores it into different machines  
2. ***Distributed Computation***: Process multiple parts of data on different machines at the same time

## Commodity Hardware
Simple machine which has storage & processing capability

## Cluster
Combination of multiple commodity hardware

## Replication Management

## Rack Awareness

## HDFS Write Request
- 3 steps of HDFS write request:
1. HDFS Client contacts Name Node to get the IP addresses of Data Nodes in which data will be written.

## High Availability or Fault Tolerence
- It is a method to handle the failure/breakdown of Name Node
- Higgly Available -> Very very less downtime

#### 2 ways to achieve High Availability in Hadoop:
1. Secondary Name Node
- 

2. Standby Name Node
- Duplicate of Name Node
- Works in Active-Passive mode

### Name node maintains below information
1. **FS-Image** - It contains complete state of the file system since the start of Name Node
2. **Edit Logs** - It contains the recent modifications made to the file system
