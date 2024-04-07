class Vacancy:
    vacancy_title: str  # Название вакансии
    vacancy_link: str  # Ссылка на вакансию
    vacancy_city: str  # Город вакансии
    company_name: str  # Название работодателя
    salary_from: int  # Зарплата от
    salary_to: int  # Зарплата до
    currency: str  # Валюта
    vacancy_responsibility: str  # Описание вакансии
    vacancy_requirements: str  # требование к вакансии

    def __init__(self, dictionary):
        self.vacancy_title = dictionary.get('vacancy_title')
        self.vacancy_link = dictionary.get('vacancy_link')
        self.vacancy_city = dictionary.get('vacancy_city')
        self.company_name = dictionary.get('company_name')
        self.salary_from = dictionary.get('salary_from')
        self.salary_to = dictionary.get('salary_to')
        self.currency = dictionary.get('currency')
        if dictionary.get('vacancy_responsibility'):
            self.vacancy_responsibility = dictionary.get('vacancy_responsibility')
        else:
            self.vacancy_responsibility = 'Не указано'
        if dictionary.get('vacancy_requirements'):
            self.vacancy_requirements = dictionary.get('vacancy_requirements')
        else:
            self.vacancy_requirements = 'Не указано'

    def __str__(self):
        """ Добавление строкового отображения """
        print('*' * 150)

        return (f'Название вакансии, ссылка: {self.vacancy_title}, {self.vacancy_link}\n'
                f'Город, компания: {self.vacancy_city}, {self.company_name}\n'
                f'Уровень заработной платы, валюта: {self.salary_from} - {self.salary_to}, {self.currency}\n'
                f'Описание: {self.vacancy_responsibility}\n'
                f'Требования: {self.vacancy_requirements}')

    def validate_vacancy(self):
        pass

    def check_salary_from(self):
        """ Проверка на наличие начального уровня зарплаты """
        if isinstance(self.salary_from, int) and self.salary_from > 0:
            return True
        else:
            return False

    def check_currency(self):
        """ Проверка валюты RUB или USD """
        if self.currency == 'RUR':
            return 'RUR'
        elif self.currency == 'USD':
            return 'USD'
        else:
            return False

    def __lt__(self, other):
        return self.salary_from < other.salary_from
