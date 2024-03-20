from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class User:
    email: str
    password: str
    posts: List[Post] = field(default_factory=list)
    votes: List['Vote'] = field(default_factory=list)

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.email == other.email and self.password == other.password

    def __hash__(self):
        return hash((self.email, self.password))

@dataclass
class Post:
    title: str
    content: str
    user: User
    def __hash__(self):
        return hash((self.title, self.content, self.user))

@dataclass
class Vote:
    user: User
    post: Post
    def __hash__(self):
        return hash((self.user, self.post))