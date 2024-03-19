from app.models import User, Post, Vote


def test_add_and_get_user(session):
    user = User(email="test@example.com", password="testpassword")  
    session.add(user)
    session.commit()
    fetched_user = session.query(User).filter_by(id="1").one()
    assert fetched_user == user
    session.rollback()

def test_add_and_get_post(session):
    user = User(email="test2@example.com", password="testpassword")  
    session.add(user)
    session.commit()
    post = Post(title="Test Post", content="Test Content", owner_id=user.id)
    session.add(post)
    session.commit()
    fetched_post = session.query(Post).filter_by(title="Test Post").one()
    assert fetched_post == post
    session.rollback()

def test_add_and_get_vote(session):
    user = User(email="test3@example.com", password="testpassword")  
    session.add(user)
    session.commit()
    post = Post(title="Test Post", content="Test Content", owner_id=user.id)
    session.add(post)
    session.commit()
    vote = Vote(user_id=user.id, post_id=post.id)
    session.add(vote)
    session.commit()
    fetched_vote = session.query(Vote).filter_by(user_id=user.id, post_id=post.id).one()
    assert fetched_vote == vote
    session.rollback()
