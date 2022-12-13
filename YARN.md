# YARN: Yet Another Resource Negotiator
- YARN was introduced in Hadoop 2.X
- In Hadoop 1.X MapReduce used to take care of Resource Management

## YARN Architecture
<img src="https://www.edureka.co/blog/wp-content/uploads/2018/06/Components-of-YARN-1.png">

## Steps for Resource Allocation
1. Client will send a job submission request to Resource Manager.
2. Resourec Manager will create one container on a random Data Node & will start Application Master service in it.
3. Each job will have **separate and only one** Application Master.
4. Application Master will request to Resource Manager to create one or more containers based on the complexity of job.
5. Resourec Manager will create required number of containers on different Data Nodes.
6. Containers will process actual blocks of data.

## Resourec Manager
- Authority to allocate resources
- Smartly optimizes the cluster utilization like keeping all resources in use all the time against various constraints.

## Components of Resourec Manager
1. **Scheduler:**
	- Responsibel for allocating resources 
	- Performs scheduling of jobs based on resource requirement
	- Maintains queues as well

2. **Application Master:**
	- Responsible for job submission
	- Negotiates no. of containers from Resource Manager
	- Also manages running application

3. **Node Manager:**
	- Takes care of individual nodes in Hadoop cluster
	- Manages jobs & it's workflow
	- Sends report & heartbeat with health status to the Resourec Manager
	- Also Monitors resource(CPU, Memory) usage of individual container

4. **Container:**
	- Small virtual space in physical machine which consists of some CPU cores, memory & network bandwidth
