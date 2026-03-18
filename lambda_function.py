import json

# Simple rule-based "model"
def predict(features):
    f1, f2, f3, f4 = features
    
    # Simple logic (acts like ML model)
    if f3 < 2:
        return 0
    elif f3 < 5:
        return 1
    else:
        return 2

def lambda_handler(event, context):
    try:
        # Parse input JSON
        body = json.loads(event.get("body", "{}"))
        
        features = [
            float(body["f1"]),
            float(body["f2"]),
            float(body["f3"]),
            float(body["f4"])
        ]
        
        prediction = predict(features)
        
        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": prediction})
        }
    
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }