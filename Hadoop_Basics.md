## Replication Management

## Rack Awareness

## HDFS Write Request
- 3 steps of HDFS write request:
1. HDFS Client contacts Name Node to get the IP addresses of Data Nodes in which data will be written.

## High Availability or Fault Tolerence
- It is a method to handle the failure/breakdown of Name Node

#### 2 ways to achieve High Availability in Hadoop:
1. Secondary Name Node
2. Standby Name Node

- Name node maintains below information
1. **FS-Image** - It contains complete state of the file system since the start of Name Node
2. **Edit Logs** - It contains the recent modifications made to the file system