import json

from faker import Faker
from falcon import HTTP_200, HTTP_404


class Companies:
    COMPANIES_COUNT = 200

    def __init__(self):
        self.fake = Faker('pl_PL')
        companies = []
        for i in range(0, self.COMPANIES_COUNT - 1):
            companies.append({
                'id': i,
                'regon': self.fake.regon(),
                'name': self.fake.company()
            })
        self.companies = companies

    def on_get(self, req, res):
        res.status = HTTP_200
        res.body = json.dumps(self.companies)

    def on_get_single(self, req, res, company_id: int):
        try:
            company = self.companies[company_id]
        except IndexError:
            res.status = HTTP_404
            return

        res.status = HTTP_200
        res.body = json.dumps(company)
