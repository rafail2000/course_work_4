from src.api import HeadHunterAPI
from src.vacancy import Vacancy


def user_interaction():
    query_vacancy = input("Какую вакансию ищем? ")
    user_top_n = int(input("Сколько вакансий вывести в топе? "))
    query_city = input("В каком городе? ")

    hh_api = HeadHunterAPI()
    hh_vacancy = hh_api.get_vacancy(query_vacancy)

    print(repr(hh_api))
    list_json_vacancy = hh_api.save_json(hh_vacancy)

    vacancies = [Vacancy(item) for item in list_json_vacancy]  # Создание экземпляров класса вакансий из списка.
    print(*vacancies, sep='\n')
    sorted_vacancy_list = []
    sorted_vacancy = sorted(vacancies, key=lambda x: x.salary_from, reverse=True)

    n = 0
    for vacancy in sorted_vacancy:
        if vacancy.vacancy_city == query_city:
            sorted_vacancy_list.append(vacancy)
    for n, vacancy in enumerate(sorted_vacancy_list[:user_top_n]):
        print(f'{n + 1}.{vacancy}')


user_interaction()
