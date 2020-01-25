from locust import HttpLocust, between, TaskSet


def get_companies(locustio):
    locustio.client.get('/companies')


def get_company(locustio):
    locustio.client.get('/companies/3')


class CompaniesBehavior(TaskSet):
    tasks = {get_companies: 2, get_company: 1}

    def on_start(self):
        get_companies(self)

    def on_stop(self):
        get_company(self)


class TestCompanies(HttpLocust):
    task_set = CompaniesBehavior
    wait_time = between(0.0, 1.0)
