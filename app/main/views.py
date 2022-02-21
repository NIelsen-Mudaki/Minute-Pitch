from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from . import main
from .forms import PostForm
from ..models import Post, User


@main.route('/')
def index():
    
    title = 'Minute Pitch | Get a minute to pitch your idea'
    return render_template('index.html',title=title)

@main.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    user = current_user
    return render_template('posts.html', posts=posts, user=user)

@main.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        user_id = current_user.id
        post_object = Post(post=post, title=title, user_id=user_id)
        post_object.save()

        return redirect(url_for('main.index'))
    else:
        return render_template('pitch.html', form=form)

@main.route('/user')
@login_required
def user():
    username = User.username
    user = User.query.filter_by(username=username).first()
    if user is None:
        return ('User not found')
    return render_template('user.html', user=user)
