from app.models import User, Post, Vote

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
        return self.session.query(Vote).filter_by(user_id=user_id, post_id=post_id).one()