"""
flask app
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def reload():
    """
    function to load index page
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotiondetector():

    """
    main function detect emotion from text
    """
    text= request.args.get("textToAnalyze")

    response = emotion_detector(text)

    return response




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
