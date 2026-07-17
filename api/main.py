from fastapi import FastAPI

from api.telemetry_api import get_latest_telemetry
from api.status_api import get_vehicle_status
from api.vehicle_api import get_vehicle_info

app = FastAPI(
    title="Smart Telemetry ECU Simulation API",
    description="Automotive ECU Telemetry REST API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Smart Telemetry ECU Simulation API is running successfully."
    }


@app.get("/telemetry")
def telemetry():
    return get_latest_telemetry()


@app.get("/status")
def status():
    return get_vehicle_status()


@app.get("/vehicle")
def vehicle():
    return get_vehicle_info()


@app.post("/start")
def start_simulation():
    return {
        "status": "Simulation Started",
        "engine": "ON",
        "can_bus": "CONNECTED"
    }


@app.post("/stop")
def stop_simulation():
    return {
        "status": "Simulation Stopped",
        "engine": "OFF",
        "can_bus": "DISCONNECTED"
    }