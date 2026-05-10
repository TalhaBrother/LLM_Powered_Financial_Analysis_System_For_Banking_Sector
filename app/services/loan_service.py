def Loan_Approval(loan_id: int, amount: float):
   
    if amount > 10000:
        return {
            "approved": False,
            "message": f"Loan with ID {loan_id} has been rejected due to high amount."
            }
    
    return {
            "approved": True,
            "message": f"Loan with ID {loan_id} has been approved."
            }