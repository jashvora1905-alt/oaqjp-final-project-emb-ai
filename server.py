"""Flask server for Emotion Detection application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze text and return detected emotions."""

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "<b>Invalid text! Please try again!</b>"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"<b>{response['dominant_emotion']}</b>."
    )


@app.route("/")
def render_index_page():
    """Render the home page."""

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    