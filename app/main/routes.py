from datetime import datetime
from flask import render_template, flash, redirect, url_for, \
	request, g, jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from app import db
from app.main.forms import CommentForm
from app.models import User, Comment
from app.main import bp


@bp.before_app_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.commit() 
	g.locale = str(get_locale())


@bp.route('/', methods=['GET','POST'])
@bp.route('/index', methods=['GET','POST'])
def index():
	# form = CommentForm()
	# if form.validate_on_submit():
	# 	comment = Comment(body=form.comment.data, author=current_user)
	# 	db.session.add(comment)
	# 	db.session.commit()
	# 	flash(_('Your post is now live.'))
	# 	return redirect(url_for('main.index'))
	# page = request.args.get('page', 1, type=int)
	# comments = current_user.followed_comments().paginate(
	# 	page, current_app.config['COMMENTS_PER_PAGE'], False)
	# next_url = url_for('main.index', page=comments.next_num) \
	# 	if comments.has_next else None
	# prev_url = url_for('main.index', page=comments.prev_num) \
	# 	if comments.has_prev else None
	return render_template('index.html', title=_('Home'))#, form=form, 
						   # comments=comments.items, next_url=next_url,
						   # prev_url=prev_url)

@bp.route('/resume')
def resume():
    return render_template('resume.html')#, user=user)
