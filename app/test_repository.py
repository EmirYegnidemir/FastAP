# test_repository.py
import pytest
from app.model import User, Post, Vote
from app.repository import SqlAlchemyRepository
from sqlalchemy import text

@pytest.fixture(scope="module")
def repository(session):
    return SqlAlchemyRepository(session)

def test_add_and_get_user(repository):
    user = User(email="test1@example.com", password="testpassword")
    repository.add(user)
    repository.session.commit() 
    fetched_user = repository.get(user.id)
    assert fetched_user.email == "test1@example.com"
    assert fetched_user.password == "testpassword"

def test_add_and_get_post(repository):
    user = User(email="test2@example.com", password="testpassword")
    repository.add(user)
    repository.session.commit()

    post = Post(title="Test Post", content="Test Content", user=user)
    repository.add(post)
    repository.session.commit()

    rows = list(repository.session.execute(
        text('SELECT posts.title, posts.content, users.email FROM "posts" JOIN "users" ON posts.user_id = users.id')
    ))
    assert rows == [(post.title, post.content, user.email)]

def test_add_and_get_vote(repository):
    user = User(email="test3@example.com", password="testpassword")
    repository.add(user)
    repository.session.commit()

    post = Post(title="Test Post 2", content="Test Content", user=user)
    repository.add(post)
    repository.session.commit()

    vote = Vote(user=user, post=post)
    repository.add(vote)
    repository.session.commit()

    rows = list(repository.session.execute(
        text('SELECT votes.id, users.email, posts.title FROM "votes" JOIN "users" ON votes.user_id = users.id JOIN "posts" ON votes.post_id = posts.id')
    ))
    assert rows == [(vote.id, user.email, post.title)]

"""import pytest
from app.repository import Repository

@pytest.fixture(scope="module")
def repository(session):
    repository = Repository(session)
    repository.add_user(email="test2@example.com", password="testpassword")
    return repository

def test_add_and_get_user(repository):
    fetched_user = repository.get_user_by_id(1)
    assert fetched_user.email == "test2@example.com"
    assert fetched_user.password == "testpassword"

def test_add_and_get_post(repository):
    post = repository.add_post(title="Test Post", content="Test Content", owner_id=1)
    fetched_post = repository.get_post_by_title("Test Post")
    assert fetched_post == post

def test_add_and_get_vote(repository):
    post = repository.add_post(title="Test Post 2", content="Test Content", owner_id=1)
    vote = repository.add_vote(user_id=1, post_id=post.id)
    fetched_vote = repository.get_vote_by_user_and_post(user_id=1, post_id=post.id)
    assert fetched_vote == vote"""