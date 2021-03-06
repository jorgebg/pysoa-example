# PySOA Example

## Requirements

- [PySOA](https://github.com/eventbrite/pysoa)
- [Redis](https://redis.io/)

## Install

```
pip3 install pysoa
```

## Usage

### Shell A
```
python3 -m server -s settings
```


### Shell B
```
python3 client.py
```

## Under the hood


Start `redis-cli monitor` before running the server and the client to see the exchanged messages.

They both use `RPUSH` for sending the messages and `BLPOP` for reading them:

![BLPOP/RPUSH example](blpop-rpush.gif)


## Conformity

If you want to validate the request and the response, follow these steps:

- Install Conformity: `pip3 install conformity`
- Update `server.py`:

```python
from conformity import fields

# ...

class SquareAction(Action):
    request_schema = fields.Dictionary({
        'number': fields.Float(),
    })

    response_schema = fields.Dictionary({
        'square': fields.Float(),
    })
    # ...
```

## References

- [BLPOP](https://redis.io/commands/BLPOP)
- [RPUSH](https://redis.io/commands/RPUSH)
- [PySOA](https://github.com/eventbrite/pysoa)
- [Conformity](https://github.com/eventbrite/conformity)
