from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Schedule
from app.forms.schedule_form import ScheduleForm
from app.utils import success_response, error_response

schedule_routes = Blueprint("schedules", __name__)

#            GET ROUTES             #
@schedule_routes.route("/", methods=["GET"])
@login_required
def get_schedules():
    user_id = current_user.id
    schedules = Schedule.query.filter_by(user_id=user_id).all()
    return success_response({"schedules": [schedule.to_dict() for schedule in schedules]})

#            POST ROUTES             #
@schedule_routes.route("/", methods=["POST"])
@login_required
def create_schedule():
    form = ScheduleForm()
    

    if form.validate_on_submit():
        new_schedule = Schedule(
            title=form.title.data,
            description=form.description.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            user_id=current_user.id,
        )
        db.session.add(new_schedule)
        db.session.commit()
        return success_response({"schedule": new_schedule.to_dict()}, 201)

    return error_response(form.errors, 400)

#             PUT ROUTES             #
@schedule_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_schedule(id):
    schedule = Schedule.query.get(id)
    if not schedule or schedule.user_id != current_user.id:
        return error_response("Schedule not found or unauthorized", 404)

    form = ScheduleForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        schedule.title = form.title.data
        schedule.description = form.description.data
        schedule.start_time = form.start_time.data
        schedule.end_time = form.end_time.data
        db.session.commit()
        return success_response({"schedule": schedule.to_dict()})

    return error_response(form.errors, 400)

#          DELETE  ROUTES             #
@schedule_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_schedule(id):
    schedule = Schedule.query.get(id)
    if not schedule or schedule.user_id != current_user.id:
        return error_response("Schedule not found or unauthorized", 404)

    db.session.delete(schedule)
    db.session.commit()
    return success_response({"message": "Schedule deleted successfully"})
