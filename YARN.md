# YARN: Yet Another Resource Negotiator

## Steps for Resource Allocation
1. Client will send a job submission request to resource manager.
2. Resourec Manager will create one container on a random Data Node & will start Application Master service in it.
3. Each job will have **separate and only one** Application Master.
4. Application Master will request to Resource Manager to create more containers based on the complexity of job.
5. Resourec Manager will create required number of containers on different Data Node.
6. Containers will process actual blocks of data.

## Resourec Manager
- Authority to allocate resources
- Smartly optimizes the cluster utilization like keeping all resources in use all the time against various constraints.

#### Components of Resourec Manager
- **Scheduler**
1. Responsibel for allocating resources 
2. Performs scheduling of jobs based on resource requirement
3. Maintains queues as well

- **Application Master**
1. Responsible for job submission
2. Negotiates no. of containers from Resource Manager
3. Also manages running application

## Node Manager
- Takes care of individual nodes in Hadoop cluster
- Manages jobs & it's workflow
- Sends report & heartbeat with health status to the Resourec Manager
- Also Monitors resource(CPU, Memory) usage of individual container

## Container
Small virtual space in physical machine which consists of some CPU cores, memory & network bandwidth