from abc import ABC, abstractmethod
import json
from src.HH_and_SJ_Vacancy import Vacancy
from operator import itemgetter


class VacancyStorage(ABC):
    """
    Абстрактный класс для реализации методов вакансий
    """
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_title(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass


class JSONSaver(VacancyStorage):
    """
        Класс для хранения вакансий в JSON-файле.
    """
    def __init__(self, filename):
        """
            Инициализация объекта JSONVacancyStorage
        """

        self.filename = filename

    def read_vacancies(self):
        """
         Метод для чтения вакансий из JSON-файла.
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def write_vacancies(self, vacancies):
        """
        Метод для записи вакансий в JSON-файл.
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        """
            Добавляет вакансии в JSON-файл
        """
        vacancies = self.read_vacancies()
        vacancy_dict = vacancy.to_dict()
        vacancies.append(vacancy_dict)
        self.write_vacancies(vacancies)

    @staticmethod
    def get_vacancies_by_title(vacancies):
        """
            Метод для сортировки вакансий по названию профессии
        """
        filtered_list_by_title = []
        for vac in vacancies:
            if vac.get('title'):
                filtered_list_by_title.append(vac)
        sorted_vacancies = sorted(filtered_list_by_title, key=lambda x: x.get('title', 0), reverse=True)
        return sorted_vacancies

    def delete_vacancy(self, vacancy_id):
        """
            Удаляет вакансию из файла по-указанному ID.
        """
        vacancies = self.read_vacancies()
        for vac in vacancies:
            if vac['vacancy_id'] == vacancy_id:
                vacancies.remove(vac)
                self.write_vacancies(vacancies)
        return vacancies

    def filter_vacancies(self, keywords):
        """
        Метод получает вакансии, в описании которых есть определенные ключевые слова
        """
        vacancies = self.read_vacancies()
        filter_words_list = keywords.split()

        def check_words_in_vacancy(vacancy):
            for word in filter_words_list:
                if not any(word.lower() in value.lower() for value in vacancy.values() if isinstance(value, str)):
                    return False
            return True

        return [v for v in vacancies if check_words_in_vacancy(v)]

    def remove_all_vacancies(self):
        """
        Полностью очищает хранилище, удаляя все вакансии из JSON-файла.
        """
        empty_vacancies = []
        self.write_vacancies(empty_vacancies)

    @staticmethod
    def get_top_vacancies(filter_by_keyword, number):
        """
            Статический метод для получения топ N вакансий по зарплате
        """
        vacancies = filter_by_keyword
        filtered_list = []
        for vac in vacancies:
            if vac.get('salary_from'):
                filtered_list.append(vac)
        sorted_vacancies = sorted(filtered_list, key=lambda x: x.get('salary_from', 0), reverse=True)
        top_10_vacancies = sorted_vacancies[:number]
        return top_10_vacancies
