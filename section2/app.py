from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'srikanth'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help='This field cannot be blank!')
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda item: item['name'] == name,items),None)
        return {'item':item}, 200 if item else 400
    
    def post(self,name):
        if next(filter(lambda item: item['name'] == name,items),None):
            return {'message':'An item with name {} already exists'.format(name)}, 400

        data = parser.parse_args()
        
        request_data = request.get_json()
        item = {'name':name,'price':request_data['price']}
        items.append(item)
        return item, 201
    
    def delete(self,name):
        item = next(filter(lambda item: item['name'] == name,items),None)
        if item:
            items.remove(item)
        return {'message':'item deleted'}

    def put(self,name):
        data = parser.parse_args()

        item = next(filter(lambda item: item['name'] == name,items),None)
        if item:
            item.update(data)
        else:
            item = {'name':name,'price':data['price']}
            items.append(item)
        return item

class ItemList(Resource):
    def get(self):
        return {'items':items}
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items/')

app.run(port=5000,debug=True)