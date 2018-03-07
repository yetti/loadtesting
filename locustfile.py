from locust import HttpLocust, TaskSet, task
from bs4 import BeautifulSoup

class UserBehavior(TaskSet):
    def detect_failure(self, island):
        with self.client.get(island + "/result?q=Howard", catch_response=True) as response:
            if response.content is None:
                response.failure("Content is None")
            else:
                soup = BeautifulSoup(response.content, 'html.parser')
                if soup.find(id="disableSecondarySearch") is not None:
                    response.failure("Secondary search disabled")

    @task(1)
    def search(self):
        self.detect_failure("")

    @task(2)
    def books(self):
        self.detect_failure("/book")

    @task(3)
    def pictures(self):
        self.detect_failure("/picture")

    @task(4)
    def articles(self):
        self.detect_failure("/article")

    @task(5)
    def newspapers(self):
        self.detect_failure("/newspaper")

    @task(6)
    def gazettes(self):
        self.detect_failure("/gazette")

    @task(7)
    def music(self):
        self.detect_failure("/music")

    @task(8)
    def maps(self):
        self.detect_failure("/map")

    @task(9)
    def collections(self):
        self.detect_failure("/collection")

    @task(10)
    def people(self):
        self.detect_failure("/people")

    @task(11)
    def lists(self):
        self.detect_failure("/list")

class SlowUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000

class QuickUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 8000
