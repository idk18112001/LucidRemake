from datetime import datetime
from app import db

class Indicator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100))  # Economic, Sentiment, Behavioral
    current_value = db.Column(db.Float)
    trend = db.Column(db.String(50))  # up, down, stable
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    source_url = db.Column(db.String(500))
    
    def __repr__(self):
        return f'<Indicator {self.name}>'

class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    current_value = db.Column(db.Float)
    change_percentage = db.Column(db.Float)
    trend = db.Column(db.String(50))  # up, down, stable
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Metric {self.name}>'

class IndicatorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    indicator_id = db.Column(db.Integer, db.ForeignKey('indicator.id'), nullable=False)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    indicator = db.relationship('Indicator', backref=db.backref('data_points', lazy=True))

class MetricData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metric_id = db.Column(db.Integer, db.ForeignKey('metric.id'), nullable=False)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    metric = db.relationship('Metric', backref=db.backref('data_points', lazy=True))