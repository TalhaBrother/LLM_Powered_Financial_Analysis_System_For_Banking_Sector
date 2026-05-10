from fastapi import FastAPI
from app.routes.loan_route import router as loan_router

app = FastAPI()
app.include_router(loan_router)



