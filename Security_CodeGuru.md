
# Security in Amazon CodeGuru Profiler


## Introduction

- Amazon CodeGuru is a developer tool that provides recommendations to improve code quality and identify an application’s most expensive lines of code. 
- Customers can integrate CodeGuru into existing software development workflows to automate code reviews during application development. 

- Continuously monitor application performance in production. 
- It uses machine learning to identify critical issues, security vulnerabilities, and hard-to-find bugs during application development to improve code quality.
- It applies the Shared Responsibilty Principle in Security. 

### Profiler high-level flow is:
 1. The profiler agent is instantiated (either within your application or via the CLI)
 2. The agent begins sampling data to send to the service at five-minute intervals
 3. CodeGuru profiler analyzes this data to generate visualizations and actionable recommendations
