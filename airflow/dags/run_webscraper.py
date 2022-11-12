from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.docker_operator import DockerOperator


default_args = {
    'owner'                 : "Airflow",
    'description'           : "Runs Webscrapers",
    'depend_on_past'        : False,
    'start_date'            : datetime(2022, 1, 1),
    'retries'               : 1,
    'retry_delay'           : timedelta(minutes=5)
}


def make_scraper_task(scraper):
    return DockerOperator(
        task_id=f"run-webscraper-{scraper}",
        image="domogordon/development:latest",  # Update this line if you're using your own
        api_version="auto",
        auto_remove=True,
        command="python main.py",
        environment={"SCRAPER": scraper},
        docker_url="tcp://docker-proxy:2375",
        network_mode="bridge"
    )


with DAG("run_webscrapers", default_args=default_args, schedule_interval="@once", catchup=False) as dag:
    webscraper_two_lincoln = make_scraper_task("two_lincoln")
    webscraper_bravern = make_scraper_task("bravern")

    [webscraper_two_lincoln, webscraper_bravern]
    
    
    
    
    