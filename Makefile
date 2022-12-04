#################################################
#                  AIRFLOW                      #
#################################################

start-airflow:
	@docker-compose up postgres redis airflow-webserver airflow-scheduler airflow-worker airflow-triggerer airflow-init airflow-cli flower docker-proxy



#################################################
#                  SELENIUM                     #
#################################################
start-selenium:
	@docker-compose up selenium-hub chrome


#################################################
#                  BACKEND                      #
#################################################
start-backend:
	@docker-compose up backend backend_db 

migrations:
	@docker-compose run backend python manage.py makemigrations
	@docker-compose run backend python manage.py migrate;

#################################################
#                  WEBSCRAPER                   #
#################################################
build-ws:
	@cd webscrapers; docker build . -t domogordon/development:latest;

push-ws:
	@make build-ws
	@cd webscrapers; docker push domogordon/development:latest;

run-ws:
	@make build-ws;
	@cd webscrapers; docker run -e SCRAPER=$(scraper) domogordon/development:latest python main.py


