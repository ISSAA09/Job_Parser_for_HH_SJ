from src.HH_and_SJ_Vacancy import Vacancy
from src.Storage import JSONSaver
from src.HH_SJ_data import data_hh, data_sj

storage = JSONSaver("vacancies.json")
storage.remove_all_vacancies()


def user_interaction():
    """
        Функция для взаимодействия с пользователем
    """
    while True:
        print('Привет,какую вакансию ищите?')
        vacancy_input = input('Вакансия ')
        print("Выберете платформу для поиска вакансии")
        while True:
            try:
                platforms = int(input("1-HeadHunter\n2-SuperJob\n3-Обе\n"))
                if platforms in [1, 2, 3]:
                    break
                else:
                    print('Неверное число')
            except:
                print("Ошибка - это не число")
        while True:
            try:
                top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                if isinstance(top_n, int):
                    break
            except:
                print("Ошибка - это не число")

        filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
        if platforms == 1:
            data_hh(storage, vacancy_input)
        elif platforms == 2:
            data_sj(storage, vacancy_input)
        elif platforms == 3:
            data_sj(storage, vacancy_input)
            data_hh(storage, vacancy_input)

        filtered_vac = storage.filter_vacancies(filter_words)
        if not filtered_vac:
            print("Нет вакансий, соответствующих заданным критериям.")
            storage.remove_all_vacancies()
            continue

        sorted_vac = storage.get_vacancies_by_title(filtered_vac)
        top_vac = storage.get_top_vacancies(sorted_vac, top_n)
        for vacancy in top_vac:
            print(Vacancy(**vacancy))
        print(len(top_vac))
        print('Чтобы продолжить поиск вакансий нажмите "enter"\nДля завершения наберите "close"')
        if input() == 'close':
            break
