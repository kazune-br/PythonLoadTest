# Python Load Test

## Requirement Packages
```
$ python3 -m pip install locustio
$ brew install libev
$ brew install mysql-connector-c
$ pip install mysqlclient
```

## How to up
```
$ docker-compose up -d
$ mysql -P 3306 -h 127.0.0.1 -uroot
$ locust --host=http://example.com
```

### REF
```
https://docs.locust.io/en/stable/quickstart.html
https://www.django-rest-framework.org/#quickstart
```