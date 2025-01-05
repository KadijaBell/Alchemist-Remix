from app.models import db, Account

def seed_accounts():
    account1 = Account(
        user_id=1,
        platform='Twitter',
        username='@demo_user',
        settings={'notifications': True, 'theme': 'dark'}
    )
    account2 = Account(
        user_id=1,
        platform='Instagram',
        username='demo_user_ig',
        settings={'auto_post': False}
    )

    db.session.add_all([account1, account2])
    db.session.commit()

def undo_accounts():
    db.session.execute('DELETE FROM accounts;')
    db.session.commit()
