"""
CREATE SUPERUSER
python manage.py createsuperuser

CREATE TOPICS
test_topic1 = Topic.objects.create(title="TEST TOPIC 1", description="DESCRIPTION IN TEST TOPIC")
test_topic2 = Topic.objects.create(title="TEST TOPIC 2", description="DESCRIPTION IN TEST TOPIC2")

ADD USER TO TOPIC
user_admin = User.objects.first()
test_topic1.prefers.add(user_admin)
user_igor = User.objects.all()[1]
test_topic1.prefers.add(user_igor)
test_topic2.prefers.add(user_igor)
user_dima = User.objects.last()
test_topic2.prefers.add(user_dima)
test_topic1.prefers.add(user_dima)

CREATE POSTS
post1 = Post.objects.create(slug="test1", title="TEST_POST_1", text="TEXT FROM POST 1", author=user_admin)
post1.contains.add(test_topic1)
post2 = Post.objects.create(slug="test2", title="TEST_POST_2", text="TEXT FROM POST 2", author=user_admin)
post2.contains.add(test_topic2)
post2.contains.add(test_topic1)
post3 = Post.objects.create(slug="test3", title="TEST_POST_3", text="TEXT FROM POST 3", author=user_igor)
post3.contains.add(test_topic1)
post3.contains.add(test_topic2)
post4 = Post.objects.create(slug="test4", title="TEST_POST_4", text="TEXT FROM POST 4", author=user_igor)
post4.contains.add(test_topic2)
post5 = Post.objects.create(slug="test5", title="TEST_POST_5", text="TEXT FROM POST 5", author=user_dima)
post5.contains.add(test_topic1)
post5.contains.add(test_topic2)

CREATE COMMENTS
Comment.objects.create(content="COMMENT 1 TO POST 1", contains=post1, author=user_admin)
Comment.objects.create(content="COMMENT 2 TO POST 1", contains=post1, author=user_admin)
Comment.objects.create(content="COMMENT 3 TO POST 1", contains=post1, author=user_igor)
Comment.objects.create(content="COMMENT 4 TO POST 1", contains=post1, author=user_dima)
Comment.objects.create(content="COMMENT 5 TO POST 1", contains=post1, author=user_dima)
Comment.objects.create(content="COMMENT 6 TO POST 1", contains=post1, author=user_igor)

Comment.objects.create(content="COMMENT 1 TO POST 2", contains=post2, author=user_igor)
Comment.objects.create(content="COMMENT 2 TO POST 2", contains=post2, author=user_igor)
Comment.objects.create(content="COMMENT 3 TO POST 2", contains=post2, author=user_igor)
Comment.objects.create(content="COMMENT 4 TO POST 2", contains=post2, author=user_admin)
Comment.objects.create(content="COMMENT 5 TO POST 2", contains=post2, author=user_admin)

Comment.objects.create(content="COMMENT 1 TO POST 3", contains=post3, author=user_admin)
Comment.objects.create(content="COMMENT 2 TO POST 3", contains=post3, author=user_admin)
Comment.objects.create(content="COMMENT 3 TO POST 3", contains=post3, author=user_admin)
Comment.objects.create(content="COMMENT 4 TO POST 3", contains=post3, author=user_igor)
Comment.objects.create(content="COMMENT 5 TO POST 3", contains=post3, author=user_igor)

Comment.objects.create(content="COMMENT 1 TO POST 4", contains=post4, author=user_igor)
Comment.objects.create(content="COMMENT 2 TO POST 4", contains=post4, author=user_igor)
Comment.objects.create(content="COMMENT 3 TO POST 4", contains=post4, author=user_igor)
Comment.objects.create(content="COMMENT 4 TO POST 4", contains=post4, author=user_igor)
Comment.objects.create(content="COMMENT 5 TO POST 4", contains=post4, author=user_dima)

POST 5 WITHOUT COMMENTS
"""
from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    prefers = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Post(models.Model):
    slug = models.SlugField(max_length=40)
    title = models.CharField(max_length=150)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contains = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateField(auto_now=True)
    content = models.CharField(max_length=150)
    contains = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
