from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Schedule,Creative,User
from app.utils import get_content_source_or_404, success_response, error_response
from app.forms.schedule_form import ScheduleForm

schedule_routes = Blueprint("schedules", __name__)


#             GET ROUTES               #

# Get all schedules
@schedule_routes.route('/', methods=['GET'])
@login_required
def get_schedules():
    user_id = current_user.id
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = Schedule.query.filter_by(user_id=user_id)

    if start_date:
        query = query.filter(Schedule.start_time >= start_date)
    if end_date:
        query = query.filter(Schedule.end_time <= end_date)

    schedules = query.all()
    return success_response({'schedules': [schedule.to_dict() for schedule in schedules]})


#            POST ROUTES              #
#Create a new schedule
@schedule_routes.route('/', methods=['POST'])
@login_required
def create_schedule():
    form = ScheduleForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        if form.start_time.data >= form.end_time.data:
            return error_response('Start time must be earlier than end time', 400)

        new_schedule = Schedule(
            title=form.title.data,
            description=form.description.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            user_id=current_user.id,
        )
        db.session.add(new_schedule)
        db.session.commit()
        return success_response(new_schedule.to_dict(), 201)

    return error_response(form.errors, 400)


#            PUT ROUTES               #
#update a schedule
@schedule_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_schedule(id):
    schedule = Schedule.query.get(id)
    if not schedule or schedule.user_id != current_user.id:
        return error_response('Schedule not found or unauthorized', 404)

    form = ScheduleForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        schedule.title = form.title.data or schedule.title
        schedule.description = form.description.data or schedule.description
        schedule.start_time = form.start_time.data or schedule.start_time
        schedule.end_time = form.end_time.data or schedule.end_time

        db.session.commit()
        return success_response(schedule.to_dict())

    return error_response(form.errors, 400)

#            DELETE ROUTES             #

@schedule_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_schedule(id):
    schedule = Schedule.query.get(id)
    if not schedule or schedule.user_id != current_user.id:
        return error_response('Schedule not found or unauthorized', 404)

    db.session.delete(schedule)
    db.session.commit()
    return success_response({'message': 'Schedule deleted successfully'})

