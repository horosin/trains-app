#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
from datetime import datetime
from trains_dict import trains
from wars_dict import wars
from media_dict import media

app = Flask(__name__)
CORS(app)


@app.route('/trains-app/api/v1.0/trains', methods=['GET'])
def get_all_trains():
    return jsonify({'trains': trains})

@app.route('/trains-app/api/v1.0/trains/<string:train_id>', methods=['GET'])
def get_train(train_id):
    train = [train for train in trains if train['id'] == train_id]
    if len(train) == 0:
        abort(404)
    return(jsonify({'train': train[0]}))

@app.route('/trains-app/api/v1.0/trains_query', methods=['GET'])
def get_train_query_string():
    start_val = request.args.get('start')
    stop_val = request.args.get('stop')
    start_time_val = request.args.get('start_time')
    stop_time_val = request.args.get('stop_time')
    disabled_val = request.args.get('is_disabled')
    sleeping_val = request.args.get('is_sleeping')
    wars_val = request.args.get('is_wars')

    train1 = [train for train in trains if train['start'] == start_val]
    train2 = [train for train in train1 if train['stop'] == stop_val]

    if start_time_val is not None:
        start_time_val = datetime.strptime(start_time_val, '%H:%M')
        train3 = [train for train in train2 if train['start_time'] >= start_time_val] # TODO datetime
    elif stop_time_val is not None:
        train3 = [train for train in train2 if train['stop_time'] <= stop_time_val] # TODO datetime
    else:
        train3 = train2

    if disabled_val:
        train4 = [train for train in train3 if train['is_disabled']]
    else:
        train4 = train3

    if sleeping_val:
        train5 = [train for train in train4 if train['is_sleeping']]
    else:
        train5 = train4

    if wars_val:
        train6 = [train for train in train5 if train['is_wars']]
    else:
        train6 = train5


    return(jsonify({'train': train6}))

@app.route('/trains-app/api/v1.0/wars', methods=['GET'])
def get_all_wars():
    return jsonify({'wars': wars})

@app.route('/trains-app/api/v1.0/media', methods=['GET'])
def get_all_media():
    return jsonify({'media': media})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



if __name__ == '__main__':
    app.run(debug=True)


# scrap youtube videos
# cors (enable communication)
# wyszukiwanie stacji koncowej w stacjach posrednich


#pip3
#flask
#flask_cors