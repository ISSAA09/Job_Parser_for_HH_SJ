class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, vacancy_id, title, salary_from, salary_to, currency, experience, town,
                 company_name, url):
        self.vacancy_id = int(vacancy_id)
        self.title = title
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.experience = experience
        self.town = town
        self.company_name = company_name
        self.url = url

        self.validate_data()

        if self.salary_from or self.salary_to:
            self.salary = f"от {salary_from}" if salary_from else ""
            if salary_to:
                self.salary += f" до {salary_to}"
        else:
            self.salary = "Не указана"

    def validate_data(self):
        """
        Метод валидации данных
        """
        if not isinstance(self.vacancy_id, int):
            raise ValueError("Id вакансии должен быть целым числом.")
        if not isinstance(self.title, str):
            raise ValueError("Название профессии должно быть строкой.")
        if not isinstance(self.salary_from, (int, float, type(None))):
            raise ValueError("Минимальная зарплата должна быть числом или None.")
        if not isinstance(self.salary_to, (int, float, type(None))):
            raise ValueError("Максимальная зарплата должна быть числом или None.")
        if not isinstance(self.currency, str):
            raise ValueError("Валюта должна быть строкой.")
        if not isinstance(self.company_name, (str, type(None))):
            raise ValueError("Название компании должно быть строкой или None.")

    def __repr__(self):
        return (
            f"Vacancy(Id={self.vacancy_id}, title='{self.title}', salary='{self.salary}', "
            f"experience='{self.experience}', "
            f"city='{self.town}', "
            f"company_name='{self.company_name}', url='{self.url}')"
        )

    def __str__(self):
        return (

            f"ID: {self.vacancy_id}\nTitle: {self.title}\nЗарплата: {self.salary} {self.currency}\n"
            f"Опыт: {self.experience}\n"
            f"Город: {self.town}\nКомпания: {self.company_name}\nURL: {self.url}\n"
            f"\n****\n"
        )

    # Методы сравнения вакансий между собой по зарплате
    def __eq__(self, other):
        return self.salary_from == other.salary_from and self.salary_to == other.salary_to

    def __lt__(self, other):
        if self.salary_from is None:
            self_salary_from = 0
        else:
            self_salary_from = self.salary_from

        if other.salary_from is None:
            other_salary_from = 0
        else:
            other_salary_from = other.salary_from

        if self_salary_from == other_salary_from:
            if self.salary_to is None:
                self_salary_to = 0
            else:
                self_salary_to = self.salary_to

            if other.salary_to is None:
                other_salary_to = 0
            else:
                other_salary_to = other.salary_to

            return self_salary_to > other_salary_to
        else:
            return self_salary_from < other_salary_from

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def to_dict(self):
        """
        Метод возвращает новый словарь-представление
        """
        return {
            "vacancy_id": self.vacancy_id,
            "title": self.title,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "currency": self.currency,
            "experience": self.experience,
            "town": self.town,
            "company_name": self.company_name,
            "url": self.url
        }
