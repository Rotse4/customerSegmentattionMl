import joblib
import os
# Create your views here.
def load_model():
    # Load the saved model
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(root_dir, 'kmeans_model.pk1')
    model = joblib.load(model_path)
    return model