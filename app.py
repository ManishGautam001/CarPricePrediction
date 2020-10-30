from flask import Flask, request, render_template
import pickle
app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))




@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')



@app.route('/predict',methods = ['POST'])
def predict():
    if request.method == 'POST':
        myDict = request.form
        Year = int(myDict['Years'])
        Present_Price = int(myDict['Present_Price'])
        Kms_Driven = int(myDict['Kms_Driven'])
        Owner = int(myDict['Owner'])
        Fuel_Type = int(myDict['Fuel_Type'])
        Seller_Type = int(myDict['Seller_Type'])
        Transmission = int(myDict['Transmission'])
        prediction=model.predict([[Present_Price,Kms_Driven,Owner,Year,Fuel_Type,Seller_Type,Transmission]])
        output = round(prediction[0],2)

        return render_template('show.html',prediction_text="You Can Sell The Car at {} lakhs".format(output))


if __name__ == "__main__":
    app.run(debug=True)
        
