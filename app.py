from flask import Flask, jsonify, redirect

app = Flask(__name__)

# Experiment procedures are transcribed from the uploaded
# "ML Practicals in WEKA" document.
EXPERIMENTS = {
    1: {
        "title": "Implement Linear Regression using WEKA",
        "steps": [
            "Open WEKA Explorer and go to the Preprocess tab.",
            "Click Open file and select the CSV or ARFF dataset.",
            "Go to the Classify tab.",
            "Click Choose > Functions > LinearRegression.",
            "Select Cross-validation and set the number of folds to 10.",
            "Click Start to run the experiment."
        ]
    },
    2: {
        "title": "Implement Logistic Regression using WEKA",
        "steps": [
            "Open WEKA Explorer and go to the Preprocess tab.",
            "Click Open file and select the CSV or ARFF dataset.",
            "Go to the Classify tab.",
            "Click Choose > Functions > Logistic.",
            "Select Cross-validation and set the number of folds to 10.",
            "Click Start to run the experiment."
        ]
    },
    3: {
        "title": "Implement the CART Algorithm in WEKA",
        "steps": [
            "If SimpleCART is not installed, open the main WEKA menu.",
            "Go to Tools > Package Manager, search for SimpleCART, and install it.",
            "Close and restart WEKA so the newly installed package is loaded.",
            "In WEKA Explorer, open the Preprocess tab and load the CSV or ARFF dataset.",
            "Go to the Classify tab.",
            "Click Choose > Trees > SimpleCART.",
            "Select Cross-validation with 10 folds.",
            "Click Start."
        ]
    },
    4: {
        "title": "Implement Random Forest Algorithm in WEKA",
        "steps": [
            "Open WEKA Explorer and go to the Preprocess tab.",
            "Click Open file and select the CSV or ARFF dataset.",
            "Go to the Classify tab.",
            "Click Choose > trees > RandomForest.",
            "Select Cross-validation and set the number of folds to 10.",
            "Click Start."
        ]
    },
    5: {
        "title": "Implement XGBoost Algorithm in WEKA",
        "steps": [
            "Install the WekaPython package: Main WEKA Menu > Tools > Package Manager; search for wekaPython and install it.",
            "Install XGBoost in Python from Command Prompt using: pip install xgboost",
            "Verify the installation using: python -c \"import xgboost; print(xgboost.__version__)\"",
            "Install scikit-learn using: pip install scikit-learn",
            "Close and restart WEKA after installing the WEKA package.",
            "In WEKA Explorer, open the Preprocess tab and load the CSV or ARFF dataset.",
            "For the XGBClassifier workflow, the class attribute must be nominal. If it is numeric, select the class attribute and apply Filter > Choose > Unsupervised > Attribute > NumericToNominal; set attribute selection to the class attribute (the document's example uses attribute 10), then click Apply.",
            "Go to Classify > Choose > sklearn > ScikitLearnClassifier.",
            "Open the ScikitLearnClassifier options and set the Scikit-learn learner to XGBClassifier.",
            "Select Cross-validation with 10 folds and click Start."
        ],
        "notes": [
            "The document states that WEKA has no official XGBoost package and uses WekaPython to integrate with Python.",
            "The NumericToNominal attribute number depends on the dataset; do not blindly use 10 if the class attribute is in a different column."
        ]
    },
    6: {
        "title": "Implement AdaBoost Algorithm in WEKA",
        "steps": [
            "Open WEKA Explorer and go to the Preprocess tab.",
            "Click Open file and select the CSV or ARFF dataset.",
            "Go to the Classify tab.",
            "Click Choose > meta > AdaBoostM1.",
            "Select Cross-validation and set the number of folds to 10.",
            "Click Start."
        ]
    },
    7: {
        "title": "Implement SVM Algorithm in WEKA",
        "steps": [
            "Open WEKA Explorer and go to the Preprocess tab.",
            "Click Open file and select the CSV or ARFF dataset.",
            "Go to the Classify tab.",
            "Click Choose > functions > SMO.",
            "Select Cross-validation and set the number of folds to 10.",
            "Click Start."
        ]
    },
    8: {
        "title": "Implement Multiclass SVM in WEKA",
        "steps": [
            "Open WEKA Explorer and go to the Preprocess tab.",
            "Click Open file and select the CSV or ARFF dataset.",
            "Go to the Classify tab.",
            "Click Choose > meta > MultiClassClassifier.",
            "Open the MultiClassClassifier options, go to Classifier, select SMO, and confirm with OK.",
            "Select Cross-validation and set the number of folds to 10.",
            "Click Start."
        ]
    },
    9: {
        "title": "Implement Support Vector Regression in WEKA",
        "steps": [
            "Open WEKA Explorer and go to the Preprocess tab.",
            "Click Open file and select the CSV or ARFF dataset.",
            "Go to the Classify tab.",
            "Click Choose > functions > SMOreg.",
            "Select Cross-validation and set the number of folds to 10.",
            "Click Start.",
            "Keep the target/class attribute numeric; do not convert it to nominal."
        ]
    },
    10: {
        "title": "Implement EM Algorithm in WEKA",
        "steps": [
            "Open WEKA Explorer and go to the Preprocess tab.",
            "Click Open file and select the CSV or ARFF dataset.",
            "Go to the Cluster tab and click Choose > EM.",
            "Open the EM options and set maxIterations = 100.",
            "Set numClusters = 2.",
            "Set numExecutionSlots = 1.",
            "Set numFolds = 10 and Seed = 100.",
            "Choose Use training set and click Start."
        ]
    },
    11: {
        "title": "Implement DBSCAN in WEKA",
        "steps": [
            "Install the DBSCAN package: Main WEKA Menu > Tools > Package Manager; search for optics_dbScan and install it.",
            "Close and restart WEKA so the package is loaded.",
            "Open WEKA Explorer, go to the Preprocess tab, and load the CSV or ARFF dataset.",
            "Go to the Cluster tab and choose DBSCAN.",
            "Open the DBSCAN options and set Epsilon = 0.9.",
            "Set minPoints = 6.",
            "Choose Use training set and click Start."
        ]
    },
    12: {
        "title": "Implement Principal Component Analysis (PCA) in WEKA",
        "steps": [
            "Open WEKA Explorer and go to the Preprocess tab.",
            "Click Open file and select the CSV or ARFF dataset.",
            "Go to Select attributes.",
            "Set Attribute Evaluator to PrincipalComponents.",
            "Set Search Method to Ranker.",
            "Open PrincipalComponents options and set Variance Covered = 0.95.",
            "Choose Use full training set and click Start.",
            "To generate PC1, PC2, and subsequent component attributes, return to Preprocess.",
            "Choose Filter > Unsupervised > Attribute > PrincipalComponents, then click Apply."
        ]
    },
    13: {
        "title": "Implement Linear Discriminant Analysis (LDA) in WEKA",
        "steps": [
            "Install the discriminantAnalysis package: Main WEKA Menu > Tools > Package Manager; search for discriminantAnalysis and install it.",
            "Close and restart WEKA so the package is loaded.",
            "Open WEKA Explorer and go to the Preprocess tab.",
            "Click Open file and select the CSV or ARFF dataset.",
            "Go to the Classify tab.",
            "Click Choose > functions > LDA.",
            "Select Cross-validation and set the number of folds to 10.",
            "Click Start."
        ]
    }
}


