from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from datetime import datetime


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Files(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('user.id'), index=True)
    file_name: so.Mapped[str] = so.mapped_column(sa.String(120), index=True)
    file_type: so.Mapped[str] = so.mapped_column(sa.String(120), index=True)
    file_size: so.Mapped[int] = so.mapped_column(sa.Integer, index=True)
    upload_date: so.Mapped[str] = so.mapped_column(sa.DateTime, default=datetime.now(), index=True)

    def __repr__(self):
        return '<Files {}>'.format(self.file_name)
