# create_users.py
from app.database import SessionLocal, engine, Base
from app.models import User
from app.auth import pwd_context

# Cria as tabelas
Base.metadata.create_all(bind=engine)

# Conecta ao banco
db = SessionLocal()

# Adiciona usuários fictícios
user1 = User(username="user", role="user", hashed_password=pwd_context.hash("L0XuwPOdS5U"))
user2 = User(username="admin", role="admin", hashed_password=pwd_context.hash("JKSipm0YH"))

db.add(user1)
db.add(user2)
db.commit()
db.close()
