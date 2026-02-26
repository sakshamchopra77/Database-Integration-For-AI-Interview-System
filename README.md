# Database-Integration-For-AI-Interview-System
AI Interview Proctoring & Evaluation System
This repository features a Python-based database integration layer for an automated interview proctoring system. It bridges the gap between raw PostgreSQL data and application logic, specifically designed to monitor candidate behavior and evaluate interview performance using AI.


Table,                                                   Purpose

users,                      Manages candidate profiles, including full names and authentication data.
interview_sessions,         The central hub tracking session status, timing, and cumulative risk scores.
object_detection_events,    Logs AI-detected items (like cell phones) with confidence levels and snapshot URLs.
face_pose_events,           Tracks suspicious physical behavior, duration, and severity levels.
audio_transcripts,          Stores text content and timestamps for candidate audio responses.
answer_evaluations,         Links candidate answers to AI-generated relevance scores and feedback.
