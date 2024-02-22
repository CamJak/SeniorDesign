from PacketReader import SessionTracker
from scapy.all import sniff, TCP, IP
import pickle
import sklearn
import pandas as pd

# unpickle model.pkl
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

#define a callback function for the session tracker
def predict(features):
    for key, value in features.items():
                print(f"{key}: {value}")

    print("---------------------------------\n")

    #predict the class of the connection
    features.pop("num_packets")
    #prediction = model.predict([list(features.values())])
    prediction = model.predict(pd.DataFrame([features]))

    if prediction == 1:
        prediction = "Malicious"
    elif prediction == 0:
        prediction = "Benign"
    else:
        prediction = "Unknown"

    print(f"Prediction: {prediction}")
    print("\n\n")

#instantiating the session tracker
tracker = SessionTracker(predict)

#start sniffing packets
sniff(iface="enp0s3", prn=lambda x: tracker.add_packet(x) if TCP in x else None)
