from config import PATH


def user_interaction():
    user_input = input("Какую вакансию вы ищете? ")
    hh_vacancies = PATH.HeadHunterApi.get_vacancy(user_input)
    user_city = input("В каком городе? ")


if __name__ == '__main__':
    user_interaction()
