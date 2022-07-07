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
```
CREATE TABLE IF NOT EXISTS `habi_db`.`like` (
  `idlike` INT NOT NULL,
  `auth_user_id` INT(11) NOT NULL,
  `property_id` INT(11) NOT NULL,
  PRIMARY KEY (`idlike`),
  INDEX `fk_like_auth_user1_idx` (`auth_user_id` ASC) VISIBLE,
  INDEX `fk_like_property1_idx` (`property_id` ASC) VISIBLE,
  UNIQUE KEY `my_uniq_id` (`auth_user_id`,`property_id`)
  CONSTRAINT `fk_like_auth_user1`
    FOREIGN KEY (`auth_user_id`)
    REFERENCES `habi_db`.`auth_user` (`id`)
    ON DELETE CASCADE
  CONSTRAINT `fk_like_property1`
    FOREIGN KEY (`property_id`)
    REFERENCES `habi_db`.`property` (`id`)
    ON DELETE CASCADE
)
```