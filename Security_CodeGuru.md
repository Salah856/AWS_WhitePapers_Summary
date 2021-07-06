
# Security in Amazon CodeGuru Profiler

- Amazon CodeGuru is a developer tool that provides recommendations to improve code quality and identify an application’s most expensive lines of code. 
- Customers can integrate CodeGuru into existing software development workflows to automate code reviews during application development. 
- Continuously monitor application performance in production. 
- It uses machine learning to identify critical issues, security vulnerabilities, and hard-to-find bugs during application development to improve code quality.
- It applies the Shared Responsibilty Principle in Security. 
- AWS is responsible for managing CodeGuru patching and maintenance of the underlying compute functions. 
- Also, managing service availability, and data encryption in transit and at rest.


### Profiler high-level flow is:
 1. The profiler agent is instantiated (either within your application or via the CLI)
 2. The agent begins sampling data to send to the service at five-minute intervals
 3. CodeGuru profiler analyzes this data to generate visualizations and actionable recommendations


### Data Captured 
- The CodeGuru Profiler agent is responsible for collecting data from a local instance, and sending it to the service endpoint for analysis.
- It does this by using language appropriate mechanisms in either the Java Virtual Machine (JVM), or through Python interfaces.
- The profiler agent does not collect or store your applications source code in any way.
-There are only two types of data the tool collects to send to the profiler service – stack traces and heap summaries.

#### Stack Traces
- A stack trace is a sequence of function or method names in execution. 
- It does not have access to the names or values of function parameters, or the values of variables or application data.
- It sends only method names, and profiling statistics such as CPU, memory, etc. 
- It detects anomalies to recommend improvements in code quality. 

#### Heap summary (JVM only) 
- Heap memory is allocated to JVM and is shared by all threads in the application.
- The profiling agent can collect information about objects in the heap over time and securely share this with the service for analysis.
- Heap summary offers a consolidated view of memory use per object type (e.g. String, int, char[]), and custom types, during a given time frame (usually five minutes). 
- The data is sampled approximately in line with when a full garbage collection is done, and is sent to the CodeGuru Profiler service every 5 minutes. 


### Encryption of Data at Rest
- 





