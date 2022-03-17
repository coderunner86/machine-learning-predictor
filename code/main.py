from lr_model import preprocessDataAndPredict
#import Flask 
from flask import Flask, render_template, request
#create an instance of Flask
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict/', methods=['POST'])
def predict():
    if request.method == "POST":

        #call preprocessDataAndPredict and pass inputs
        try:
            predictions = preprocessDataAndPredict()
            #pass prediction to template
            return render_template('predict.html', prediction = predictions)
        except ValueError:
            return "Error"
        pass       
    pass

if __name__ == '__main__':
    app.run(debug=True)