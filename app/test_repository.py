# test_repository.py
import pytest
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
    assert fetched_vote == vote