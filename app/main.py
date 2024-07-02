from application.dial_application import DialApplication
import uvicorn
from aidial_sdk import DIALApp

app = DIALApp()
app.add_chat_completion("app", DialApplication())

# Run builded app
if __name__ == "__main__":
    uvicorn.run(app, port=5002, host="0.0.0.0")
