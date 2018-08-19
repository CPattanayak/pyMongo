from flask_restful import Resource, reqparse

from model.todo import TodoModel


class TodoResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('completed',
                        type=bool,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('completedAt',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!")
    def post(self):
        data = TodoResource.parser.parse_args()
        item=TodoModel(**data)
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.find_by_name(data.get('text')) , 201

    def get(self):
         return TodoModel.find_all() , 201

