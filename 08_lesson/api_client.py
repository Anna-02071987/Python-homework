import requests
import config


class YougileAPIClient:
    """Client for Yougile API"""

    def __init__(self):
        self.base_url = config.Config.BASE_URL
        self.headers = config.Config.HEADERS

    def _make_request(self, method, endpoint, **kwargs):
        """Make HTTP request"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(
            method, url, headers=self.headers, **kwargs
        )
        return response

    def create_project(self, data):
        """Create project"""
        return self._make_request("POST", "/projects", json=data)

    def get_project(self, project_id):
        """Get project by ID"""
        return self._make_request("GET", f"/projects/{project_id}")

    def update_project(self, project_id, data):
        """Update project"""
        return self._make_request("PUT", f"/projects/{project_id}", json=data)

    def delete_project(self, project_id):
        """Delete project"""
        return self._make_request("DELETE", f"/projects/{project_id}")
