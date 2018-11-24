#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
from datetime import datetime
from trains_dict import trains
from wars_dict import wars
from media_dict import media

app = Flask(__name__)


@app.route('/trains-app/api/v1.0/trains', methods=['GET'])
def get_all_trains():
    return jsonify({'trains': trains})

@app.route('/trains-app/api/v1.0/trains/<string:train_id>', methods=['GET'])
def get_train(train_id):
    train = [train for train in trains if train['id'] == train_id]
    if len(train) == 0:
        abort(404)
    return(jsonify({'train': train[0]}))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



if __name__ == '__main__':
    app.run(debug=True)


# scrap youtube videos
# query strings