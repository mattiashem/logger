from flask import Flask, request, jsonify
import json
from prometheus_flask_exporter import PrometheusMetrics

#Custom
from dbKafka import addToKafka


app = Flask(__name__)
metrics = PrometheusMetrics(app)


#Start
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

#The logs endpoint
@app.route('/log',  methods=['PUT'])
def log():
    #Lets verify we have valid json 
    try:
        data = json.loads(request.data)
        print(data)
        #Add data to kafka
        addToKafka(data)
        return 'OK', 200
    except:
        return 'Invalid JSON', 400


#
# This is the check to keep the pod alive
# if this fails k8s will restart the pod
@metrics.do_not_track()
@app.route('/health', methods=['GET'])
def health():
    return 'Everything is Good!'

#
# This is the check that lets the pod accepts trafffic
# if this fails k8s will not send any more traffic to this pod
@metrics.do_not_track()
@app.route('/ready',  methods=['GET'])
def ready():
    return 'Im ready to work!'


#
# /metrics endpint is alive and send prometheus metrics
#  
#
#