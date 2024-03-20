import abc
from typing import Set
from app.orm import users, posts, votes
from app.model import User, Post, Vote

class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()  # type: Set[User, Post, Vote]

    def add(self, user: User):
        self._add(user)
        self.seen.add(user)

    def get(self, id) -> User:
        user = self._get(id)
        if user:
            self.seen.add(user)
        return user

    @abc.abstractmethod
    def _add(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, id) -> User:
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, user):
        self.session.add(user)

    def _get(self, id):
        return self.session.query(User).filter_by(id=id).one()
    
    """from app.orm import User, Post, Vote

class Repository:
    def __init__(self, session):
        self.session = session

    def add_user(self, email, password):
        user = User(email=email, password=password)
        self.session.add(user)
        self.session.commit()
        return user

    def get_user_by_id(self, id):
        return self.session.query(User).filter_by(id=id).one()

    def add_post(self, title, content, owner_id):
        post = Post(title=title, content=content, owner_id=owner_id)
        self.session.add(post)
        self.session.commit()
        return post

    def get_post_by_title(self, title):
        return self.session.query(Post).filter_by(title=title).one()

    def add_vote(self, user_id, post_id):
        vote = Vote(user_id=user_id, post_id=post_id)
        self.session.add(vote)
        self.session.commit()
        return vote

    def get_vote_by_user_and_post(self, user_id, post_id):
        return self.session.query(Vote).filter_by(user_id=user_id, post_id=post_id).one()"""