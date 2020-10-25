#!/usr/bin/env python
from __future__ import print_function
import time
import fleet_manager_client
from fleet_manager_client.rest import ApiException
from pprint import pprint

config = fleet_manager_client.Configuration()
config.host = '127.0.0.1:8080'

# create an instance of the API class
api_instance = fleet_manager_client.ResultApi(fleet_manager_client.ApiClient(config))

# Create header 
header = fleet_manager_client.Header()
header.id = 3  # Robot ID (robot number 3)
header.timestamp = int(time.time())  # Unix timestamp

# Create position (nominal position of the obstacle relative to the world frame (in meters))
position = fleet_manager_client.Position()
position.x = 5.348  # x component of position in meters [m]
position.y = 7.442  # y component of position in meters [m]

# Create size
size = 0.552  # nominal size of the obstacle in meters

# Create velocity (nominal velocity of the obstacle relative to the world frame (in meters per scond))
velocity = fleet_manager_client.Velocity()
velocity.x = -0.354  # x component of velocity in meters per scond [m/s]
velocity.y = 0.126  # y component of velocity in meters per scond [m/s]


# Combine them into the result object:
body = fleet_manager_client.Result(header, position, size, velocity) # Result | Properties of the detected obstacle

try:
    # Send the result of obstacle detection to the fleet manager
    api_instance.send_result(body)
except ApiException as e:
    print("Exception when calling ResultApi->send_result: %s\n" % e)