from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [
	{
		'name' : 'My store', 
		'items' : [
			{
				'name': 'My item', 
				'price': 15.99
			}
		]
	}
]

"""
From Server Perspective: 
# POST - Used to receive data
# GET - Used to send data back only
"""

# Decorator, tell what the request does
# TO-Do : Learn Decorator

# By default app.route is get request

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
	request_data = request.get_json()
	new_store = {
		'name' : request_data['name'],
		'items': []
	}
	stores.append(new_store)

	return jsonify(new_store)

@app.route('/store/<name>')
def get_store_(name):
	#Iterate over stores and return the store, if none return error stmt
	
	for store_details in stores:
		if store_details['name'] == name:
			return jsonify(store_details)

	return jsonify({"message":"The store doesn't exist"})

@app.route('/store')
def get_store():
	return jsonify({'stores':stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	request_data = request.get_json()
	for store in stores:
		if store['name'] == name:
			new_item = {
				'name': request_data['name'],
				'price': request_data['price']
			}
			store['items'].append(new_item)
			return jsonify(new_item)

	return jsonify({'message':'store not found'})


@app.route('/store/name/item')
def get_items_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify({'items':store['items']})

	return jsonify({'message':'store not found'})


#Tell the app to run
#First argument will be a port
app.run(port=4000)