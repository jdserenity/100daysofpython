from sheety import Sheety; from kiwi import Kiwi; from notify import Notify;


def main():
    sheety = Sheety(); kiwi = Kiwi(); notify = Notify(); 

    # sheety.add_user_to_sheet()

    cities_to_search = sheety.get_entries_from_sheet()
    
    best_flights = kiwi.search_for_cheapest_flight_in_each_city(cities_to_search)

    users = sheety.return_list_of_users()

    notify.send_emails_to_users_with_discounted_flight_details(best_flights, cities_to_search, users)


if __name__ == "__main__":
    main()
