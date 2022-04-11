from flask import flash, request
from flask.views import MethodView
from posts.models import Post
from extentions import db
import timeago
import datetime


class PostResource(MethodView):

    def get(self):
        args = request.args
        location = args.get('location')
        page = args.get('page', 1, type=int)
        per_page = 10
        meters = 10000
        query = f"""
                    SELECT 
                        id,
                        text,
                        timestamp,
                        location
                    FROM post
                    WHERE
                        ST_DWithin('{location}'::geography, ST_MakePoint(ST_X(location), ST_Y(post.location)),{meters}) 
                        limit {per_page} offset {(page-1) * per_page};
                """
        res = db.engine.execute(query)
        output = []
        for row in res:
            row_dict = {
                'id': row[0],
                'text': row[1],
                'timestamp': row[2],

            }
            time_ago = timeago.format(row[2], datetime.datetime.now())
            row_dict['timeago'] = time_ago
            output.append(row_dict)
        return {'data': output, 'meta': {'current_page': page}}


class TweetResource(MethodView):

    def post(self):
        text = request.form['text']
        location = request.form['location']
        data = Post(text=text, location=location)
        db.session.add(data)
        db.session.commit()
        flash("Post Successful!")
        return {'message': 'Post Successful!'}
