Predicting Tumour Diagnosis and Interpreting Measurement Importance
Motivation

Medical prediction models are often evaluated only by accuracy.
This project explores whether a simple interpretable model can both predict diagnosis and provide biologically meaningful insight into which measurements drive the prediction.

Question

Can medical measurements predict diagnosis, and which measurements are most informative?

Dataset

Breast Cancer Wisconsin dataset (from scikit-learn)
Each row represents one patient and each column represents a tumour measurement.

Method

Logistic regression classifier

80/20 train–test split

Evaluation using sensitivity and confusion matrix

Feature coefficient analysis for interpretability

Results

The model achieved high sensitivity and missed very few malignant cases in the test set.

Interpretation

Tumour size and texture variability were the strongest predictors of malignancy, consistent with biological expectations about irregular tumour growth.

Limitation

The dataset is curated and may not reflect real clinical workflow data.
