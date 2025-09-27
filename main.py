import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

#first get websites from csv files

def get_website(csv_path: str) -> list[str]:
    websites: list[str] =[]
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])

        return websites
    

def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome


print(get_user_agent())