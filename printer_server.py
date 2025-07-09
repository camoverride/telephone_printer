from flask import Flask, request
from flask_restful import Resource, Api
import yaml
from print_text import print_text


# Load config file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


# Create Flask app and API
app = Flask(__name__)
api = Api(app)

class Printer(Resource):
    def post(self):
        # Extract the prompt.
        text = request.json.get("text", "")

        print_text(text=text,
                   newline=True)

        return {"reply": "SUCCESS"}


# Register endpoint
api.add_resource(Printer, "/print")



if __name__ == "__main__":

    app.run(host="0.0.0.0",
            port=5000,
            debug=True)

"""
curl -X POST http://localhost:5000/print \
  -H "Content-Type: application/json" \
  -d '{"text":"Hello World"}'
"""
