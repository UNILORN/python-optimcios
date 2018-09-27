# Optim CIOS APIv1,v2 Python Package

## Usage

Clone from GitHub.

`git clone https://github.com/UNILORN/python-optimcios`

Execute the following command.

```bash

$ cd python-optimcios
$ make

```


## CIOSv1 Sample Codes In Messaging

```python

from python_optimcios.v1 import messaging

channel_id = ""
access_token = ""
cios = messaging.Messaging('ws://0.0.0.0:9999',channel_id,access_token)

cios.connection()

cios.sendMessage('Hello world')

mes = cios.receiveMessage()
print(mes)

```

## CIOSv2 Sample Codes

### Authorization

```python
from python_optimcios.v2 import authorization

auth = authorization.Authorization(
            auth_uri="AUTH_URI",
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
            log=True
        )

access_token = auth.getRefreshAccessToken(
    scope="SCOPE",
    refresh_token="REFRESH_TOKEN"
)

print(access_token)
```

### Datastore

```python
from python_optimcios.v2 import authorization, datastore

auth = authorization.Authorization(
            auth_uri="AUTH_URI",
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
            log=True
        )
access_token = auth.getRefreshAccessToken(
    scope="SCOPE",
    refresh_token="REFRESH_TOKEN"
)

datastore = datastore.Datastore(
            access_token=access_token,
            api_uri="API_URI",
            log=True
        )

# Datastore Channel List
datastore.getListChannel()

# Datastore Channel Info
datastore.getChannel(channel_id="CHANNEL_ID")

# Datastore Object List
datastore.getListObjects(channel_id="CHANNEL_ID")

# Datastore Create Object
datastore.postObject(channel_id="CHANNEL_ID",data="POST_DATA_JSON")

# Datastore Object Info
datastore.getObject(channel_id="CHANNEL_ID",object_id="OBJECT_ID")

# Datastore Latest Object Info
datastore.getObject(channel_id="CHANNEL_ID")

# Datasotre Delete Object
datastore.deleteObject(channel_id="CHANNEL_ID",object_id="OBJECT_ID")

```

### Messaging

`In Development`


## Development

### Required

```

Python >= 3.6.0
pip >= 10.0.1

```

### It work

1. Please install with the following command.

    ```bash
    
    $ make inst-dev
    
    ```

2. Change the .env file

3. Run the test and make sure there are no errors

    ```bash
    $ python3 setup.py test
    ```