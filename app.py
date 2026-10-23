"""Flask web application for the blockchain consensus comparison project."""
from pathlib import Path
import sys
from flask import Flask, render_template, jsonify
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from consensus_analysis import comparison_dataframe, attack_dataframe, run_analysis

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html",
        data=comparison_dataframe().to_dict(orient="records"),
        attacks=attack_dataframe().to_dict(orient="records"))

@app.route("/api/consensus")
def api_consensus():
    return jsonify(comparison_dataframe().to_dict(orient="records"))

@app.route("/api/security")
def api_security():
    return jsonify(attack_dataframe().to_dict(orient="records"))

@app.route("/generate-reports", methods=["POST"])
def generate_reports():
    result = run_analysis()
    paths = [result["comparison_csv"], result["attacks_csv"], *result["charts"]]
    return jsonify({"message": "Reports generated successfully.",
                    "files": [str(p.relative_to(ROOT)) for p in paths]})

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
