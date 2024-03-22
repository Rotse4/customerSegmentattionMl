import joblib
# Create your views here.
def load_model():
    # Load the saved model
    model = joblib.load('/home/rotse4/Desktop/ml/grace/kmeans_model.pk1')
    return model