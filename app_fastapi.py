from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel

app = FastAPI()

# Load the trained model
model = joblib.load('spam_filter_model.pkl')

class EmailText(BaseModel):
    email_text: str

@app.post('/classify')
async def classify_email(email: EmailText):
    email_text = email.email_text

    # Predict using the model
    prediction = model.predict([email_text])
    result = 'spam' if prediction[0] == 1 else 'ham'

    return {'result': result}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)