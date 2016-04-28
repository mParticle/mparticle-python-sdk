# mparticle.EventsApi

All URIs are relative to *https://s2s.mparticle.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_upload_events**](EventsApi.md#bulk_upload_events) | **POST** /bulkevents | Send events to mParticle
[**upload_events**](EventsApi.md#upload_events) | **POST** /events | Send events to mParticle


# **bulk_upload_events**
> bulk_upload_events(body)

Send events to mParticle



### Example 
```python
import time
import mparticle
from mparticle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
mparticle.configuration.api_key = 'YOUR_USERNAME'
mparticle.configuration.api_secret = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mparticle.EventsApi()
body = [mparticle.Batch()] # list[Batch] | Up to 100 Batch objects

try: 
    # Send events to mParticle
    api_instance.bulk_upload_events(body)
except ApiException as e:
    print "Exception when calling EventsApi->bulk_upload_events: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Batch]**](Batch.md)| Up to 100 Batch objects | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_events**
> upload_events(body)

Send events to mParticle



### Example 
```python
import time
import mparticle
from mparticle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
mparticle.configuration.api_key = 'YOUR_USERNAME'
mparticle.configuration.api_secret = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mparticle.EventsApi()
body = mparticle.Batch() # Batch | Batch of event data

try: 
    # Send events to mParticle
    api_instance.upload_events(body)
except ApiException as e:
    print "Exception when calling EventsApi->upload_events: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Batch**](Batch.md)| Batch of event data | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

