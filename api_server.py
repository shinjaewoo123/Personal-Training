'''
	created by Rain.
'''
import sys
import os

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

class RegistUser(Resource):
	def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('my_str_input', type=str)
			parser.add_argument('my_int_input', type=int)
			args = parser.parse_args()

			_myInput = args['my_str_input']
			_myInput2 = args['my_int_input']

			output1 = _myInput * 2
			output2 = _myInput2 * 2

			return {'input1': output1, 'input2': output2}
		except Exception as e:
			return {'error': str(e)}
		
api.add_resource(RegistUser, '/user')

def main(args):
	print(args)

'''
@app.route('/')
def hello_world():
	return 'Hello World!'
'''



if __name__ == '__main__':
	main(sys.argv[1:])

	app.run(debug=True)