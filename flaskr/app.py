# from flask import Flask, abort
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from flask_cors import CORS
# import os

# app = Flask(__name__)
# CORS(app)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'mysecret'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
# # app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# login_manager = LoginManager(app)

# @login_manager.unauthorized_handler
# def unauthorized():
#     abort(401)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# from models import *
# from views import *

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
    
from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_cors import CORS
import os

# Flask アプリケーションの初期化
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# データベースとマイグレーションの設定
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# LoginManagerの設定
login_manager = LoginManager()
login_manager.init_app(app)

# ログインが必要なページへのアクセスが認証されていない場合の処理
@login_manager.unauthorized_handler
def unauthorized():
    abort(401)

# ユーザーローダー関数の設定
@login_manager.user_loader
def load_user(user_id):
    # ユーザーをデータベースから取得するロジック
    return User.query.get(int(user_id))  # Userモデルからユーザーを取得する

# エンドポイントを定義
@app.route('/api/login_status')
def login_status():
    return jsonify({'is_authenticated': current_user.is_authenticated})

# モデルとビューのインポート
from models import *
from views import *

# アプリケーションのエントリーポイント
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

