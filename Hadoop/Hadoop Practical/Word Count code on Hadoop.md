# Execute word count code on Hadoop

## Write a mapper logic
```
mapper.py
```

## Write a reducer logic
```
reducer.py
```

## Use Hadoop Streaming
  - Hadoop Streaming is a utility that allows users to create and run MapReduce jobs with any executables as the mapper and/or the reducer.
  - e.g. Python scripts or compiled binaries.
  - The Hadoop Streaming jar file ***hadoop-streaming-2.4.0.jar*** is a Java archive file that contains the classes and resources needed to run Hadoop Streaming jobs.
  - Hadoop Streaming is a flexible and powerful tool that allows users to run MapReduce jobs using any executables, without the need to write Java code.

##  Command to execute map reduce code
  - Method #1
  ```
  hadoop jar hadoop-streaming-2.4.0.jar -input /vivek/input/demo.txt -output /vivek/output -mapper "python mapper.py" -reducer "python reducer.py" -file mapper.py -file reducer.py
  ``` 
  
  - Method #2
  ```
  hadoop jar hadoop-streaming-2.4.0.jar \
  -input /vivek/input/demo.txt \
  -output /vivek/output \
  -mapper "python mapper.py" \
  -reducer "python reducer.py" \
  -file mapper.py \
  -file reducer.py
  ```
  
## Assumptions & Considerations
- For above example I have created a directory named vivek. Inside it I have created one more directory named input & I have kept the demo.txt file in it.
- hadoop-streaming-2.4.0.jar, mapper.py & reducer.py should be located in the local file system(Not in HDFS).
- demo.txt should be located in HDFS in the path given in ```-input``` tag.
- The output folder should not be created by user or else an error will be generated. It will be auto created as per path given in ```-output``` tag.

## Output
- Run below command to check the output file
```
hadoop fs -cat /vivek/output/part-00000
```
- Result will be displayed as below
```
bye     164
hello   82
hi      41
nice    41
ok      82
tata    41
```
