from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c87370a82cce712cb31b8abcf9962b56dd263592bea9190f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2096398:Tong881205..@csmysql.cs.cf.ac.uk:3306/c2096398_c2096398_flask'
app.run(debug=True)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes

from flask_admin import Admin
from blog.views import AdminView
from blog.models import User, Post, Comment

#admin = Admin(app,name='Admin panel',template_mode='bootstrap3')
#admin.add_view(AdminView(User, db.session))
#admin.add_view(AdminView(Post, db.session))
#admin.add_view(AdminView(Comment, db.session))

admin = Admin(app, name='Admin panel', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))