from pydantic import BaseModel

class Loan_Request(BaseModel):
    loan_id: int
    borrower_name: str
    amount: float
    