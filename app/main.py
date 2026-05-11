from fastapi import FastAPI
from .routes.loan_route import router as loan_router
from .database import engine,Base


app = FastAPI()
app.include_router(loan_router)


Base.metadata.create_all(bind=engine)
@app.get("/")
def connect():
    return {"message": "PostgreSQL is connected!"}
