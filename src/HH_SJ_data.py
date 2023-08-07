from src.HH_and_SJ_API import HH_API, SJ_API
from src.HH_and_SJ_Vacancy import Vacancy


def data_hh(storage, find):
    """
        Метод фильтрует и сохраняет вакансии в JSON-файл, полученные с HH.ru
    """
    api_hh = HH_API()
    vacancies_hh = api_hh.get_vacancies(find)
    if vacancies_hh:
        for vacancy in vacancies_hh:
            vacancy_id = vacancy.get("id")
            title = vacancy.get("name")
            url = vacancy.get("alternate_url")
            city = vacancy.get("area", {}).get("name", "Unknown City")
            experience = vacancy.get("experience", {}).get("name")
            salary_from = vacancy.get("salary", {}).get("from")
            salary_to = vacancy.get("salary", {}).get("to")
            currency = vacancy.get("salary", {}).get("currency")
            company_name = vacancy.get("employer", {}).get("name")

            vacancy_obj = Vacancy(vacancy_id, title, salary_from, salary_to, currency,
                                  experience, city, company_name, url)
            storage.add_vacancy(vacancy_obj)
    else:
        print('Вакансии на HeadHunter не найдены.')


def data_sj(storage, find):
    """
    Метод фильтрует и сохраняет вакансии в JSON-файл, полученные с SJ.ru
    """
    api_sj = SJ_API()
    vacancies_sj = api_sj.get_vacancies(find)
    if vacancies_sj:
        for vacancy in vacancies_sj:
            vacancy_id = vacancy.get("id")
            title = vacancy.get("profession")
            url = vacancy.get("link")
            city = vacancy.get("town", {}).get("title", "Unknown City")
            salary_from = vacancy.get("payment_from")
            salary_to = vacancy.get("payment_to")
            currency = vacancy.get("currency")
            company_name = vacancy.get("client", {}).get("title")
            experience = vacancy.get("experience", {}).get("title")

            vacancy_obj = Vacancy(vacancy_id, title, salary_from, salary_to, currency,
                                  experience, city, company_name, url)
            storage.add_vacancy(vacancy_obj)
    else:
        print('Вакансии на SuperJob не найдены.')
