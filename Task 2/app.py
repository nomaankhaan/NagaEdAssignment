from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import uuid

app = Flask(__name__)
api = Api(app)

# Dictionary data structure as a storage for courses
courses = {}

class Course(Resource):
    def get(self, course_id):
        course = courses.get(course_id)
        if course:
            return jsonify(course)
        return {"message": "Course not found"}, 404

    def put(self, course_id):
        if course_id not in courses:
            return {"message": "Course not found"}, 404
        
        data = request.get_json()
        courses[course_id].update(data)
        return jsonify(courses[course_id])

    def delete(self, course_id):
        if course_id in courses:
            del courses[course_id]
            return {"message": "Course deleted successfully"}, 200
        return {"message": "Course not found"}, 404

class CourseList(Resource):
    def get(self):
        return list(courses.values())

    def post(self):
        data = request.get_json()
        if not all(key in data for key in ('title', 'description', 'duration')):
            return {"message": "Missing required fields"}, 400
        
        course_id = str(uuid.uuid4())
        new_course = {
            "id": course_id,
            "title": data['title'],
            "description": data['description'],
            "duration": data['duration']
        }
        courses[course_id] = new_course
        return new_course, 201

api.add_resource(CourseList, '/courses')
api.add_resource(Course, '/courses/<string:course_id>')

if __name__ == '__main__':
    app.run(debug=True)