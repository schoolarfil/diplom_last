import sender_stand_request
#Филиппов Николай, 5я когорта - финальный проект.

def test_get_order_by_track():
    # Создание нового заказа
    response = sender_stand_request.post_new_order()

    if response.status_code == 201:
        track_number = response.json()["track"]
        # Получение заказа по трек-номеру
        get_order_response = sender_stand_request.get_order_by_track(track_number)

        # Проверка кода ответа GET-запроса
        assert get_order_response.status_code == 200, "Order retrieval failed with status code: " + str(
            get_order_response.status_code)

        # Вывод результатов GET-запроса
        print(get_order_response.json())
