# app/models/log.py
from datetime import datetime
from app import db  # app에서 db를 임포트

class Log(db.Model):
    __tablename__ = 'log'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    incident_id = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)  # Incident 모델 참조
    service = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'incident_id': self.incident_id,
            'service': self.service,
            'status': self.status,
            'message': self.message
        }

    def __repr__(self):
        return f"<Log id={self.id} service={self.service} status={self.status}>"
