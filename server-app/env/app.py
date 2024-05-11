from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient


app = Flask(__name__)
cors = CORS(app, origins='*')
client = MongoClient('mongodb+srv://deepuVaira:Vaira001*@mycluster.j5rbkwa.mongodb.net/retryWrites=true&w=majority&appName=MyCluster')
db = client["MyDB"]
employeeDB = db["employee"]


@app.route("/api/users", methods = ['GET'])
def getAllUsers():
    return list(employeeDB.find({}, {'_id': False}))

# @app.route("/api/addEmployee", methods = ['POST'])
# def addNewEmployee():
#     result = employeeDB.insert_one({
#        "id": "1002",
#        "firstName": "VairaMuthu",
#        "lastName": "Dhatchinamoorthy",
#        "salaryGrade": "30",
#        "designation": "Web Designer - Analyst",
#        "mobileNumber": "8089799757"
#         })
#     if result:
#             return jsonify({'success': 'Employee updated successfully'}), 200
#     else:
#             return jsonify({'error': 'Employee not found'}), 404
#     return

# @app.route("/api/updateEmployee/<string:id>", methods = ['PUT'])
# def updateEmployee(id):
#     result = employeeDB.find_one_and_update({"id": int(id)}, {"$set": {
#        "firstName": "",
#        "lastName": "",
#        "salaryGrade": "",
#        "designation": "",
#        "mobileNumber": ""
#     }})
#     if result:
#             return jsonify({'success': 'Employee updated successfully'}), 200
#     else:
#             return jsonify({'error': 'Employee not found'}), 404
    
@app.route("/api/deleteEmployee/<string:id>", methods = ['GET', 'DELETE', 'POST'])
def deleteEmployee(id):
    result = employeeDB.find_one_and_delete({"id": int(id)})
    if result:
            return jsonify({'success': 'Employee deleted successfully'}), 200
    else:
            return jsonify({'error': 'Employee not found'}), 404
    

if __name__ == "__main__":
   app.run(port=8080)