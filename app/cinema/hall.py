from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list[Customer], cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for c in customers:
            print(f'{c.name} is watching "{movie_name}".')
        print(f'"{movie_name}" ended.')
        print(f'Cleaner {cleaning_staff.name} is cleaning hall number {self.number}.')
