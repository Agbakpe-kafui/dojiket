from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, users, events, registrations, venues
from .database import engine
from .models import users as user_models, events as event_models, venues as venue_models, registrations as registration_models

# Create database tables
user_models.Base.metadata.create_all(bind=engine)
event_models.Base.metadata.create_all(bind=engine)
venue_models.Base.metadata.create_all(bind=engine)
registration_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Event Registration API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(events.router, prefix="/api/events", tags=["Events"])
app.include_router(registrations.router, prefix="/api/registrations", tags=["Registrations"])
app.include_router(venues.router, prefix="/api/venues", tags=["Venues"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Event Registration API"} 