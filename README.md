<img src="http://static.mparticle.com/sdk/logo.svg" width="280">

## Python SDK

This is the mParticle Python client SDK - use it to send your data to the [mParticle platform](https://www.mparticle.com/) and off to 80+ app services.

### Requirements.

Python 2.7 and later.

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
from mparticle import AppEvent, SessionStartEvent, SessionEndEvent, Batch

batch = Batch()
batch.environment = 'development'

app_event = AppEvent('Hello World', 'navigation')
batch.events = [SessionStartEvent(), app_event, SessionEndEvent()]

configuration = mparticle.Configuration()
configuration.api_key = 'REPLACE WITH API KEY'
configuration.api_secret = 'REPLACE WITH API SECRET'
api_instance = mparticle.EventsApi(configuration)

# synchronous
try: 
    api_instance.upload_events(batch)
    #or api_instance.bulk_upload_events([batch_1, batch_2])
except mparticle.rest.ApiException as e:
    print "Exception while calling mParticle: %s\n" % e


# asynchronous, specifying your callback function
# api_instance.upload_events(batch, callback=callback_function)
```

### License

[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
