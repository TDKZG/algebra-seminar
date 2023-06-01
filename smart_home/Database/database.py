from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import Session, relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    active = Column(Boolean)
    admin = Column(Boolean)
    tasks = relationship("Task", backref="user")

    def __repr__(self) -> str:
        return f"id={self.id}, name={self.name}, surname={self.surname}"


class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    status = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"id={self.id}, name={self.name}, location={self.location}, brand={self.brand}, status={self.status}"


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    datetime = Column(DateTime)
    status = Column(String, default="na cekanju")
    duration_minutes = Column(Integer, default=60)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class Meteo(Base):
    __tablename__ = "meteo"
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, nullable=False)
    city_temp = Column(Float)
    city_humidity = Column(Float)
    city_pressure = Column(Float)
    inside_temp = Column(Float)
    outside_temp = Column(Float)


db_engine = create_engine("sqlite:///SmartHome.db")
Base.metadata.create_all(bind=db_engine)


def db_add_user(name, surname, username, password, active, admin):
    with Session(bind=db_engine) as session:
        user_exists = (
            session.query(User).filter(User.username == username).one_or_none()
        )
        if user_exists:
            return

        user = User(
            name=name,
            surname=surname,
            username=username,
            password=password,
            active=active,
            admin=admin,
        )
        session.add(user)
        session.commit()


def db_delete_user(user_id):
    with Session(db_engine) as session:
        user = session.query(User).filter(User.id == user_id).one_or_none()

        if user:
            session.delete(user)
            session.commit()


def db_login(username, password):
    with Session(db_engine) as session:
        user = (
            session.query(User)
            .filter(User.username == username, User.password == password)
            .one_or_none()
        )
        return user


def db_devices():
    with Session(db_engine) as session:
        devices = session.query(Device).all()
        return devices


def db_update_device(device):
    with Session(bind=db_engine) as session:
        current_device = session.query(Device).filter(Device.id == device.id)
        current_device.update(
            values={
                "brand": device.brand,
                "name": device.name,
                "location": device.location,
                "status": device.status,
            }
        )
        session.commit()


def db_add_meteo_data(meteo):
    with Session(bind=db_engine) as session:
        session.add(meteo)
        session.commit()


def db_delete_all_meteo_data():
    with Session(bind=db_engine) as session:
        session.query(Meteo).delete()
        session.commit()
