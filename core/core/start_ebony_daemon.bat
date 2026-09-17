@echo off
cd /d C:\HVF_Repos\hvf-media-matrix-private
"C:\Users\mrshu\AppData\Local\Programs\Python\Python311\python.exe" -m streamlit run app.py --server.port 8501 --server.headless true --browser.gatherUsageStats false > C:\HVF_Repos\hvf-media-matrix-private\daemon_telemetry.log 2>&1
