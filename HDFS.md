
# HDFS - Hadoop Distributed File System

## Name Node
- It acts like a master node & manages Data Node
- It maintains the metadata of all the files in the cluster. Example: Location of data blocks, file size, location of replicated data

## Data Node
- It is a slave node
- The actual data is stored on Data Nodes
- Data Nodes will also help in computing
- Data Nodes sends heartbeat to Name Node periodically to report the overall health of the system

# Block
- Smallest unit of physical memory where data is stored
- Default size of a block in Hadoop 2.x is 128MB

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
