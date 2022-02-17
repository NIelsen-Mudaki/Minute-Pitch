from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from . import main
from .forms import PostForm
from ..models import Post, User


@main.route('/')
def index():
    posts = Post.query.all()
    
    return render_template('index.html', posts=posts)
