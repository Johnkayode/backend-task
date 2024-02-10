# Agify Backend Task

## How to Use

## Technologies

The following technologies have been used:

- **Python** - Language
- **FastAPI** - Web Framework
- **Pytest** - Unit tests
- **Redis** - Caching
- **Docker** - Containerization

## API Endpoints

This API implements the following routes:

| **Endpoint**     	| **HTTP method**    | **Description**      	| **Payload** 
|-----------------	|----------------  	 | ---------------
| `/api`     	    | GET           	 | ping the server    	    |
| `/api/human_age`	| POST       	     | retrieve age  guess  	| name: string


### Prerequisites
Make sure you have a modern version of `docker` (>1.13.0) and `docker-compose` installed.

## Build the API image

To build, test and run this API we'll be using `docker-compose`. As such, the first step
is to build the images defined in the `docker-compose.yml` file.

```bash
$ docker-compose build
```

This will build two images:

- `backend-task-app-1` image with REST API.
- `backend-task-redis-1` image with Redis.

## Run the Containers
 
To run the containers previously built, execute the following:
 
```bash
$ docker-compose up -d
```

This will launch two services named `app` (the API) and `redis`. The `app` service will be running on port `8000` on localhost. 
To make sure the app is running correctly open [http://localhost:8000/api](http://localhost:8000/api) in 
your web browser (and/or run `docker-compose logs -f` from the command line). 

## Run the Tests

The tests can be executed with:

```bash
$ docker exec backend-task-app-1 pytest
```

Additional Checks to verify, and possibly correct, the code formatting 
(using `black`) and the ordering and organization of import statements (using `isort`).

```bash
$ docker exec backend-task-app-1 black . --check
$ docker exec backend-task-app-1 isort . --check-only
```

