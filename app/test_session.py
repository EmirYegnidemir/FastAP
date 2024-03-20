from app.model import User, Post, Vote


def test_add_and_get_user(session):
    user = User(email="test@example.com", password="testpassword")  
    session.add(user)
    session.commit()
    fetched_user = session.query(User).filter_by(id="1").one()
    assert fetched_user == user

def test_add_and_get_post(session):
    user = User(email="test2@example.com", password="testpassword")  
    session.add(user)
    session.commit()
    post = Post(title="Test Post", content="Test Content", user=user)
    session.add(post)
    session.commit()
    fetched_post = session.query(Post).filter_by(title="Test Post").one()
    assert fetched_post == post

def test_add_and_get_vote(session):
    user = User(email="test3@example.com", password="testpassword")  
    session.add(user)
    session.commit()
    post = Post(title="Test Post", content="Test Content", user=user)
    session.add(post)
    session.commit()
    vote = Vote(user=user, post=post)
    session.add(vote)
    session.commit()
    fetched_vote = session.query(Vote).filter_by(user_id=user.id, post_id=post.id).one()
    assert fetched_vote == vote
