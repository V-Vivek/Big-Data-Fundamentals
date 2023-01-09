
#### HDFS is the primary or major component of the Hadoop ecosystem which is responsible for storing large data sets of structured or unstructured data across various nodes and thereby maintaining the metadata in the form of log files.
-----

# General Shell Commands

# LOCAL FILE SYSTEM

- To change the current directory
```
cd directory_path
```

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

- LISTING ROOT DIRECTORY (/)
```
hadoop fs -ls /
```

- CREATE A DIRECTORY IN HDFS
```
hadoop fs -mkdir /directory_name
```

- COPY FROM LOCAL FS TO HDFS
  - USING *copyFromLocal*
  ```
  hadoop fs -copyFromLocal data.csv /directory_name
  ```
  - USING *put*
  ```
  hadoop fs -put data.csv /directory_name
  ```

- COPY FROM HDFS TO LOCAL FS
```
hadoop fs -copyToLocal /directory_namer/data.csv destination_directory
```

- COPY A FILE FROM ONE FOLDER TO ANOTHER INSIDE HDFS

```
hadoop fs -cp /directory_namer/data.csv /destination_directory_name
```

# Execute word count code on Hadoop

- Write a mapper logic
```
mapper.py
```

- Write a reducer logic
```
reducer.py
```

- Use Hadoop Streaming
  - Hadoop Streaming is a utility that allows users to create and run MapReduce jobs with any executables as the mapper and/or the reducer.
  - e.g. Python scripts or compiled binaries.
  - The Hadoop Streaming jar file ***hadoop-streaming-2.4.0.jar*** is a Java archive file that contains the classes and resources needed to run Hadoop Streaming jobs.
  - Hadoop Streaming is a flexible and powerful tool that allows users to run MapReduce jobs using any executables, without the need to write Java code.

-  Command to execute map reduce code
  - Method #1
  ```
  hadoop jar hadoop-streaming-2.4.0.jar -files mapper.py, reducer.py -mapper mapper.py -reducer reducer.py -input /path_of_input file -output /output
  ``` 
  
  - Method #2
  ```
  hadoop jar hadoop-streaming-2.4.0.jar \
  -input input_dir \
  -output output_dir \
  -mapper mapper.py \
  -reducer reducer.py
  ```



