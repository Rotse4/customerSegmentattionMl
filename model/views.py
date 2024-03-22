# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from . model import load_model

@api_view(['POST'])
def predict_from_csv(request):
    if request.method == 'POST' and request.FILES.get('file'):
        try:
            # Load the model
            model = load_model()

            # Read the uploaded CSV file
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file,)

            # Extract features from the DataFrame
            # X = df[['feature1', 'feature2', ...]]  # Replace with actual feature names
            X = df[['BALANCE', 'BALANCE_FREQUENCY', 'PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY', 'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT', 'TENURE']] 
            print(X)

            # Make predictions using the loaded model
            predictions = model.predict(X)

            # Return predictions in the response
            return Response({'predictions': predictions.tolist()}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
