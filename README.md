Interpreting Malignant Tumour Predictions from Clinical Measurements
Overview

This project investigates whether routine tumour measurements can meaningfully distinguish malignant from benign cases, and more importantly, which measurements drive the prediction. 

Rather than focusing only on model accuracy, the goal is to understand how reliable the prediction is and why the model reaches its conclusion. In clinical contexts, a correct prediction is not sufficient; the reasoning behind it determines whether the result can be trusted.

Research Question

Can measurable tumour characteristics predict malignancy, and which features most influence the decision?
Dataset

The analysis uses the publicly available breast cancer diagnostic dataset included in scikit-learn.

Each sample contains quantitative measurements extracted from digitised images of fine needle aspirate biopsies.

Examples of features:

-mean radius

-mean texture

-mean area

-worst perimeter

-fractal dimension

-symmetry

Target:   0 = benign;   1 = malignant

Total samples: 569

Method
1. Data preparation

Loaded dataset from scikit-learn

Separated predictors and diagnosis target

Split into training and testing subsets (80/20)

2. Modelling

Used logistic regression as an interpretable baseline model.

Reason:
A transparent model allows examination of feature influence rather than acting as a black box.

3. Evaluation

Model performance evaluated using:

Accuracy

Confusion matrix

Precision & recall

Sensitivity to malignant cases

Clinical motivation:
Missing a malignant tumour (false negative) is more critical than falsely flagging a benign one.

4. Feature interpretation

Examined model coefficients to identify which measurements most influenced classification decisions.

Results

Accuracy: 0.956

Confusion Matrix:

Actual Benign:	39 Predicted Benign;      	4 Predicted Malignant

Actual Malignant:	1 Predicted Benign;      	70 Predicted Malignant

Key observation:
The model rarely misses malignant cases (high recall), which is more important clinically than overall accuracy.

Most Influential Features

Top contributing measurements:

-texture error

-mean radius

-mean texture

-worst radius

-compactness error

-mean area

These relate to tumour size and irregularity — known biological indicators of malignancy.

Interpretation

The important outcome of this project is not the high accuracy, but that the model’s reasoning aligns with biological expectations.

Larger, more irregular tumours were consistently associated with malignant classification.

This demonstrates that even simple interpretable models can capture meaningful structure in clinical measurements, but their usefulness depends on understanding the basis of the prediction rather than accepting the output blindly.

Limitations

Dataset is curated and clean compared to real clinical workflow data

Does not include missing values or measurement variability

Predictions are not diagnostic decisions

Model performance in practice would depend on population differences

Output
feature importance plot

Key Takeaway

A predictive model is useful only when its reasoning can be understood.
In medical contexts, interpretability is not optional ; it determines whether a prediction can support a decision.
