# -*- coding: utf-8 -*-
import pytest
from application import Application



# создаем фикстуру
@pytest.fixture # тут мы сказали что создаем фикстуру
def app(request): # 'request будет принимать свойство закрытия браузера
    fixture = Application() # ссылаемся на модуль main_fixture с классом Application
    request.addfinalizer(fixture.closeBrowser) # тут вызываем закрытие браузера
    return fixture
    # addfinalizer это свойство фикстуры из либы pytest'a



def test_group(app): # app это фикстура со всем нужными тестами
    app.openPage()
    app.find_teckets(city_from="Мсоква", city_to="Париж")
    app.check_date(date_from="25.04.2019", date_back="04.05.2019")
    app.search()


def tearDown(app): # вызов идет через фикстуру app ^^
    app.closeBrowser()

