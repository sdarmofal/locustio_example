from random import randint

from locust import HttpLocust, between, TaskSet, task
from locust.contrib.fasthttp import FastHttpLocust


class CompaniesBehavior(TaskSet):

    @task(3)
    def get_companies(locustio):
        locustio.client.get('/companies')

    @task(1)
    def get_company(locustio):
        locustio.client.get(f"/companies/{randint(1,100)}", name="/companies/[id]")


class TestCompanies(FastHttpLocust):
    task_set = CompaniesBehavior
    wait_time = between(0.0, 1.0)
