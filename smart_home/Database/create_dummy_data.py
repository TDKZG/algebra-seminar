from sqlalchemy.orm import Session
from database import *


def populate_database():
    with Session(bind=db_engine) as session:
        user = User(name="Ivan", surname="Horvat", username="admin", password="12345")
        session.add(user)

        device1 = Device(name="TV", location="dnevni boravak", brand="LG")
        session.add(device1)
        device2 = Device(name="Perilica suda", location="kuhinja", brand="Beko")
        session.add(device2)

        task1 = Task(description="Pranje suda", duration_minutes=30)
        task1.user = user
        session.add(task1)
        task2 = Task(description="Ugasi televizor", duration_minutes=0)
        task2.user = user
        session.add(task2)

        session.commit()


if __name__ == "__main__":
    populate_database()
