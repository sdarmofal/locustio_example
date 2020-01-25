import json

from faker import Faker
from falcon import HTTP_200


class Companies:
    COMPANIES_COUNT = 200

    def __init__(self):
        self.fake = Faker('pl_PL')

    def on_get(self, req, res):
        companies = []
        for i in range(1, self.COMPANIES_COUNT):
            companies.append({
                'id': i,
                'regon': self.fake.regon(),
                'name': self.fake.company()
            })

        res.status = HTTP_200
        res.body = json.dumps(companies)
