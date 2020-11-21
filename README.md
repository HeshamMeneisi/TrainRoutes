# Requirements

python 3.9+

Recommended Docker Image: `python:3.9-alpine`

# CLI
```
usage: main.py [-h] [--routes-file ROUTES_FILE] [--origin ORIGIN]
               [--dest DEST]

optional arguments:
  -h, --help            show this help message and exit
  --routes-file ROUTES_FILE
                        points to the csv file containing routes
  --origin ORIGIN       (Optional) origin station name
  --dest DEST           (Optional) destination station name

```

Will start in interactive mode if optional parameters are not provided

# Development

Pycharm configuration is provided. It's recommended to set the default interpreter to Docker (python:3.9-alpine)
