# Simple REST API TODO list
Developed using Python Flask, in a bid to try and learn this way of creating REST APIs. 

# Specifications
The API stores specific tasks in a TODO list, with task description and a summary of the task. The task data is stored as JSON.
The API serves two endpoints, `/todo` and `/todo/ {id}`, where `{id}`is provided to the endpoint and refers to the id within the database. <br>
The API currenctly utilizes a `.db` file to store the data provided to the API - the file resides within the *instance* folder. 

## Endpoint `/todo`
To invoke the `/todo` endpoint, it is simply appended at the end of a url (*127.0.0.1:5000*).<br>The endpoint only works with **GET** requests.
<br>The **GET** request will return all the todo tasks stored in the `.db` file. 
<br><br>
**Example URL:** `http://127.0.0.1:5000/todo`<br>
**Example Response:**
```json
{
    "1": {
        "task": "this is the first task",
        "summary": "summary is updated"
    },
    "2": {
        "task": "brew coffee",
        "summary": "summary is updated"
    }
}
```


## Endpoint `todo/{id}`
To invoke the `/todo/{id}` endpoint the `{id}` needs to be a recognized ID within the database. <br>
Generally the `{id}` follows an incrementation, but this is not enforced as far as I understand.
<br>This endpoint support **GET, POST, PUT,** and **DELETE** requests.
<br><br>
**Example URL:** `http://127.0.0.1:500/todo/1`<br>
**Example Response:**
```json
{
    "id": 1,
    "task": "this is the first task",
    "summary": "summary is updated"
}
```
# References

**Videos followed to create the baseline of the code base**: 
https://www.youtube.com/watch?v=kENidSltTuA&list=PLS1QulWo1RIYbSv5_R2I_QbAcvbyqBCun

**Additionally the documentation for the Python Libraries Flask and Flask_RESTful was used**
Flask: https://flask.palletsprojects.com/en/3.0.x/
<br>
Flask_RESTful: https://flask-restful.readthedocs.io/en/latest/

