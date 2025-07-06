#!/bin/bash

echo "🔄 Starting AutoInfraGuard..."

# Start FastAPI server in the background
echo "🚀 Launching FastAPI inference server..."
uvicorn app.inference_api:app --reload --port 8000 &

# Save the PID
SERVER_PID=$!

# Start prediction loop to log data continuously
echo "🔁 Starting prediction simulator..."
python3 app/send_requests_loop.py &

# Optional: Show latest logs in terminal (optional)
echo "📊 (Optional) View latest predictions from metrics.db"
echo "You can run: python3 app/view_logs.py"

# Reminder for dashboard
echo ""
echo "🌐 To visualize metrics, open Grafana or explore metrics.db."
echo "📁 Data is stored in: monitoring/metrics.db"
echo "🛑 To stop everything, use: kill $SERVER_PID"

# Wait for the FastAPI process to stop
wait $SERVER_PID


# To Make It Executable:
# chmod +x start_auto_infraguard.sh
# Then run it with:
# ./start_auto_infraguard.sh