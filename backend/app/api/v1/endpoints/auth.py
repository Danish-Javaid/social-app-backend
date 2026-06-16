from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.schemas.user import UserCreate
from app.schemas.auth import LoginRequest, TokenResponse, RefreshRequest
from app.schemas.otp import OTPVerifyRequest, OTPResendRequest, OTPResponse
from app.services.auth_service import AuthService
from app.services.otp_service import OTPService
from app.services.user_service import UserService
from app.db.enums import OTPType
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    return AuthService.register(db, user_create)

@router.post("/verify-email")
def verify_email(request: OTPVerifyRequest, db: Session = Depends(get_db)):
    return AuthService.verify_email_otp(db, request.email, request.otp_code)

@router.post("/resend-otp", response_model=OTPResponse)
def resend_otp(request: OTPResendRequest, db: Session = Depends(get_db)):
    user = UserService.get_user_by_email(db, request.email)
    if not user:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="User not found")
    OTPService.send_otp(db, str(user.id), OTPType.email_verification)
    return OTPResponse(message=f"OTP sent to {request.email}", email=request.email)

@router.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest, request: Request, db: Session = Depends(get_db)):
    ip_address = request.client.host if request.client else "unknown"
    user_agent = request.headers.get("user-agent", "unknown")
    return AuthService.login(db, credentials.email, credentials.password, ip_address, user_agent)

@router.post("/refresh", response_model=TokenResponse)
def refresh_token(request: RefreshRequest, db: Session = Depends(get_db)):
    return AuthService.refresh_access_token(db, request.refresh_token)

@router.post("/logout")
def logout(request: RefreshRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return AuthService.logout(db, str(current_user.id), request.refresh_token)
