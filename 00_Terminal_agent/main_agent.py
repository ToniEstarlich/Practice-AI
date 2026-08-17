from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(
    title="Hello Techne",
    description="A beautiful FastAPI website built by TECHNE 🤖",
    version="1.0.0",
)


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Hello Techne</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;

            background: linear-gradient(
                135deg,
                #0f0c29,
                #302b63,
                #24243e
            );

            min-height: 100vh;

            display: flex;
            align-items: center;
            justify-content: center;

            color: white;
        }

        .container {
            text-align: center;
            padding: 2rem;

            animation: fadeIn 1s ease-in-out;
        }

        @keyframes fadeIn {

            from {
                opacity: 0;
                transform: translateY(30px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }

        }

        h1 {
            font-size: 4rem;

            background: linear-gradient(
                to right,
                #00d2ff,
                #3a7bd5
            );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;

            margin-bottom: 1rem;
        }

        .subtitle {
            font-size: 1.4rem;
            color: #b0b0d0;
            margin-bottom: 2rem;
        }

        .status {
            display: inline-block;

            background: rgba(0, 210, 255, 0.1);

            border: 1px solid rgba(0, 211, 255, 0.3);

            padding: 0.6rem 1.4rem;

            border-radius: 999px;

            font-size: 1rem;

            color: #00d2ff;
        }

        .status-dot {
            display: inline-block;

            width: 8px;
            height: 8px;

            background: #00ff88;

            border-radius: 50%;

            margin-right: 6px;

            animation: pulse 2s infinite;
        }

        @keyframes pulse {

            0%, 100% {
                opacity: 1;
                box-shadow:
                    0 0 0 0 rgba(0,255,136,0.4);
            }

            50% {
                opacity: 0.7;
                box-shadow:
                    0 0 0 8px rgba(0,255,136,0);
            }

        }

        .links {
            margin-top: 2.5rem;

            display: flex;

            gap: 1rem;

            justify-content: center;

            flex-wrap: wrap;
        }

        .links a {

            color: white;

            text-decoration: none;

            padding: 0.7rem 1.5rem;

            border: 1px solid rgba(255,255,255,0.15);

            border-radius: 8px;

            transition: all 0.3s ease;

            background: rgba(255,255,255,0.04);
        }

        .links a:hover {

            background: rgba(0, 210, 255, 0.12);

            border-color: #00d2ff;

            color: #00d2ff;
        }

        .info {

            margin-top: 3rem;

            font-size: 0.85rem;

            color: #666;
        }

    </style>

</head>

<body>

    <div class="container">

        <h1>Hello Techne</h1>

        <p class="subtitle">
            Powered by FastAPI & AI
        </p>

        <div class="status">

            <span class="status-dot"></span>

            Server is running

        </div>

        <div class="links">

            <a href="/api/info">
                🔍 API Info
            </a>

            <a href="/api/time">
                ⏰ Current Time
            </a>

            <a href="/api/health">
                ❤️ Health Check
            </a>

            <a href="/docs">
                📄 Swagger Docs
            </a>

        </div>

        <p class="info">
            Built by TECHNE AI Agent — FastAPI
        </p>

    </div>

</body>

</html>
"""


@app.get("/api/info")
async def api_info():

    return {
        "name": "Hello Techne",
        "description": "A beautiful FastAPI website built by TECHNE 🤖",
        "version": "1.0.0",

        "tech_stack": [
            "Python",
            "FastAPI",
            "Ollama",
            "AI"
        ],

        "agent": "TECHNE",

        "endpoints": [
            {
                "path": "/",
                "method": "GET",
                "description": "Home page"
            },
            {
                "path": "/api/info",
                "method": "GET",
                "description": "API information"
            },
            {
                "path": "/api/time",
                "method": "GET",
                "description": "Current server time"
            },
            {
                "path": "/api/health",
                "method": "GET",
                "description": "Health check"
            },
            {
                "path": "/docs",
                "method": "GET",
                "description": "Interactive API documentation"
            }
        ]
    }


@app.get("/api/time")
async def current_time():

    now = datetime.now()

    return {
        "time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": "Local server time",
        "timestamp": int(now.timestamp()),
        "day_of_week": now.strftime("%A")
    }


@app.get("/api/health")
async def health_check():

    return {
        "status": "healthy",
        "uptime": "running",
        "service": "hello_techne",
        "agent": "TECHNE",
        "message": "All systems operational"
    }