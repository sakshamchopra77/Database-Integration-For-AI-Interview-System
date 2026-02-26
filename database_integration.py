from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Numeric, Text, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Update these details with your actual PostgreSQL credentials
DATABASE_URL = "postgresql://postgres:password@localhost:5432/interview_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Mapped Tables from your SQL File ---

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    full_name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class InterviewSession(Base):
    __tablename__ = 'interview_sessions'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    start_time = Column(DateTime(timezone=True), server_default=func.now())
    total_risk_score = Column(Numeric(5, 2), default=0.00)
    status = Column(String, default='IN_PROGRESS')

class ObjectDetectionEvent(Base):
    __tablename__ = 'object_detection_events'
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('interview_sessions.id'), nullable=False)
    object_detected = Column(String, nullable=False)
    confidence_score = Column(Numeric(5, 2), nullable=False)
    snapshot_url = Column(Text)

# Initialize and Create Tables
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database Integrated: All tables from SQL file created successfully.")
