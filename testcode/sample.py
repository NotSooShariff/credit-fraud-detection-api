import requests
import numpy as np
import json

ngheaders = {'ngrok-skip-browser-warning': 'true'} 

# Define the data as a dictionary with all features
data = {
    "V1": float(-1.3598071336738),
    "V2": float(-0.0727811733098497),
    "V3": float(2.53634673796914),
    "V4": float(1.37815522427443),
    "V5": float(-0.3383207699425183),
    "V6": float(0.462387777762292),
    "V7": float(0.239598554061257),
    "V8": float(0.0986979012610507),
    "V9": float(0.363786969611213),
    "V10": float(0.0907941719789316),
    "V11": float(-0.551599533260813),
    "V12": float(-0.617800855762348),
    "V13": float(-0.991389847235408),
    "V14": float(-0.311169353699879),
    "V15": float(1.46817697209427),
    "V16": float(-0.470400525259478),
    "V17": float(0.207971241929242),
    "V18": float(0.0257905801985591),
    "V19": float(0.403992960255733),
    "V20": float(0.251412098239705),
    "V21": float(-0.018306777944153),
    "V22": float(0.277837575558899),
    "V23": float(-0.110473910188767),
    "V24": float(0.0669280749146731),
    "V25": float(0.128539358273528),
    "V26": float(-0.189114843888824),
    "V27": float(0.133558376740387),
    "V28": float(-0.0210530534538215),
    "Amount": float(149.62),
    "Time": float(0)
}

# Convert the dictionary values to native Python types
data = {key: float(value) if isinstance(value, (np.float32, np.float64)) else value for key, value in data.items()}

# Serialize the data manually
serialized_data = json.dumps(data)

# Make a POST request to the API
response = requests.post('{YourNgrokURL}/predict', data=serialized_data, headers=ngheaders)

# Print the response
print(response.json())
