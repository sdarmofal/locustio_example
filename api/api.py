import falcon

from api.endpoints import Companies

app = falcon.API()

companies = Companies()

app.add_route('/companies', companies)
