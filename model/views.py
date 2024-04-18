from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from . model import load_model

@api_view(['POST'])
def predict_from_csv(request):
    if request.method == 'POST':
        try:
            # Load the model
            model = load_model()

            # Extract feature values from the form data
            balance = float(request.POST.get('balance'))
            balance_frequency = float(request.POST.get('balance_frequency'))

            # Create a DataFrame from the extracted feature values
            data = {'BALANCE': [balance], 'BALANCE_FREQUENCY': [balance_frequency]}
            input_df = pd.DataFrame(data)

            # Drop feature names from input DataFrame
            input_df = input_df.values

            print("Input data:", input_df)  # Debugging

            # Make predictions using the loaded model
            predictions = model.predict(input_df)

            print("Predictions:", predictions)  # Debugging

            # Return predictions in the response
            return Response({'prediction': predictions[0]}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': 'Prediction error: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


def home(request):
         
    # list=['BALANCE', 'BALANCE_FREQUENCY', 'PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY', 'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT', 'TENURE']
    # my_dict = {index: value for index, value in enumerate(list)}
    # print(my_dict)
         

       
    model = load_model()
    
    # csv_file = request.FILES['file']
    csv_file = pd.read_csv('companies.csv')
    df = pd.read_csv('companies.csv',)
    
    X = df[['BALANCE', 'BALANCE_FREQUENCY', 'PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY', 'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT', 'TENURE']] 
    
    predictions = model.predict(X)
    df['prediction']=predictions
    data = df.to_dict(orient='records')
   
    return render(request, 'home.html', {"data":data})
    