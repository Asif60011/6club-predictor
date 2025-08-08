# predictor.py

import csv

def load_history(file_path="backup.csv"):
    history = []
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # skip empty
                period, result = row
                history.append((period.strip(), result.strip().lower()))
    return history

def predict_next(history):
    if len(history) < 5:
        return "Not enough data for prediction."

    recent = [res for _, res in history[-5:]]
    count = {"red": 0, "green": 0, "violet": 0}
    for r in recent:
        count[r] += 1

    prediction = max(count, key=count.get)
    confidence = round((count[prediction] / 5) * 100, 2)

    if prediction in ("red", "green"):
        big_small = "Big" if prediction == "red" else "Small"
    else:
        big_small = "Neutral"

    return f"🎯 Prediction: {prediction.upper()} | 📊 Confidence: {confidence}% | 🎲 Bet: {big_small}"

if __name__ == "__main__":
    period = input("🕑 Enter last period number: ")
    history = load_history()
    print(predict_next(history))
