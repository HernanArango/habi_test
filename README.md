# habi_test
To approach the development I will first implement a simple web server, followed by an abstraction layer for database 
access and for the event handler of the application. And finally I will implement the requested logic.

## used Dependencies
- pytest
- mysql.connector
- json
- requests
- urllib3

## Setup

Create virtual enviroment
```shell script
virtualenv env
```

Activate the virtual env with
```shell script
source env/bin/activate
```

## Install
Install the dependencies
```shell script
make install
```

## Usage

Run the app.
```shell script
make run
```

Run the test.
```shell script
make test
```


## Endpoint
### Property
| Method | Path     | Description          |
|--|----------|----------------------------|
| GET |/    | get the properties

### Properties filters
| Filter | Path     | Description          |
|--|----------|----------------------------|
| City |/?city=xxxxx    | Filter by city    |
| Year |/?year=xxxxx | Filter by year          |
| Actual State |/?actual_state=xxxxx | Filter by actual state (pre_venta, en_venta, vendido) |

### Pagination
by default show only 10 result
| Filter | Path     | Description          |
|--|----------|----------------------------|
| Page |/?page=number    | Filter by city    |
| Per Page |/?per_page=number | Filter by year          |


## Point 2 (Likes)
![MER Like](./info/requerimiento2.png?raw=true "MER")

Table relating users and properties is added. Each record will be equivalent to a like.  The like field is also added
in the properties table to keep a total of these and not calculate it every time it is needed.