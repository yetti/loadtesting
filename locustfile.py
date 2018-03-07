from locust import HttpLocust, TaskSet, task
from bs4 import BeautifulSoup

def detect_failure(self, island):
    with self.client.get(island + "/result?q=Howard", catch_response=True) as response:
        soup = BeautifulSoup(response.content, 'html.parser')
        if soup.find(id="disableSecondarySearch") is not None:
            response.failure("Secondary search disabled")

class UserBehavior(TaskSet):
    min_wait = 5000
    max_wait = 9000

    @task(1)
    def search(self):
        detect_failure(self, "")

    @task(2)
    def books(self):
        detect_failure(self, "/book")

    @task(3)
    def pictures(self):
        detect_failure(self, "/picture")

    @task(4)
    def articles(self):
        detect_failure(self, "/article")

    @task(5)
    def newspapers(self):
        detect_failure(self, "/newspaper")

    @task(6)
    def gazettes(self):
        detect_failure(self, "/gazette")

    @task(7)
    def music(self):
        detect_failure(self, "/music")

    @task(8)
    def maps(self):
        detect_failure(self, "/map")

    @task(9)
    def collections(self):
        detect_failure(self, "/collection")

    @task(10)
    def people(self):
        detect_failure(self, "/people")

    @task(11)
    def lists(self):
        detect_failure(self, "/list")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
