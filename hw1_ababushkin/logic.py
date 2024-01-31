import datetime


def return_human_time(unix_time: int) -> str:
    """Функция возвращает человекочитаемый формат времени"""
    return datetime.datetime.fromtimestamp(unix_time, datetime.timezone.utc).strftime(
        "%H:%M %p"
    )


def sorted_list_of_open_hour(list_of_open_hours: list) -> list:
    """Функция возвращает сортированный список словарей по ключу времени"""
    list_of_open_hours.sort(key=lambda dictionary: dictionary["value"])
    return list_of_open_hours


def modify_data_to_human(data_open) -> str:
    """Функция возвращает готовую строку согласно задания"""
    list_days = list(data_open.keys())
    result_string = ""
    for day_of_the_week in list_days:
        sorted_list_of_open_hour(data_open[day_of_the_week])

    count = 0
    while count < len(list_days):
        if data_open[list_days[count]]:
            last_value_type = data_open[list_days[count]][-1]["type"]
            if last_value_type == "open":
                data_open[list_days[count]].append(data_open[list_days[count + 1]][0])
                data_open[list_days[count + 1]].pop(0)
            result_string += f"{list_days[count]}: {return_human_string(data_open[list_days[count]])}\n"
            count += 1

        else:
            result_string += f"{list_days[count]}: close\n"
            count += 1
    print(result_string)
    return result_string


def return_human_string(sorted_list_of_open_hours: list) -> str:
    """Функция возвращает человекочетаемую строку из списка данных"""
    human_string = ""
    for i in range(0, len(sorted_list_of_open_hours)):
        if sorted_list_of_open_hours[i]["type"] == "open":
            human_string += (
                f"{return_human_time(sorted_list_of_open_hours[i]['value'])} - "
            )
        if sorted_list_of_open_hours[i]["type"] == "close":
            if i == (len(sorted_list_of_open_hours) - 1):
                human_string += (
                    f"{return_human_time(sorted_list_of_open_hours[i]['value'])}"
                )
            else:
                human_string += (
                    f"{return_human_time(sorted_list_of_open_hours[i]['value'])}, "
                )
    return human_string


if __name__ == "__main__":

    data = {
        "monday": [],
        "tuesday": [{"type": "open", "value": 3600}, {"type": "close", "value": 32400}],
        "wednesday": [
            {"type": "open", "value": 3600},
            {"type": "close", "value": 32400},
        ],
        "thursday": [],
        "friday": [{"type": "open", "value": 64800}],
        "saturday": [
            {"type": "close", "value": 82800},
            {"type": "close", "value": 3600},
            {"type": "open", "value": 32400},
            {"type": "close", "value": 39600},
            {"type": "open", "value": 57600},
        ],
        "sunday": [],
    }

    list_for_sort = [
        {"type": "open", "value": 32400},
        {"type": "close", "value": 39600},
        {"type": "open", "value": 57600},
        {"type": "close", "value": 82800},
    ]

    modify_data_to_human(data)
    print()
    return_human_string(list_for_sort)
