# donor-drive-test

### requirements
docker-compose must be installed and compatabile with version 2.2 

### setup
run `docker-compose build`

### running
run `docker-compose up`
connect to `http://localhost:5601`

### Notes on this test

##### Documentation referenced:
for the docker setup I heavily referenced the elasticsearch + kibana docker setup found [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)
for the python script I referenced the python elasticsearch client [here](https://elasticsearch-py.readthedocs.io/en/v8.3.1/)

##### Implementation details:
The 2 ways I majorly differed from the elastic search documentation
1. I added the pythonscript service to the docker-compose
1. I configured Elastic Search and Kibana to use http instead of https to make the communication with the script easier
