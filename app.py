from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    age = int(request.form['age'])
    gender = request.form['gender']
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    activity = request.form['activity']

    bmi = weight / ((height / 100) ** 2)

    if bmi < 18.5:
        status = "Underweight"
        food = "Nuts, eggs, milk, bananas, potatoes, and healthy fats."
        exercise = "Light strength training, yoga, avoid over-exertion."
        risk = "Risk of anemia, weak immunity, fatigue."
    elif 18.5 <= bmi < 24.9:
        status = "Normal (Healthy)"
        food = "Balanced diet with green vegetables, fruits, lean proteins, and whole grains."
        exercise = "Jogging, brisk walking, swimming, 30 min daily."
        risk = "Low risk. Maintain healthy habits."
    elif 25 <= bmi < 29.9:
        status = "Overweight"
        food = "More fiber-rich foods like oats, legumes, avoid sugary and fried items."
        exercise = "Cardio like running, cycling, HIIT workouts."
        risk = "Higher risk of diabetes, high blood pressure, joint issues."
    else:
        status = "Obese"
        food = "Low-calorie foods: salads, whole grains, steamed vegetables."
        exercise = "Consult doctor. Begin with walking, then low-impact cardio."
        risk = "Risk of heart disease, type 2 diabetes, sleep apnea."

    return render_template('result.html', bmi=round(bmi, 2), status=status,
                           food=food, exercise=exercise, risk=risk)

if __name__ == '__main__':
    app.run(debug=True)
