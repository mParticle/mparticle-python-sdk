<img src="https://static.mparticle.com/sdk/mp_logo_black.svg" width="280">

## Python SDK

This is the mParticle Python client SDK - use it to send your data to the [mParticle platform](https://www.mparticle.com/) and off to 200+ integrations.

### Requirements.

Python 3.5 and later.

### Installation

```sh
python setup.py install
```

Or install from Github via pip:

```sh
pip install git+https://github.com/mparticle/mparticle-python-sdk.git
```

Import the package:

```python
import mparticle
```

#### Manual Installation
If you do not wish to use setuptools, you can download the latest release.
Then, to use the bindings, import the package:

```python
import path.to.mparticle
```

### Usage

```python
import mparticle
from mparticle import AppEvent, SessionStartEvent, SessionEndEvent, Batch

batch = Batch()
batch.environment = 'development'

app_event = AppEvent('Hello World', 'navigation')
batch.events = [SessionStartEvent(), app_event, SessionEndEvent()]

configuration = mparticle.Configuration()
configuration.api_key = 'REPLACE WITH API KEY'
configuration.api_secret = 'REPLACE WITH API SECRET'

# Raise the connection pool size if necessary (defaults to 1)
# configuration.connection_pool_size = 50

api_instance = mparticle.EventsApi(configuration)

# synchronous
try: 
    api_instance.upload_events(batch)
    # or api_instance.bulk_upload_events([batch_1, batch_2])
    # both upload and bulk_upload also have _with_http_info signatures,
    # which will return the HTTP status info and headers, along with the body
except mparticle.rest.ApiException as e:
    print "Exception while calling mParticle: %s\n" % e


# asynchronous, specifying your callback function
def my_callback(response):
    if type(response) is mparticle.rest.ApiException:
        print 'An error occured: ' + str(response)
    else:
        #successful uploads will yield an HTTP 202 response and no body
        print response
        
thread = api_instance.upload_events(batch, callback=my_callback)
```

### License

[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
