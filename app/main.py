from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    # Create custom class instances
    customer_list: list[Customer] = [
        Customer(
            customer["name"],
            customer["food"]
        ) for customer in customers
    ]
    cleaning_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    # Sell food and drinks to each customer
    for customer in customer_list:
        CinemaBar.sell_product(customer, customer.food)

    # Start the movie session
    hall.movie_session(movie, customer_list, cleaning_staff)
