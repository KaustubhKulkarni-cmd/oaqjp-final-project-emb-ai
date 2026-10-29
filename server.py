"""Flask web server for the Emotion Detector application."""

from flask import Flask, jsonify, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def render_index_page():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze submitted text and return a readable result."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        message = "Invalid input! Please enter text to analyze."
        if request.accept_mimetypes.best == "application/json":
            return jsonify({"error": message}), 400
        return render_template("index.html", error=message), 400

    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        message = "Unable to analyze the text. Please try again."
        if request.accept_mimetypes.best == "application/json":
            return jsonify({"error": message}), 502
        return render_template(
            "index.html",
            error=message,
            submitted_text=text_to_analyze,
        ), 502

    if request.accept_mimetypes.best == "application/json":
        return jsonify(result)

    return render_template(
        "index.html",
        result=result,
        submitted_text=text_to_analyze,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
