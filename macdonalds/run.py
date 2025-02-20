import uvicorn
from multiprocessing import Process
import subprocess
from api_server.main import app
from api_server.utils import FILE_PATH
from macdonalds.macdonalds.spiders.mac import logger


def run_spider():
    subprocess.run(
        ["scrapy", "crawl", "mac", "-O", FILE_PATH], 
        check=True,
        )


def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    logger.info("Start scraping...")
    spider_process = Process(target=run_spider)
    spider_process.start()
    spider_process.join()

    logger.info("Starting FastAPI server...")
    run_server()