import requests
from bs4 import BeautifulSoup
from canvasapi import Canvas
from dotenv import load_dotenv
import os

load_dotenv()

access_token = os.getenv("access_token")
dashboard_url = os.getenv("dashboard_url")
canvas = Canvas(dashboard_url, access_token)

# url = "https://canvas.instructure.com/api/v1/courses?access_token=13096~UjBWGYwxbFt0ZYLucGBwhTPEWS0eRZD04TxA3GU1wVxHFYeOMIAzWa8aX3ZJoFfL"
response = requests.get(dashboard_url, params=access_token)
raw_content = response.content
# format = "html"
format = "json"
# soup = BeautifulSoup(raw_content, 'html.parser')

content = open(f"raw_content.{format}", "w")
content.write(raw_content.decode("utf-8"))
content.close()

print(response)

# print(soup)