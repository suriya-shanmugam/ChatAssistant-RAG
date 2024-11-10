from flask import Flask, jsonify, request, render_template
from smarthub import Query_Handler 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define a route for the homepage
@app.route('/')
def computeresponse():
    return render_template('index.html')


@app.route('/api/query', methods=['POST'])
def query_model():
    
    data = request.get_json()
    user_query = data.get("query")
    print(user_query)
    
    response = Query_Handler.process_query(user_query)
    
    return jsonify({
            "data": response,
            "message": "Query processed successfully",
            "status": 200
    }), 200
    



@app.route('/api/data', methods=['GET'])
def get_data():
    
    #testing
    input_query = "Explain increase prices impact on food security"
    response = Query_Handler.process_query(input_query)
    
    sample_data = {
        "code": "200",
        "description": response
    }
    
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)
