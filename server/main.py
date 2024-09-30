from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from v1.router import router as v1_router

app = FastAPI()

# Add CORS middleware to allow requests from your frontend (adjust URL if necessary)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include your router
app.include_router(v1_router, prefix="/v1")

# Root route
@app.get("/")
def root():
    return {"message": "Hello, Welcome to Python FASTAPI"}
