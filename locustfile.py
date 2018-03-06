from locust import HttpLocust, TaskSet

def search(l):
    l.client.get("/result?q=Howard")

def books(l):
    l.client.get("/book/result?q=Howard")

def pictures(l):
    l.client.get("/picture/result?q=Howard")

def articles(l):
    l.client.get("/article/result?q=Howard")

def newspapers(l):
    l.client.get("/newspaper/result?q=Howard")

def gazettes(l):
    l.client.get("/gazette/result?q=Howard")

def music(l):
    l.client.get("/music/result?q=Howard")

def maps(l):
    l.client.get("/map/result?q=Howard")

def collections(l):
    l.client.get("/collection/result?q=Howard")

def people(l):
    l.client.get("/people/result?q=Howard")

def lists(l):
    l.client.get("/list/result?q=Howard")

class UserBehavior(TaskSet):
    tasks = {search: 1, books: 2, pictures: 3, articles: 4, newspapers: 5, gazettes: 6, music: 7, maps: 8, collections: 9, people: 10, lists: 11}

    def on_start(self):
        search(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
