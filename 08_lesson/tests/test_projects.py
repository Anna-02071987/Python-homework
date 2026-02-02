import uuid 
 
from yougile_api import YougileAPI 
 
 
# ---------- POST ---------- 
def test_create_project_positive(api): 
    title = f"project_{uuid.uuid4()}" 
    r = api.create_project(title) 
 
    assert r.status_code == 201 
    assert "id" in r.json() 
 
 
def test_create_project_negative_no_title(api): 
    user_id = api.get_any_user_id() 
    payload = {"users": {user_id: "admin"}} 
 
    r = api._request("POST", "/api-v2/projects", json=payload) 
 
    assert r.status_code in (400, 422) 
 
 
# ---------- PUT ---------- 
def test_update_project_positive(api, created_project): 
    new_title = f"updated_{uuid.uuid4()}" 
    r = api.update_project(created_project, new_title) 
 
    assert r.status_code == 200 
 
 
def test_update_project_negative_wrong_id(api): 
    r = api.update_project("invalid_id", "test") 
 
    assert r.status_code in (400, 404) 
 
 
# ---------- GET ---------- 
def test_get_project_positive(api, created_project): 
    r = api.get_project(created_project) 
 
    assert r.status_code == 200 
    assert r.json()["id"] == created_project 
 
 
def test_get_project_negative_wrong_id(api): 
    r = api.get_project("invalid_id") 
 
    assert r.status_code in (400, 404) 
