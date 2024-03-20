# orm.py
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry, relationship
from app.model import User, Post, Vote

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('email', String(255), unique=True),
    Column('password', String(255)),
)

posts = Table(
    'posts', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255)),
    Column('content', String(255)),
    Column('user_id', Integer, ForeignKey('users.id')),
)

votes = Table(
    'votes', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('post_id', Integer, ForeignKey('posts.id')),
)

mapper_registry = registry()
def start_mappers():
    mapper_registry.map_imperatively(User, users, properties={
        'posts': relationship(Post, backref='user'),
        'votes': relationship(Vote, backref='user')
    })
    mapper_registry.map_imperatively(Post, posts, properties={
        'votes': relationship(Vote, backref='post')
    })
    mapper_registry.map_imperatively(Vote, votes)

"""from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer ,primary_key=True, nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, 
                        server_default=func.current_timestamp())

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer ,primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    published= Column(Boolean, server_default='1', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, 
                        server_default=func.current_timestamp())
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship('User')  # creates a property and fetches the user based on the owner_id, automatically

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "post.id", ondelete="CASCADE"), primary_key=True)"""