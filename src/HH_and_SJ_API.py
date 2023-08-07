import requests
import os
from abc import ABC, abstractmethod


class AbstractJobAPI(ABC):
    """
    Абстрактный класс для API сайтов с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, keyword: str):
        """
        Получает список вакансий по заданному ключевому слову.

        Параметры:
            keyword (str): Ключевое слово для поиска вакансий.
        """
        pass


class SJ_API(AbstractJobAPI):
    """
    Класс для работы с API сайта SuperJob.
    """

    SECRET_KEY = os.getenv('SJ_API_KEY')

    def get_vacancies(self, keyword: str):
        """Получает список вакансий с сайта SJ по заданному ключевому слову."""
        params = {
            "keyword": keyword,
            "count": 100,
            "no_agreement": 1
        }

        headers = {
            'X-Api-App-Id': self.SECRET_KEY
        }
        url = f'https://api.superjob.ru/2.0/vacancies/'
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            response_data = response.json()
            vacancies = response_data.get('objects', [])
            return vacancies
        else:
            print(f"Запрос не выполнен с кодом состояния: {response.status_code}")
            return []


class HH_API(AbstractJobAPI):
    """Класс для работы с API сайта HeadHunter."""

    def get_vacancies(self, keyword: str):
        """Получает список вакансий с сайта HeadHunter по заданному ключевому слову."""
        params = {
            "text": keyword,
            "per_page": 100,
            "only_with_salary": True
        }

        url = f'https://api.hh.ru/vacancies'
        response = requests.get(url, params=params)

        if response.status_code == 200:
            response_data = response.json()
            vacancies = response_data.get('items', [])
            return vacancies
        else:
            print(f"Запрос не выполнен с кодом состояния: {response.status_code}")
            return []
