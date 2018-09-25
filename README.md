# Optim CIOS APIv1 Python Package

## usage

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
scope = ""

access_token = auth.getRefreshAccessToken(
    scope=scope,
    refresh_token="REFRESH_TOKEN"
)

print(access_token)
```

### Messaging

`In Development`

## Development

### Required

```

Python >= 3.6.0
pip >= 10.0.1
npm >= 3.10.10

```

**※Caution**

`wscat` It will automatically be installed globally.

### It work

Please install with the following command.

```bash

$ make inst-dev

```

Please execute the following command while working

```bash

$ make dev

```