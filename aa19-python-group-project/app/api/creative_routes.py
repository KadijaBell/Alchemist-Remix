from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Schedule,Creative,User
from app.utils import get_content_source_or_404, success_response, error_response
from app.forms.creative_form import CreativeForm

creative_routes = Blueprint("creatives", __name__)


#             GET ROUTES               #
@creative_routes.route('/', methods=['GET'])
@login_required
def get_creatives():
    user_id = current_user.id
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    creatives = Creative.query.filter_by(user_id=user_id).paginate(page=page, per_page=per_page)

    return success_response({
        'creatives': [creative.to_dict() for creative in creatives.items],
        'page': creatives.page,
        'total_pages': creatives.pages,
        'total_creatives': creatives.total,
    })


#             POST ROUTES              #
@creative_routes.route('/', methods=['POST'])
@login_required
def create_creative():

    form = CreativeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    form.user_id.data = current_user.id

    if form.validate_on_submit():
        schedule = Schedule.query.get(form.schedule_id.data)
        if not schedule or schedule.user_id != current_user.id:
            return error_response('Invalid schedule or unauthorized', 403)

        new_creative = Creative(
            title=form.title.data,
            content=form.content.data,
            content_type=form.content_type.data,
            media=form.media.data,
            schedule_id=form.schedule_id.data,
            user_id=current_user.id,
        )
        db.session.add(new_creative)
        db.session.commit()
        return success_response(new_creative.to_dict(), 201)

    return error_response(form.errors, 400)

#             PUT ROUTES               #
@creative_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_creative(id):

    creative = Creative.query.get(id)

    if not creative or creative.user_id != current_user.id:
        return error_response('Creative not found or unauthorized', 404)

    form = CreativeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    form.user_id.data = current_user.id

    if form.validate_on_submit():
        creative.title = form.title.data or creative.title
        creative.content = form.content.data or creative.content
        creative.content_type = form.content_type.data or creative.content_type
        creative.media = form.media.data or creative.media

        db.session.commit()
        return success_response(creative.to_dict())

    return error_response(form.errors, 400)


#             DELETE ROUTES             #
@creative_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_creative(id):
    creative = Creative.query.get(id)
    if not creative or creative.user_id != current_user.id:
        return {'error': 'Creative not found or unauthorized'}, 404

    db.session.delete(creative)
    db.session.commit()
    return {'message': 'Creative deleted successfully'}


@creative_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_creative(id):
    creative = Creative.query.get(id)
    if not creative or creative.user_id != current_user.id:
        return error_response('Creative not found or unauthorized', 404)
    
    db.session.delete(creative)
    db.session.commit()
    return success_response({'message': 'Creative deleted successfully'})
