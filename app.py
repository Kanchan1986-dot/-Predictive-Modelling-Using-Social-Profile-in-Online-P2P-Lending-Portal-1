from flask import Flask ,render_template,request
from waitress import serve    
import pickle
import numpy as np

model = pickle.load(open("C:/Users/kanch/ML Deployment/model.pkl",'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_loanstatus():
    BorrowerAPR = float(request.form.get('BorrowerAPR'))
    CreditScoreRangeLower= float(request.form.get('CreditScoreRangeLower'))
    CreditScoreRangeUpper = float(request.form.get('CreditScoreRangeUpper	'))
    LP_CustomerPrincipalPayments = float(request.form.get('LP_CustomerPrincipalPayments'))
    EstimatedReturn= float(request.form.get('EstimatedReturn'))
    LenderYield	= float(request.form.get('LenderYield'))
    LP_CustomerPayments = float(request.form.get('LP_CustomerPayments'))
    EstimatedLoss = float(request.form.get('EstimatedLoss'))
    BorrowerRate = float(request.form.get('BorrowerRate'))
    
    

    # prediction
    result = model.predict(np.array([ BorrowerAPR , CreditScoreRangeLower, CreditScoreRangeUpper,LP_CustomerPrincipalPayments,EstimatedReturn,LenderYield,LP_CustomerPayments,EstimatedLoss,BorrowerRate]).reshape(1,3))

    if result[0] == 1:
        result = 'Non defaulter'
    else:
        result = 'defaulter'

    return render_template('index.html',result=result)


if __name__ == '__main__':
    serve(app,host='0.0.0.0',port=8080)