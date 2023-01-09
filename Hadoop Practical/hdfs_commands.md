
#### HDFS is the primary or major component of the Hadoop ecosystem which is responsible for storing large data sets of structured or unstructured data across various nodes and thereby maintaining the metadata in the form of log files.
-----

# General Shell Commands

# LOCAL FILE SYSTEM

- To list the file names in current directory  
  ```
  ls
  ```
- Optional switches for *ls* command:
  - To use long listing format 
    ```
    ls -l
    ```

  - To sort the list by modification time, newest first
    ```
    ls -t
    ```

  - To reverse order while sorting
    ```
    ls -r
    ```

- To create a new directory
```
mkdir directory_name
```

- Copy file from source to destination
```
cp data.csv destination_directory
```

- Move file from source to destination
```
mv data.csv destination_directory
```

- Remove/Delete the file
```
rm data.csv

```

- Remove/Delete the folder
```
rm directory_name

```
# HADOOP DISTRIBUTED FILE SYSTEM (HDFS)

- LISTING ROOT DIRECTORY

```
hadoop fs -ls /
```

- LISTING DEFAULT TO HOME DIRECTORY

```
hadoop fs -ls
```

- CREATE A DIRECTORY IN HDFS

```
hadoop fs -mkdir /hadoop-user
```

- COPY FROM LOCAL FS TO HDFS

```
hadoop fs -copyFromLocal trees.csv /hadoop-user
```

- COPY TO HDFS TO LOCAL FS

```
hadoop fs -copyToLocal /hadoop-user/trees.csv .
```

```
hadoop fs -ls /hadoop-user
```

- COPY A FILE FROM ONE FOLDER TO ANOTHER

```
hadoop fs -cp /hadoop-user/trees.csv /hadoop-user2
```

## URL to view data in UI:

Name Node - <your_app_name>.ineuron.app:9870

Data Node - <your_app_name>.ineuron.app:9864

Hadoop Clutser - <your_app_name>.ineuron.app:8088/cluster

















# In hdfs file system / is the root

# Command to check the files inside root hdfs directory
hadoop fs -ls /

# Command to create directory in hdfs
hadoop fs -mkdir /input_data


# Copy data from local file system to Hdfs
hadoop fs -put test_demo/trees.csv /input_data

# Copy from HDFS path to local file system
hadoop fs -copyToLocal /input_data/trees.csv ./

# Command to execute map reduce code
hadoop jar hadoop-streaming-2.4.0.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /test/demo.txt -output /output
