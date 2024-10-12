from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)


class Quote(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    author: Mapped[str]
    address: Mapped[str] = mapped_column(default='Moscow', server_default='Moscow')
    text: Mapped[str]






