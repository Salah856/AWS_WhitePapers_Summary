
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
- 
