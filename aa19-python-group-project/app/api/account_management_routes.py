from flask import Blueprint, request, jsonify,request
from flask_login import login_required, current_user
from app.models import db, Account
from app.forms.account_management_form import AccountManagementForm
from app.utils import success_response, error_response
import json

account_routes = Blueprint("accounts", __name__)

#             GET ROUTES               #
@account_routes.route('/', methods=['GET'])
@login_required
def get_accounts():
    """Fetch all connected accounts for the logged-in user."""
    user_id = current_user.id
    accounts = Account.query.filter_by(user_id=user_id).all()
    return success_response({"accounts": [account.to_dict() for account in accounts]})


#             POST ROUTES              #
@account_routes.route('/', methods=['POST'])
@login_required
def create_account():
    form = AccountManagementForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    form['user_id'].data = current_user.id

    if form.validate_on_submit():
        new_account = Account(
            platform=form.platform.data,
            username=form.username.data,
            settings=form.settings.data,
            user_id=current_user.id  # Automatically set the user ID
        )
        db.session.add(new_account)
        db.session.commit()
        return {"message": {"account": new_account.to_dict()}}, 201
    return {"errors": form.errors}, 400

#             PUT ROUTES               #
@account_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_account(id):
    account = Account.query.get(id)
    if not account or account.user_id != current_user.id:
        return {"errors": "Account not found or unauthorized."}, 404

    form = AccountManagementForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    form['user_id'].data = current_user.id
    
    if form.validate_on_submit():
        account.platform = form.platform.data or account.platform
        account.username = form.username.data or account.username
        account.settings = form.settings.data or account.settings
        db.session.commit()
        return {"message": {"account": account.to_dict()}}, 200
    return {"errors": form.errors}, 400


#             DELETE ROUTES            #
@account_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_account(id):
    """Disconnect a social media account."""
    account = Account.query.get(id)

    if not account or account.user_id != current_user.id:
        return error_response("Account not found or unauthorized", status=404)

    db.session.delete(account)
    db.session.commit()
    return success_response({"message": "Account deleted successfully"})
