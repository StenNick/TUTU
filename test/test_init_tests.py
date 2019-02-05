# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application



# создаем фикстуру
@pytest.fixture # тут мы сказали что создаем фикстуру
def app(request): # 'request будет принимать свойство закрытия браузера
    fixture = Application() # ссылаемся на модуль main_fixture с классом Application
    request.addfinalizer(fixture.closeSession.closeBrowser) # тут вызываем закрытие браузера
    return fixture
    # addfinalizer это свойство фикстуры из либы pytest'a



def test_group(app): # app это фикстура со всем нужными тестами
    app.openSession.openPage(url_page="https://www.tutu.ru/")
    app.findTickets.find_teckets(city_from="Мсоква", city_to="Париж")
    app.getDate.check_date(date_from="25.04.2019", date_back="04.05.2019")
    app.search.search()
    app.closeSession.closeBrowser()


