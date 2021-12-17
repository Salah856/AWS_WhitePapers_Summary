# Designing MQTT Topics for AWS IoT Core


- This whitepaper focuses on best practices for MQTT topic design in Amazon Web Services (AWS) Internet of Things (IoT). 

- It covers how developing an optimal MQTT topic schema can improve the overall architecture and efficiency of your IoT solutions. 

- It does so by providing greater visibility into cloud to device communication, 
- providing more fine-grained security permissions, and enhancing integration options with other AWS IoT Core services. 

- This whitepaper is intended for technical architects, IoT cloud engineers, and application architects. 


### MQTT communication patterns

- IoT applications support multiple communication scenarios, such as device-to-device, device-to-cloud, loud-to-device, and device-to-or-from-users. 

- Although the range of patterns can significantly vary, a ajority of MQTT communication models derive from three MQTT patterns: 
        
        --  point-to-point, broadcast, and fan-in.


#### Point-to-point

A point-to-point communication pattern is one of the basic building blocks of how devices commonly send and receive messages in MQTT. 

Two devices use a single MQTT topic as the communication channel.

The device that receives the event subscribes to an MQTT topic. 

The thing that sends the message publishes to the same known MQTT topic. 

This approach is common in smart home scenarios where an end user receives updates about the thing in the home. 

In the following example, the room occupancy publishes a message on a topic subscribed to by an application running on digital display outside screening room.

#### Broadcast

Broadcast patterns are used for one-to-many messaging. 

The broadcast pattern sends the same message to a large fleet of devices. 

In a broadcast, multiple devices subscribe to the same MQTT topic, and the sender publishes a message to that topic. 

A typical use of a broadcast pattern is to send a notification to devices based on the category or group of the device. 

For example, a weather station transmits a broadcast message based on a topic based on its geolocation.


#### Fan-In

The fan-in pattern is a many-to-one communication pattern and can be thought of as the reverse of the broadcast pattern.

Multiple devices publish on a shared or similar topic with a single subscriber to that topic. 

With the fan-in pattern, the subscriber may use wildcards as the publishers all use a similar but unique MQTT topics. 

The fan-in pattern is commonly used to aggregate telemetry data.

The AWS IoT Rules Engine uses a wildcard subscription to receive the messages and route them to an Amazon Kinesis stream. 














<a href="https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.pdf#designing-mqtt-topics-aws-iot-core
"> Ref </a> 











