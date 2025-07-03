from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, index=True)
    message_content = Column(Text)
    is_from_user = Column(Boolean)  # True if from user, False if from bot
    message_type = Column(String)  # text, image, document, etc.
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Message(phone_number='{self.phone_number}', is_from_user='{self.is_from_user}')>"