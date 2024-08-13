from sqlalchemy.orm import Session
from Database import User, Message

def create_user(db: Session, data):
    user = User(**data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_message(db: Session, data):
    message = Message(**data)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_user(db: Session, telegram_user_id):
    return db.query(User).filter(User.telegram_user_id == telegram_user_id).first()


def get_messages(db: Session, user_id: int):
    return db.query(Message).filter(Message.user_id == user_id).all()