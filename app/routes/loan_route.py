from fastapi import APIRouter
from app.services.loan_service import Loan_Approval
from app.models.loan_model import Loan_Request

router = APIRouter()



@router.post("/loan/approve/{loan_id}")
def Approve_Loan(loan:Loan_Request):
    
    result = Loan_Approval(loan.loan_id, loan.amount)
    return result