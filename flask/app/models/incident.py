# app/models/incident.py
from datetime import datetime
from enum import Enum
from app import db

class Incident(db.Model):
    __tablename__ = 'incident'

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    detail = db.Column(db.Text, nullable=False)
    occurred_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    restored_at = db.Column(db.DateTime, nullable=True)
    logs = db.relationship('Log', backref='incident', lazy=True)

    def __repr__(self):
        return f"<Incident id={self.id} service={self.service} status={self.status}>"

class IncidentStatus(Enum):
    NOTICED = "Noticed"          # 문제 발생
    INVESTIGATING = "Investigating"  # 조사 중
    RESOLVING = "Resolving"      # 해결 중
    RESTORED = "Restored"        # 정상 복구됨
