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

1. Logistic regression classifier

2. 80/20 train–test split

3. Evaluation using sensitivity and confusion matrix

4. Feature coefficient analysis for interpretability

Results

The model achieved high sensitivity and missed very few malignant cases in the test set.
1. Accuracy: 0.956

2. Confusion matrix: [[39, 4], [1, 70]]

3. Missed malignant cases: 1

4. Top positive predictors: texture error, mean radius, mean texture

Interpretation

Tumour size and texture variability were the strongest predictors of malignancy, consistent with biological expectations about irregular tumour growth.

Limitation

The dataset is curated and may not reflect real clinical workflow data.
