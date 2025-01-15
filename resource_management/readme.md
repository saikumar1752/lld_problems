# Resource Management
It’s a system that is able to do efficient task allocation based on the resources available over the infrastructure.


## Problem Statement
You need to design a system that is able to track resources available and do effective allocation of resources based on the availability of resources.
### Different terminology:
- Resource: Can be of different types. For the question purpose, we deal with only the SERVER_INSTANCE type of the resources. Each resource will have some pricing and cpu configuration.
- Data Center: Data center is location based storage of resources. All the resources of the same data center reside in a single geographical location.
- Task: Each task will be executed on a single/multiple SERVER_INSTANCE type of resources. Systems can be asked to execute the task on one (single instance)/multiple resources (multiple instances) simultaneously. Resources can be demanded based on high or low cpu intensive use cases. Whenever a task is submitted the minimum cpu configuration requirement need to be passed. A resource can execute single task at a time. As soon as the task is complete, resources become available for further tasks.


## Requirements P0
All the below requirements are for a given data center.

- Provide an interface to add/delete different types of the resources to the data center.
- Provide an interface to see all the available resources based on the resource type and resource type specific configuration filter. e.g. SERVER_INSTANCE, 8 (cpu)
- Return list of resources available having at least these configurations.
- Provide an interface to see all the allocated resources based on the resource type.e.g. SERVER_INSTANCE
- For a given task, allocate the single resource and execute the task on the resource.
- Resource allocation can be done through different criteria.
    - Criteria 1: allocate the resources having the least price.
    - Criteria 2: allocate the resources having the best execution time.
- For simplicity execution time can be considered inversely proportional to (Cpu)
- Satisfying minimum configuration requirements is important apart from these criteria.
- An interface to check the status of the task, resource allocated, start and end time.
- Handle error scenarios appropriately.
## Requirements P1
- Handle concurrency cases for different scenarios.
- If the resource is not available, Put the task in the waiting queue and wait for the resources to be available. Assign the task in FIFO manner based on their matching configuration to the free resource. You can choose to do a non-blocking task submit in this case.