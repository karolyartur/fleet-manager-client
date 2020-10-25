# fleet_manager_client.ResultApi

All URIs are relative to */obstacle-detection*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_result**](ResultApi.md#send_result) | **POST** /result | Send the result of obstacle detection to the fleet manager

# **send_result**
> send_result(body)

Send the result of obstacle detection to the fleet manager

### Example
```python
from __future__ import print_function
import time
import fleet_manager_client
from fleet_manager_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fleet_manager_client.ResultApi()
body = fleet_manager_client.Result() # Result | Properties of the detected obstacle

try:
    # Send the result of obstacle detection to the fleet manager
    api_instance.send_result(body)
except ApiException as e:
    print("Exception when calling ResultApi->send_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Result**](Result.md)| Properties of the detected obstacle | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

