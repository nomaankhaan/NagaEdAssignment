# Task 1

Contact Form Task
This project implements a simple, responsive contact form with HTML, CSS, and JavaScript.

1. Clone this repository:
   ```
   git clone https://github.com/nomaankhaan/NagaEdAssignment.git
   cd Task 1
   ```
2. Open index.html and click on go live to open the contact form page

# Task 2

This project is a simple RESTful API for managing educational resources, specifically courses. It provides basic CRUD (Create, Read, Update, Delete) operations for course management.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/nomaankhaan/NagaEdAssignment.git
   cd Task 2
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the API server:
   ```
   python app.py
   ```

2. The API will be available at `http://localhost:5000`

## API Testing with Postman

[Postman](https://www.postman.com/) is a popular API client that makes it easy to create, share, test, and document APIs. Follow these steps to test the Educational Resources API using Postman:

1. **Install Postman**: 
   - Download and install Postman from [https://www.postman.com/downloads/](https://www.postman.com/downloads/)

2. **Launch Postman and create a new request**:
   - Click on the "+" button to create a new request tab

4. **Test GET all courses**:
   - Set the request type to GET
   - Enter the URL: `http://localhost:5000/courses`
   - Click "Send"
   - You should receive a 200 OK response with an empty list (assuming no courses have been added yet)

5. **Test POST a new course**:
   - Set the request type to POST
   - Enter the URL: `http://localhost:5000/courses`
   -  In the "Headers" tab, add: Key: Content-Type; Value: application/json
   - Go to the "Body" tab, select "raw" and choose "JSON" from the dropdown
   - Enter the following JSON:
     ```json
     {
       "title": "Introduction to Python",
       "description": "Learn the basics of Python programming",
       "duration": "4 weeks"
     }
     ```
   - Click "Send"
   - You should receive a 201 Created response with the newly created course object, including its ID

6. **Test GET a specific course**:
   - Copy the `id` from the response of the POST request
   - Set the request type to GET
   - Enter the URL: `{{base_url}}/courses/<paste-course-id-here>`
   - Click "Send"
   - You should receive a 200 OK response with the course details

7. **Test PUT to update a course**:
   - Set the request type to PUT
   - Enter the URL: ``http://localhost:5000/courses/<paste-course-id-here>`
   - In the "Body" tab, enter the following JSON:
     ```json
     {
       "title": "Advanced Python Programming"
     }
     ```
   - Click "Send"
   - You should receive a 200 OK response with the updated course details

8. **Test DELETE a course**:
   - Set the request type to DELETE
   - Enter the URL: `http://localhost:5000/courses<paste-course-id-here>`
   - Click "Send"
   - You should receive a 200 OK response with a success message
