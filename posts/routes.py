from flask import Blueprint
from posts.controller import PostResource, TweetResource

posts = Blueprint('posts', __name__, template_folder='templates', url_prefix='/posts')
posts.add_url_rule('/get_data', 'posts', PostResource.as_view('posts'))
posts.add_url_rule('/tweet', 'tweet', TweetResource.as_view('tweet'))
