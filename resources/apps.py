from flask_restful import Resource

class AppResource(Resource):
    def get(self, id= None):
        if id == None:
            return []
        
        else:
            return {}
        
    def post(self):
        return {"message": "App created successfully"}
    
    def delete(self, id):
        return {"message": "app deleted successfully"}
