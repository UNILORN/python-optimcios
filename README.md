# Optim CIOS APIv1 Python Package

## usage

Clone from GitHub

`git clone https://github.com/UNILORN/python-optimcios`

Execute the following command.

```bash

$ cd python-optimcios
$ make

```


## Sample Codes

```python

from python_optimcios import messaging

channel_id = ""
access_token = ""
cios = messaging.messaging('ws://0.0.0.0:9999',channel_id,access_token)

cios.connection()

cios.sendMessage('Hello world')

mes = cios.receiveMessage()
print(mes)

```


