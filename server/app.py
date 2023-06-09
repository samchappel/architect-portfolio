from flask import request, make_response, session
from flask_restful import Api, Resource
from flask_login import current_user
from models import User, PortfolioGrid, ProjectDetail, db
from config import app, api, bcrypt, login_manager
from datetime import datetime
from werkzeug.utils import secure_filename
import os

login_manager.init_app(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        response = make_response(users, 200)
        return response

    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if User.query.filter_by(username=username).first():
            return {'error': 'Username already in use'}, 409

        new_user = User(username=username, password=password, first_name=first_name, last_name=last_name)

        db.session.add(new_user)
        db.session.commit()

        return new_user.to_dict(), 201


api.add_resource(Users, '/users')


class PortfolioGrids(Resource):
    def get(self):
        portfolio_grid_list = [portfolio_grid.to_dict() for portfolio_grid in PortfolioGrid.query.all()]
        response = make_response(portfolio_grid_list, 200)
        return response

    def post(self):
        data = request.get_json()
        highlight_image = data.get('highlight_image')
        title = data.get('title')
        preview = data.get('preview')

        new_portfolio_grid = PortfolioGrid(highlight_image=highlight_image, title=title, preview=preview)

        db.session.add(new_portfolio_grid)
        db.session.commit()

        return new_portfolio_grid.to_dict(), 201


api.add_resource(PortfolioGrids, '/portfoliogrids')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class ProjectDetails(Resource):
    def get(self):
        project_details_list = [project_details.to_dict() for project_details in ProjectDetail.query.all()]
        response = make_response(project_details_list, 200)
        return response

    def post(self):
        image = request.files.get('image')
        if not image or not allowed_file(image.filename):
            return make_response({'message': 'No file or unsupported file type'}, 400)

        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        image_path = f'/uploads/{filename}'
        

        data = request.form
        grid_id = data.get('grid_id')
        title = data.get('title')
        description = data.get('description')

        new_project_detail = ProjectDetail(grid_id=grid_id, title=title, description=description, image=image_path)

        db.session.add(new_project_detail)
        db.session.commit()

        return new_project_detail.to_dict(), 201


api.add_resource(ProjectDetails, '/projectdetails')


if __name__ == '__main__':
    app.run(port=5000, debug=True)