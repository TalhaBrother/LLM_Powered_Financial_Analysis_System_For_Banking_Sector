from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()

class LoanApplication(BaseModel):
    applicant_name: str
    amount: int
          

@router.post("/loan/apply")
def apply_loan(loan_application: LoanApplication):
   
    if loan_application.amount > 10000:
        return {"message": "Loan application rejected: Amount exceeds limit."}
    return {"message": "Loan application approved!"}