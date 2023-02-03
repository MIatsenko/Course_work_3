import requests


def getting_json_from_web():
    """Ф-я получает список словарей по ссылке"""
    file = requests.get("https://www.jsonkeeper.com/b/FGAS")
    file = file.json()
    return file


def finding_ides():
    """Ф-я находит id последних операций и возвращает их в правильном порядке"""
    list_of_id = []
    dates = []
    dict_of_dates = {}
    max_date = ['2019', '11', '00']
    file = getting_json_from_web()
    for index in file:
        if len(index) != 0 and index['state'] == "EXECUTED":
            date_month_num = index['date'].split('T')
            year_month_day = date_month_num[0].split('-')
            index_id = index['id']
            if year_month_day[0] == max_date[0] and year_month_day[1] >= max_date[1]:
                full_date = year_month_day[0] + year_month_day[1] + year_month_day[2]
                dates.append(full_date)
                dict_of_dates[full_date] = index_id

    dates.sort(reverse=True)
    dates = dates[0:6]
    while len(list_of_id) < 5:
        for ides in dates:
            list_of_id.append(dict_of_dates[ides])
    return list_of_id
