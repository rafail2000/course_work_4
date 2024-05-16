from abc import ABC, abstractmethod
import requests


class AbstractHeadHunterApi(ABC):
    """ Абстрактный класс AbstractHeadHunterApi """

    @abstractmethod
    def __init__(self, url: str, params: str):
        """ Инициализация пременных в абстрактном классе """
        self.url = url
        self.params = params

    @abstractmethod
    def get_vacancies(self, user_input: str) -> dict:
        """ Абстрактный метод для получения вакансии в формате JSON """
        pass


class HeadHunterApi(AbstractHeadHunterApi):
    """ Абстрактный класс HeadHunterApi """

    def __init__(self, url, params):
        """ Инициализация пременных через метод super """
        super().__init__(url, params)

    def get_vacancies(self, user_input: str) -> dict:
        """ Метод для получения вакансии в формате JSON """
        url = 'https://api.hh.ru/vacancies'
        params = {'text': user_input, 'search_field': 'name', 'per_page': 100}
        response = requests.get(url, params=params)
        return print(response.json()["items"])
