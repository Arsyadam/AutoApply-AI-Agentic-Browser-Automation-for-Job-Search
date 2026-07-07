"""Pydantic API schemas -- request/response models for all endpoints."""

from app.schemas.analytics import (
    ApplicationFunnelData,
    ATSScoreDistribution,
    DashboardStats,
    LLMUsageStats,
    TimelineEntry,
)
from app.schemas.admin import SystemIssueResponse
from app.schemas.application import (
    ApplicationBatchCreate,
    ApplicationBulkApprove,
    ApplicationCreate,
    ApplicationIntervention,
    ApplicationListResponse,
    ApplicationResponse,
    ApplicationStatusUpdate,
    CoverLetterResponse,
)
from app.schemas.auth import RegisterRequest, TokenResponse, UserResponse, WSTicketResponse
from app.schemas.job import (
    JobAnalysisResponse,
    JobListingResponse,
    JobListResponse,
    JobSearchRequest,
)
from app.schemas.resume import (
    ResumeGenerateRequest,
    ResumeListResponse,
    ResumeResponse,
    ResumeScoreRequest,
    ResumeScoreResponse,
    ResumeUploadResponse,
)
from app.schemas.settings import LLMProviderStatus, SettingsResponse, SettingsUpdate

__all__ = [
    "ATSScoreDistribution",
    # application
    "ApplicationBatchCreate",
    "ApplicationBulkApprove",
    "ApplicationCreate",
    # analytics
    "ApplicationFunnelData",
    "ApplicationListResponse",
    "ApplicationResponse",
    "ApplicationStatusUpdate",
    "ApplicationIntervention",
    "CoverLetterResponse",
    "DashboardStats",
    # job
    "JobAnalysisResponse",
    "JobListResponse",
    "JobListingResponse",
    "JobSearchRequest",
    # settings
    "LLMProviderStatus",
    "LLMUsageStats",
    # resume
    "ResumeGenerateRequest",
    "ResumeListResponse",
    "ResumeResponse",
    "ResumeScoreRequest",
    "ResumeScoreResponse",
    "ResumeUploadResponse",
    "SettingsResponse",
    "SettingsUpdate",
    "SystemIssueResponse",
    "TimelineEntry",
    "TokenResponse",
    "RegisterRequest",
    "UserResponse",
    "WSTicketResponse",
]
