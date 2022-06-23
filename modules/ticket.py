import json
import requests
from flask import Blueprint, jsonify, request

ticket_blueprint = Blueprint('ticket', __name__)

@ticket_blueprint.route('/createTicket', methods=["POST"])
def createTicket():
    payload = json.loads(request.data)
    print(payload)

    url = "https://<instanceName>.servicenow.com/api/now/table/<tableName>"
    user = "username"
    password = "password"

    headers = {"Content-Type":"application/xml","Accept":"application/json"}

    data = {
        "location": "<long, lat> or <site name>",
        "urgency": 2,
        "impact": 2,
        "description": "longer ticket description",
        "group_list": "",
        "priority": "3",
        "sys_mod_count": "0",
        "business_service": "<something>",
        "sys_updated_on": "2016-01-22 14:28:24",
        "number": "<something>",
        "category": "<something>",
        "incident_state": "1",
        "company": "<something>",
        "active": "true",
        "assignment_group": {
            "link": "https://instance.servicenow.com/api/now/table/sys_user_group/<something>",
            "value": "<something>"
        },
        "caller_id": "<something>",
        "knowledge": "false",
        "state": "1",
        "child_incidents": "<maybe the # of occurrences>",
        "short_description": "Unable to connect to office wifi",
        "problem_id": "",
        "sys_id": "c537bae64f411200adf9f8e18110c76e",
        "approval": "not requested",
        "caused_by": "<something>",
        "severity": "3",
        "sys_created_by": "admin",
        "resolved_at": "",
        "assigned_to": "",
        "business_stc": "",
        "wf_activity": "",
        "sys_domain_path": "/",
        "cmdb_ci": "",
        "subcategory": "",
        "rejection_goto": "",
        "sys_class_name": "incident",
        "watch_list": "",
        "time_worked": "",
        "contact_type": "phone",
        "escalation": "0",
        "comments": ""
    }

    response = requests.post(
        url,
        auth = (user, password),
        headers = headers,
        data = data
    )

    if (response.status_code != 201):
        return jsonify(status = response.status_code, headers=response.headers, response=response.json())
    
    print(response.json())
    return jsonify(status=response.status_code, response = response.json())

@ticket_blueprint.route('/getTicket', methods=["POST"])
def getTicket():
    payload = json.loads(request.data)
    print(payload)
    return jsonify(ticketID="<some id>", ticketStatus="open", ticketName="ticketName", ticketDescription="ticketDescription", otherData="otherData")