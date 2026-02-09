Correct Model Building Steps (Weather Prediction)

Import required libraries
(NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn)

Import / load the dataset

Explore the data
(shape, columns, data types, statistical summary)

Check missing (null) values
→ fill using mean / median / mode (as suitable)

Convert categorical features into numerical form
(Label Encoding / One-Hot Encoding)

Feature selection
(important features choose karna)

Check class imbalance
→ handle using SMOTE / oversampling / undersampling (agar needed ho)

Split the data into training and testing sets

Apply normalization / standardization
✅ StandardScaler sirf training data par fit hota hai
→ test data par sirf transform hota hai

Model selection
(Linear Regression, Decision Tree, Random Forest, etc.)

Train the model using training data

Evaluate the model
(Accuracy, Precision, Recall, RMSE, etc.)

Save the trained model for future reuse
(Pickle / Joblib)