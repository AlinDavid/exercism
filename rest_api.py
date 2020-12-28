import json

class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if payload: # convert payload to string if it exists
            payload = json.loads(payload)

        output = {'users': []} # create new users object to return 
        for user in enumerate(self.database['users']): # if the user from the db is asked for (payload)
            if user[1]['name'] in payload['users']:
                output['users'].append(self.database['users'][user[0]])

        if url == '/users':
            return json.dumps(output)

    def post(self, url, payload=None):
        if payload:
            payload = json.loads(payload)

        if url == '/iou':
            output = {'users': []}
            for user in self.database['users']:
                amount = payload['amount']
                lender = payload['lender']
                borrower = payload['borrower']
                if user['name'] == lender:
                    user['balance'] += amount
                    if borrower in user['owes']:
                        user['owes'][borrower] -= amount
                        if user['owes'][borrower] <= 0:
                            amount = -(user['owes'][borrower])
                            del user['owes'][borrower]
                        else:
                            amount = 0
                    if borrower in user['owed_by']:
                        user['owed_by'][borrower] += amount
                    else:
                        user['owed_by'][borrower] = amount
                    if user['owed_by'][borrower] <= 0:
                        del user['owed_by'][borrower]
                    output['users'].append(user)
                if user['name'] == borrower:
                    user['balance'] -= amount
                    if lender in user['owed_by']:
                        user['owed_by'][lender] -= amount
                        if user['owed_by'][lender] <= 0:
                            amount = -(user['owed_by'][lender])
                            del user['owed_by'][lender]
                        else:
                            amount = 0
                    if lender in user['owes']:
                        user['owes'][lender] += amount
                    else:
                        user['owes'][lender] = amount
                    if user['owes'][lender] <= 0:
                        del user['owes'][lender]
                    output['users'].append(user)
            return json.dumps(output)

        if url == '/add':
            new_user ={"name": payload['user'] , "owes": {}, "owed_by": {}, "balance": 0.0}
            self.database['users'].append(new_user)
            return json.dumps(new_user)