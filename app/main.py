from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.api.whatsapp import router as whatsapp_router
from app.api.appointments import router as appointments_router
from app.api.leads import router as leads_router
from config.settings import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="WellnessConnect API",
    description="AI-Powered Health Concierge Platform",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(whatsapp_router, prefix="/webhook", tags=["WhatsApp"])
app.include_router(appointments_router, prefix="/api", tags=["Appointments"])
app.include_router(leads_router, prefix="/api", tags=["Leads"])

@app.get("/")
async def root():
    return {"message": "WellnessConnect API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)