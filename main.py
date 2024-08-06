from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from payment_check import lolz_pay

#########################
# BLOCK WITH API ROUTES #
#########################

# create instance of the app
app = FastAPI()
# docs_url=None,
#               redoc_url=None
# openapi_url = None
origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8000",
    "https://mail.google.com",
    "https://google.com",
    "http://grbar.online",
    "https://grbar.online",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # вернуть origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition", "X-Additional-Data"],
)


api_router = APIRouter()

api_router.include_router(lolz_pay, prefix="/bot", tags=["Lolz payment check"])

app.include_router(api_router)
