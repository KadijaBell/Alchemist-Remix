from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Creative, Schedule
from app.forms.creative_form import CreativeForm
from app.utils import success_response, error_response

creative_routes = Blueprint("creatives", __name__)

#          GET ROUTES             #
@creative_routes.route("/", methods=["GET"])
@login_required
def get_creatives():
    user_id = current_user.id
    creatives = Creative.query.filter_by(user_id=user_id).all()
    return success_response({"creatives": [creative.to_dict() for creative in creatives]})

#             POST ROUTES             #
@creative_routes.route("/", methods=["POST"])
@login_required
def create_creative():
    form = CreativeForm()

    if form.validate_on_submit():
        schedule = Schedule.query.get(form.schedule_id.data)
        if not schedule or schedule.user_id != current_user.id:
            return error_response("Invalid schedule or unauthorized", 404)

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
        return success_response({"creative": new_creative.to_dict()}, 201)

    return error_response(form.errors, 400)

#             PUT ROUTES            #
@creative_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_creative(id):
    creative = Creative.query.get(id)
    if not creative or creative.user_id != current_user.id:
        return {'error': 'Creative not found or unauthorized'}, 404

    # Use the form for validation
    form = CreativeForm(data=request.get_json())
    form['csrf_token'].data = request.cookies['csrf_token']


    if form.validate():
        creative.title = form.data.get('title', creative.title)
        creative.content = form.data.get('content', creative.content)
        creative.content_type = form.data.get('content_type', creative.content_type)
        creative.media = form.data.get('media', creative.media)
        creative.schedule_id = form.data.get('schedule_id', creative.schedule_id)

        db.session.commit()
        return {'message': {'creative': creative.to_dict()}}
    return {'error': form.errors}, 400

#            DELETE ROUTES             #
@creative_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_creative(id):
    creative = Creative.query.get(id)
    if not creative or creative.user_id != current_user.id:
        return error_response("Creative not found or unauthorized", 404)

    db.session.delete(creative)
    db.session.commit()
    return success_response({"message": "Creative deleted successfully"})
