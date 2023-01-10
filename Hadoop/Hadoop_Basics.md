
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

# Hadoop
- Distributed computation framework  
- Specially designed for batch data processing  

## Hadoop components
1. ***HDFS*** -> Storage 
2. ***Map-Reduce*** -> Processing
3. ***YARN*** -> Resource Management

## Basic terminologies
- ***Distributed Storage***: Breaks data into small blocks & stores it into different machines  
- ***Distributed Computation***: Process multiple parts of data on different machines at the same time  
- ***Commodity Hardware***: Simple machine which has storage & processing capability  
- ***Cluster***: Combination of multiple commodity hardware
