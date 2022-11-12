# DOCKER WEBSCRAPER
by Domonique Gordon & Henry Zou
<br>
<br>


## Prerequisites
1. Running Docker
2. `Makefile`


## Getting Started 
1. `make start-airflow`
2. `make start-selenium`
3. `make start-backend`
4. Login to your **[Airflow UI](http://localhost:8080)** 
    ```
        username: airflow
        password: airflow
    ```
5. Turn on the `run_webscrapers` **[DAG](http://localhost:8080/dags/run_webscrapers/grid)**
6. Check **[Django Admin](http://localhost:8000/admin/api/apartments/)** to ensure that the scraped data has been loaded 
```
    username: admin
    password: admin12345
```

