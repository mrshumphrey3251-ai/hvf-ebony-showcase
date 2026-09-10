# SENTINEL ULTRA - SOVEREIGN ENGINE IGNITION [PUBLIC SPECIFICATION]
# Target: Local API Gateway (Mock Endpoints)
# Execution: Localhost (127.0.0.1)

Write-Host "[*] INITIATING SOVEREIGN ENGINE IGNITION SEQUENCE..." -ForegroundColor Cyan

# Verify local dependencies
if (!(Get-Command uvicorn -ErrorAction SilentlyContinue)) {
    Write-Host "[*] Installing local Uvicorn server..." -ForegroundColor Yellow
    python -m pip install fastapi uvicorn pydantic
}

Write-Host "[*] Booting Sentinel Ultra API Gateway (Sanitized Spec) on Localhost..." -ForegroundColor Green
Write-Host "[*] Techno Exponent: Connect Flutter UI to http://127.0.0.1:8000" -ForegroundColor Yellow

# Launch the sanitized API Gateway
uvicorn api_gateway.main:app --host 127.0.0.1 --port 8000 --reload
