from sqlalchemy.orm import Session
from Model.database.Users import Users

session = Session()

c1 = Users(
    username="aaa",
    password="adasdf",
    email="adasd@asdf",
    role="user"
)

session.add(c1)
session.commit()

user = session.query(Users).filter(Users.username == "aaa")
print(user)