from page_object_patern.pages.search_hotel import SearchHotelPage
from page_object_patern.pages.search_results import SearchResultsPage
from page_object_patern.utils.read_excel import ExcelReader

import allure
import pytest
import xlrd

# dzielenie metody setup: zrob osobna klase w osobny pliku i uzyj @pytest.mark.usefixtures("setup")


@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @allure.title("Hotel search Test")
    @allure.description("Serching of hotels regarding to data from report")
    @pytest.mark.parametrize("data", ExcelReader.get_data())
    def test_hotel_search(self, data):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range(data.check_in, data.check_out)
        search_hotel_page.perform_search()
        search_results = SearchResultsPage(self.driver)
        hotel_names = search_results.get_hotel_names()
        hotel_prices = search_results.get_hotel_prices()

        assert hotel_names[0] == 'Jumeirah Beach Hotel'
        assert hotel_names[1] == 'Oasis Beach Tower'
        assert hotel_names[2] == 'Rose Rayhaan Rotana'
        assert hotel_names[3] == 'Hyatt Regency Perth'

        assert hotel_prices[0] == '$22'
        assert hotel_prices[1] == '$50'
        assert hotel_prices[2] == '$80'
        assert hotel_prices[3] == '$150'