@app.get("/")
def home():
    return redirect("/Index")


@app.get("/Index")
def index():
    """List all experiment endpoints and their titles."""
    routes = [
        {
            "route": f"/Exp{number}",
            "experiment": number,
            "title": experiment["title"]
        }
        for number, experiment in EXPERIMENTS.items()
    ]
    return jsonify({
        "message": "Available WEKA ML practical experiments",
        "total_experiments": len(routes),
        "experiments": routes
    })


@app.get("/Exp<int:experiment_id>")
def get_experiment(experiment_id):
    """Return the procedure for one experiment."""
    experiment = EXPERIMENTS.get(experiment_id)

    if experiment is None:
        return jsonify({
            "error": "Experiment not found",
            "available_range": f"/Exp1 to /Exp{len(EXPERIMENTS)}",
            "index": "/Index"
        }), 404

    return jsonify({
        "route": f"/Exp{experiment_id}",
        "experiment": experiment_id,
        "title": experiment["title"],
        "total_steps": len(experiment["steps"]),
        "steps": [
            {"step": number, "instruction": instruction}
            for number, instruction in enumerate(experiment["steps"], start=1)
        ],
        **({"notes": experiment["notes"]} if "notes" in experiment else {})
    })


if __name__ == "__main__":
    # Run with: python app.py
    # API base URL: http://127.0.0.1:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
