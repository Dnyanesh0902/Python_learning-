import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([1,2,2.5,3,3.5,4,5,6]).reshape(-1, 1)

# Marks Scored
y = np.array([40,50,60,70,80,90,95,97])

model =  LinearRegression()
model.fit(x, y)


new_hours = float(input("Enter Study Hours (0-6):"))
if new_hours > 6:
    print("Invalid Input. Max Study Hours Is 6.")
    exit()
    
predicted_marks = model.predict(np.array([[new_hours]]))[0]
predicted_marks = max(0, min(100, predicted_marks))

print(f"Predicted Marks: {predicted_marks:.2f}")
    