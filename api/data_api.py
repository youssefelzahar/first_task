import flask
from flask import Flask, request, jsonify
from sklearn.datasets import load_iris  
import pandas as pd
app = flask.Flask(__name__)

iris = load_iris()
df_columns = iris.feature_names + ['target']
df_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_data['target'] = iris.target
data_store = {"df": df_data}

@app.route('/data', methods=['POST'])
def add_data():
    new_record = request.get_json()

    expected_keys = iris.feature_names + ['target']
    if not all(key in new_record for key in expected_keys):
        return jsonify({"error": f"Missing fields. Required: {expected_keys}"}), 400

    new_row = pd.DataFrame([new_record])
    data_store["df"] = pd.concat([data_store["df"], new_row], ignore_index=True)

    return jsonify({"message": "Record added successfully", "data": new_record}), 201

@app.route('/data',methods=['GET'])
def get_data():
    return jsonify(data_store["df"].to_dict(orient='records')), 200


    df=data_store['df']
    if index not in len(df):
        return jsonify("not invalid")
    data_store['df']=df.drop(index).reset_index(drop=True)
    return jsonify({"message": f"Record at index {index} deleted successfully"}), 200



if __name__ == '__main__':
    app.run(debug=True)