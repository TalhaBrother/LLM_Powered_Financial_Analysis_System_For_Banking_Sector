from fastapi import FastAPI
from app.routes.loan import router as loan_router

app = FastAPI()
app.include_router(loan_router)

@app.get("/")
def home():
    return {"message": "UBL System is running!"}

@app.get("/loan")
def get_loan():
    return {"message": "Fetching loan information..."}