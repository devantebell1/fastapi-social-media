from typing import List
from app import schemas
import pytest

def validate(post):
    posts = schemas.PostOut(**post)
    return posts


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    
    posts_map = map(validate, res.json())
    
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    
def test_unathorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401
    
def test_unathorized_user_get_one_posts(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401
    
def test_get_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/8888")
    assert res.status_code == 404
 
def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title

### CREATE POST TEST ####

@pytest.mark.parametrize("title, content, published", [
    ("new title", "new content", True),
    ("Hello title", "Hello content", False),
    ("good morning", "good afternoon", True),
    
])
def test_create_post(authorized_client, create_test_user, test_posts, title, content, published):
    res = authorized_client.post("/posts/", json={"title": title, "content": content, "published": published})
    
    created_post = schemas.Post(**res.json())
    
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert res.status_code == 201
    assert created_post.user_id == create_test_user['id']
    
def test_create_post_default_published_true(authorized_client, create_test_user, test_posts):
    res = authorized_client.post("/posts/", json={"title": "some title", "content": "some content"})
    
    created_post = schemas.Post(**res.json())
    assert created_post.title == "some title"
    assert created_post.content == "some content"
    assert created_post.published == False
    assert res.status_code == 201
    assert created_post.user_id == create_test_user['id']
    
def test_unathorized_create_posts(client, test_posts):
    res = client.post("/posts/", json={"title": "some title", "content": "some content"})
    assert res.status_code == 401
    
#### DELETE POST TEST ####    

def test_unathorized_delete_posts(client, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401
    
def test_delete_posts_success(authorized_client, test_posts, create_test_user):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204
    
def test_delete_posts_non_exist(authorized_client, test_posts, create_test_user):
    res = authorized_client.delete(f"/posts/800")
    assert res.status_code == 404
    
def test_delete_other_user_posts(authorized_client, test_posts, create_test_user):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert res.status_code == 403
    
def test_update_post(authorized_client, create_test_user, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[0].id
    }
    
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    assert res.status_code == 200
    updated_post = schemas.Post(**res.json())
    assert updated_post.title == data['title']
    assert updated_post.content == data['content']
    
def test_update_other_user_post(authorized_client, create_test_user, create_test_user2, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[3].id
    }
    
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    assert res.status_code == 403
    
def test_unathorized_update_posts(client, test_posts):
    res = client.put(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_update_post_not_exist(authorized_client, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[0].id
    }
    
    res = authorized_client.put(f"/posts/8888", json=data)
    assert res.status_code == 404