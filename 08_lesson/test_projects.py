import pytest
from api_client import YougileAPIClient


class TestYougileProjects:
    """Tests for Yougile projects API"""

    @pytest.fixture
    def api_client(self):
        return YougileAPIClient()

    @pytest.fixture
    def project_data(self):
        return {
            "title": "Test Project",
            "metadata": {
                "description": "Test project for API testing"
            }
        }

    @pytest.fixture
    def created_project(self, api_client, project_data):
        response = api_client.create_project(project_data)
        assert response.status_code == 201, (
            f"Failed to create project: {response.text}"
        )
        project = response.json()
        project_id = project["id"]
        yield project_id
        api_client.delete_project(project_id)

    def test_create_project_positive(self, api_client, project_data):
        response = api_client.create_project(project_data)
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert data["title"] == project_data["title"]
        api_client.delete_project(data["id"])

    def test_get_project_positive(self, api_client, created_project):
        response = api_client.get_project(created_project)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == created_project
        assert "title" in data

    def test_update_project_positive(self, api_client, created_project):
        update_data = {
            "title": "Updated Project",
            "metadata": {"description": "Updated"}
        }
        response = api_client.update_project(created_project, update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == update_data["title"]

    def test_create_project_negative_missing_title(self, api_client):
        invalid_data = {"metadata": {"description": "No title"}}
        response = api_client.create_project(invalid_data)
        assert response.status_code == 400

    def test_get_project_negative_not_found(self, api_client):
        response = api_client.get_project("non-existent-123")
        assert response.status_code == 404

    def test_update_project_negative_invalid_id(self, api_client):
        update_data = {"title": "Test"}
        response = api_client.update_project("invalid-id", update_data)
        assert response.status_code in [400, 404]
