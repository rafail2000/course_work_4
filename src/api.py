import json
import requests
import os
from abc import ABC, abstractmethod
from config import DATA_PATH


class AbstractAPI(ABC):
    """ Абстрактный класс для HeadHunterAPI """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancy(self, query):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class HeadHunterAPI(AbstractAPI):
    """ Класс HeadHunterAPI для получения и сохранения вакансий """

    def __init__(self):
        self.url = 'http://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User_Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancy = []

    def get_vacancy(self, query_vacancy):
        """ Метод формирования запроса для получения вакансий """
        self.params['text'] = query_vacancy
        vacancy_list = []
        response = requests.get(f'{self.url}?per_page=100&page=0&text={query_vacancy}&search_field=name')
        vacancy = response.json()['items']
        self.vacancy.extend(vacancy)
        self.params['page'] += 1
        vacancy_list = self.vacancy
        return vacancy_list

    def save_json(self, vacancy_json):
        """ Метод для сохранения полученных данных с HeadHunterAPI """
        file_json = os.path.join(DATA_PATH, f'Vacancy_HH.json')
        vacancy_list = []
        for item in vacancy_json:
            if item['salary']:
                salary_from = item['salary']['from']
                salary_to = item['salary']['to']
                if item['salary']['from'] is None:
                    salary_from = 0
                if item['salary']['to'] is None:
                    salary_to = 0
                item_dict = {'vacancy_title': item['name'],
                             'vacancy_link': item['alternate_url'],
                             'vacancy_city': item['area']['name'],
                             'company_name': item['employer']['name'],
                             'salary_from': salary_from,
                             'salary_to': salary_to,
                             'currency': item['salary']['currency'],
                             'vacancy_responsibility': item['snippet']['responsibility'],
                             'vacancy_requirements': item['snippet']['requirement']
                             }
                vacancy_list.append(item_dict)

                with open(file_json, 'w', encoding='utf-8') as file:
                    json.dump(vacancy_list, file, indent=4, ensure_ascii=False)
            return vacancy_list

    def __repr__(self):
        return f'Выполняется подключение к классу {self.__class__.__name__} для получения вакансий с сайта HeadHunter.'
