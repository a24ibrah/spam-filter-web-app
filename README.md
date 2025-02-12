# Spam Filter Web App  

This project demonstrates how to deploy a spam filter as a web app using Flask or FastAPI.  

## Features  
- Classify emails as spam or ham in real time.  
- Choose between Flask (lightweight) or FastAPI (modern and fast).  

## Setup  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/spam-filter-web-app.git
   cd spam-filter-web-app
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:  
   ```bash
   python app_flask.py
   ```

4. Run the FastAPI app:  
   ```bash
   python app_fastapi.py
   ```

## Usage  

Send a POST request to the `/classify` endpoint with the email text:  

```bash
curl -X POST -H "Content-Type: application/json" -d '{"email_text": "Congratulations! You've won a $1000 Walmart gift card."}' http://127.0.0.1:5000/classify
```

## Deployment  

Deploy the app to Heroku:  

1. Install the Heroku CLI and log in.  
2. Create a `Procfile`:  
   ```bash
   echo "web: python app_flask.py" > Procfile
   ```
3. Commit your changes and deploy:  
   ```bash
   git add .
   git commit -m "Deploying to Heroku"
   heroku create
   git push heroku master
   ```

## License  

This project is licensed under the MIT License.
