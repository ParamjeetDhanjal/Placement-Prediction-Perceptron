import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('placement_data.csv')

x1 = data[['CGPA']].values
x2 = data[['IQ']].values
y = data['Placed'].map({'Yes': 1, 'No': 0}).values
bias = 1
w1 = 0.1
w2 = 0.1
epoch = 500
lr = 0.01

#Activation 
def step(z):
    return 1 if z>=0 else 0

def Perceptron():
    for i in range(epoch):
       for i in range(len(y)):
            global w1,w2,bias
            z = w1*x1[i][0] + w2*x2[i][0] + bias
            y_pred = step(z)
            error = y[i] - y_pred
            w1 += lr * error * x1[i][0]
            w2 += lr * error * x2[i][0]
            bias += lr * error
    return w1, w2, bias

trained_w1, trained_w2, trained_bias = Perceptron()
def predict(cgpa, iq):
    z = trained_w1*cgpa + trained_w2*iq + trained_bias
    return step(z)

predicted_cgpa = int(input("Enter CGPA: "))
predicted_iq = int(input("Enter IQ: "))
predicted_y = predict(predicted_cgpa, predicted_iq)

cgpa_placed = data['CGPA'][y == 1]
cgpa_not_placed = data['CGPA'][y == 0]


plt.scatter(cgpa_placed, [1]*len(cgpa_placed), color='green', label='Placed')
plt.scatter(cgpa_not_placed, [0]*len(cgpa_not_placed), color='red', label='Not Placed')
plt.scatter(predicted_cgpa,predicted_y, color='blue', label='predicted')
plt.xlabel('CGPA')
plt.ylabel('Placed (0=No, 1=Yes)')
plt.title('Placement Prediction by CGPA')
plt.legend()
plt.show()
