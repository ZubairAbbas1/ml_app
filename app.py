import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR, SVC
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
import xgboost as xgb

# ============ REGRESSION MODELS ============
def linear_regression(X, Y):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    model = LinearRegression()
    model.fit(x_train_scaled, y_train)
    y_pred = model.predict(x_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    cv_scores = cross_val_score(model, x_train_scaled, y_train, cv=5, scoring='r2')
    return model, scaler, mse, r2, cv_scores

def decision_tree(X, Y, max_depth=4):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    model = DecisionTreeRegressor(max_depth=max_depth, random_state=42, min_samples_split=5, min_samples_leaf=2)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    cv_scores = cross_val_score(model, x_train, y_train, cv=5, scoring='r2')
    return model, mse, r2, cv_scores

def random_forest(X, Y):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, max_depth=8, min_samples_split=5, min_samples_leaf=2, random_state=42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    cv_scores = cross_val_score(model, x_train, y_train, cv=5, scoring='r2')
    return model, mse, r2, cv_scores

def xgboost_model(X, Y):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, subsample=0.8, colsample_bytree=0.8, random_state=42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    cv_scores = cross_val_score(model, x_train, y_train, cv=5, scoring='r2')
    return model, mse, r2, cv_scores

def svr(X, Y):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    scaler_x = StandardScaler()
    scaler_y = StandardScaler()
    x_train_scaled = scaler_x.fit_transform(x_train)
    x_test_scaled = scaler_x.transform(x_test)
    y_train_scaled = scaler_y.fit_transform(y_train.reshape(-1, 1)).ravel()
    model = SVR(kernel='rbf', C=1.0)
    model.fit(x_train_scaled, y_train_scaled)
    y_pred_scaled = model.predict(x_test_scaled)
    y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1)).ravel()
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    cv_scores = cross_val_score(model, x_train_scaled, y_train_scaled, cv=5, scoring='r2')
    return model, mse, r2, cv_scores

def knn(X, Y):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    model = KNeighborsRegressor(n_neighbors=5)
    model.fit(x_train_scaled, y_train)
    y_pred = model.predict(x_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    cv_scores = cross_val_score(model, x_train_scaled, y_train, cv=5, scoring='r2')
    return model, mse, r2, cv_scores

# ============ CLASSIFICATION MODELS ============
def logistic_regression(X, Y):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    model = LogisticRegression(max_iter=1000, C=1.0, random_state=0)
    model.fit(x_train_scaled, y_train)
    y_pred = model.predict(x_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    cm = confusion_matrix(y_test, y_pred)
    cv_scores = cross_val_score(model, x_train_scaled, y_train, cv=5, scoring='accuracy')
    return model, scaler, accuracy, precision, cm, cv_scores

def decision_tree_classifiers(X, Y, max_depth=4):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=1, max_depth=max_depth, min_samples_split=5, min_samples_leaf=2)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    cm = confusion_matrix(y_test, y_pred)
    cv_scores = cross_val_score(model, x_train, y_train, cv=5, scoring='accuracy')
    return model, accuracy, precision, cm, cv_scores

def xgboost_classifier(X, Y):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', max_depth=3, subsample=0.8, colsample_bytree=0.8, learning_rate=0.1)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    cm = confusion_matrix(y_test, y_pred)
    cv_scores = cross_val_score(model, x_train, y_train, cv=5, scoring='accuracy')
    return model, accuracy, precision, cm, cv_scores

def SVM_classifier(X, Y):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    model = SVC(kernel='linear', C=1.0)
    model.fit(x_train_scaled, y_train)
    y_pred = model.predict(x_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    cm = confusion_matrix(y_test, y_pred)
    cv_scores = cross_val_score(model, x_train_scaled, y_train, cv=5, scoring='accuracy')
    return model, scaler, accuracy, precision, cm, cv_scores

def naive_bayes(X, Y):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    model = GaussianNB()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    cm = confusion_matrix(y_test, y_pred)
    cv_scores = cross_val_score(model, x_train, y_train, cv=5, scoring='accuracy')
    return model, accuracy, precision, cm, cv_scores

# ============ STREAMLIT APP ============

# Initialize ALL session state variables FIRST
if "model" not in st.session_state:
    st.session_state.model = None
if "scaler" not in st.session_state:
    st.session_state.scaler = None
if "feature_columns" not in st.session_state:
    st.session_state.feature_columns = None
if "label_encoder" not in st.session_state:
    st.session_state.label_encoder = None
if "problem_type" not in st.session_state:
    st.session_state.problem_type = None
if "original_labels" not in st.session_state:
    st.session_state.original_labels = None

st.set_page_config(page_title="ML Beginner", layout="wide")
st.title("Machine Learning Beginner 🚀")
st.text("Upload your CSV file and train a model easily")

uploaded_file = st.file_uploader("Upload your CSV file here", type=["csv"])

if uploaded_file is None:
    st.warning("Please upload a CSV file to continue")
    st.stop()

df = pd.read_csv(uploaded_file, nrows=1000)
st.write("Here is the data you uploaded:")
st.dataframe(df)

# Data Analysis
def data_analyze(df):
    st.write(f"Shape of dataset: {df.shape}")
    st.write("Column names:")
    st.write(df.columns.tolist())
    st.write("Missing values per column:")
    st.write(df.isnull().sum())

    if df.isnull().values.any():
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].fillna(df[col].mode()[0])
            else:
                df[col] = df[col].fillna(df[col].mean())
        st.success("Missing values have been filled.")
    else:
        st.info("No missing values found.")

    duplicate_count = df.duplicated().sum()
    st.write(f"Duplicate rows: {duplicate_count}")

    if duplicate_count > 0:
        if st.checkbox("Show duplicated rows"):
            st.write(df[df.duplicated()])
        df.drop_duplicates(inplace=True)
        st.success("Duplicate rows removed.")
    else:
        st.info("No duplicate rows found.")

    return df

if st.button("Analyze Dataset"):
    df = data_analyze(df)

# Feature Selection
feature_input = st.multiselect("Select Features", df.columns)
target_output = st.selectbox("Select Target Column", df.columns)

if not feature_input:
    st.warning("Please select at least one feature.")
    st.stop()

X = df[feature_input].copy()

# Handle categorical features
cat_cols = X.select_dtypes(include=['object']).columns
if len(cat_cols) > 0:
    X = pd.get_dummies(X, columns=cat_cols, drop_first=True)

st.session_state.feature_columns = X.columns

# Target
Y_raw = df[target_output]

def detect_problem(y):
    if y.dtype == 'object' or y.nunique() <= 10:
        problem = "classification"
    else:
        problem = "regression"
    st.success(f"Detected: {problem.upper()} problem")
    return problem

problem_type = detect_problem(Y_raw)
st.session_state.problem_type = problem_type

if Y_raw.dtype == 'object':
    le = LabelEncoder()
    Y = pd.Series(le.fit_transform(Y_raw))
    st.session_state.label_encoder = le
    st.session_state.original_labels = le.classes_
    st.write("Target label encoded.")
else:
    Y = Y_raw.copy()
    st.session_state.label_encoder = None
    st.session_state.original_labels = None

# Model Selection
if problem_type == 'classification':
    model_choice = st.selectbox("Choose Model", [
        "Logistic Regression", 
        "Decision Tree Classifier",
        "XGBoost Classifier",
        "SVM Classifier", 
        "Naive Bayes"
    ])
else:
    model_choice = st.selectbox("Choose Model", [
        "Linear Regression", 
        "Decision Tree Regression",
        "Random Forest", 
        "XGBoost", 
        "SVR", 
        "KNN"
    ])

# Train Model
if st.button("Train Model"):
    with st.spinner("Training model..."):
        if problem_type == 'regression':
            if model_choice == 'Linear Regression':
                model, scaler, mse, r2, cv_scores = linear_regression(X, Y)
                st.session_state.scaler = scaler
                col1, col2, col3 = st.columns(3)
                col1.metric("MSE", f"{mse:.4f}")
                col2.metric("R² Score", f"{r2:.4f}")
                col3.metric("Avg CV Score", f"{cv_scores.mean():.4f}")
                with st.expander("📊 Cross-Validation Details"):
                    st.write(f"CV Scores: {cv_scores}")
                    st.write(f"Std Dev: {cv_scores.std():.4f}")
                    if cv_scores.std() > 0.1:
                        st.warning("⚠️ High variance in CV scores - possible overfitting")
                    else:
                        st.success("✓ Consistent CV scores - good generalization")

            elif model_choice == "Decision Tree Regression":
                model, mse, r2, cv_scores = decision_tree(X, Y)
                col1, col2, col3 = st.columns(3)
                col1.metric("MSE", f"{mse:.4f}")
                col2.metric("R² Score", f"{r2:.4f}")
                col3.metric("Avg CV Score", f"{cv_scores.mean():.4f}")
                with st.expander("📊 Cross-Validation Details"):
                    st.write(f"CV Scores: {cv_scores}")
                    st.write(f"Std Dev: {cv_scores.std():.4f}")
                    if cv_scores.std() > 0.1:
                        st.warning("⚠️ High variance in CV scores - possible overfitting")
                    else:
                        st.success("✓ Consistent CV scores - good generalization")

            elif model_choice == "Random Forest":
                model, mse, r2, cv_scores = random_forest(X, Y)
                col1, col2, col3 = st.columns(3)
                col1.metric("MSE", f"{mse:.4f}")
                col2.metric("R² Score", f"{r2:.4f}")
                col3.metric("Avg CV Score", f"{cv_scores.mean():.4f}")
                with st.expander("📊 Cross-Validation Details"):
                    st.write(f"CV Scores: {cv_scores}")
                    st.write(f"Std Dev: {cv_scores.std():.4f}")
                    if cv_scores.std() > 0.1:
                        st.warning("⚠️ High variance in CV scores - possible overfitting")
                    else:
                        st.success("✓ Consistent CV scores - good generalization")

            elif model_choice == "XGBoost":
                model, mse, r2, cv_scores = xgboost_model(X, Y)
                col1, col2, col3 = st.columns(3)
                col1.metric("MSE", f"{mse:.4f}")
                col2.metric("R² Score", f"{r2:.4f}")
                col3.metric("Avg CV Score", f"{cv_scores.mean():.4f}")
                with st.expander("📊 Cross-Validation Details"):
                    st.write(f"CV Scores: {cv_scores}")
                    st.write(f"Std Dev: {cv_scores.std():.4f}")
                    if cv_scores.std() > 0.1:
                        st.warning("⚠️ High variance in CV scores - possible overfitting")
                    else:
                        st.success("✓ Consistent CV scores - good generalization")

            elif model_choice == "SVR":
                model, mse, r2, cv_scores = svr(X, Y)
                col1, col2, col3 = st.columns(3)
                col1.metric("MSE", f"{mse:.4f}")
                col2.metric("R² Score", f"{r2:.4f}")
                col3.metric("Avg CV Score", f"{cv_scores.mean():.4f}")
                with st.expander("📊 Cross-Validation Details"):
                    st.write(f"CV Scores: {cv_scores}")
                    st.write(f"Std Dev: {cv_scores.std():.4f}")
                    if cv_scores.std() > 0.1:
                        st.warning("⚠️ High variance in CV scores - possible overfitting")
                    else:
                        st.success("✓ Consistent CV scores - good generalization")

            else:
                model, mse, r2, cv_scores = knn(X, Y)
                col1, col2, col3 = st.columns(3)
                col1.metric("MSE", f"{mse:.4f}")
                col2.metric("R² Score", f"{r2:.4f}")
                col3.metric("Avg CV Score", f"{cv_scores.mean():.4f}")
                with st.expander("📊 Cross-Validation Details"):
                    st.write(f"CV Scores: {cv_scores}")
                    st.write(f"Std Dev: {cv_scores.std():.4f}")
                    if cv_scores.std() > 0.1:
                        st.warning("⚠️ High variance in CV scores - possible overfitting")
                    else:
                        st.success("✓ Consistent CV scores - good generalization")

        else:
            if model_choice == "Logistic Regression":
                model, scaler, acc, pre, conf, cv_scores = logistic_regression(X, Y)
                st.session_state.scaler = scaler
                col1, col2, col3 = st.columns(3)
                col1.metric("Accuracy", f"{acc:.4f}")
                col2.metric("Precision", f"{pre:.4f}")
                col3.metric("Avg CV Score", f"{cv_scores.mean():.4f}")
                with st.expander("📊 Cross-Validation Details"):
                    st.write(f"CV Scores: {cv_scores}")
                    st.write(f"Std Dev: {cv_scores.std():.4f}")
                    if cv_scores.std() > 0.1:
                        st.warning("⚠️ High variance in CV scores - possible overfitting")
                    else:
                        st.success("✓ Consistent CV scores - good generalization")

            elif model_choice == "Decision Tree Classifier":
                model, acc, pre, conf, cv_scores = decision_tree_classifiers(X, Y)
                col1, col2, col3 = st.columns(3)
                col1.metric("Accuracy", f"{acc:.4f}")
                col2.metric("Precision", f"{pre:.4f}")
                col3.metric("Avg CV Score", f"{cv_scores.mean():.4f}")
                with st.expander("📊 Cross-Validation Details"):
                    st.write(f"CV Scores: {cv_scores}")
                    st.write(f"Std Dev: {cv_scores.std():.4f}")
                    if cv_scores.std() > 0.1:
                        st.warning("⚠️ High variance in CV scores - possible overfitting")
                    else:
                        st.success("✓ Consistent CV scores - good generalization")

            elif model_choice == "XGBoost Classifier":
                model, acc, pre, conf, cv_scores = xgboost_classifier(X, Y)
                col1, col2, col3 = st.columns(3)
                col1.metric("Accuracy", f"{acc:.4f}")
                col2.metric("Precision", f"{pre:.4f}")
                col3.metric("Avg CV Score", f"{cv_scores.mean():.4f}")
                with st.expander("📊 Cross-Validation Details"):
                    st.write(f"CV Scores: {cv_scores}")
                    st.write(f"Std Dev: {cv_scores.std():.4f}")
                    if cv_scores.std() > 0.1:
                        st.warning("⚠️ High variance in CV scores - possible overfitting")
                    else:
                        st.success("✓ Consistent CV scores - good generalization")

            elif model_choice == "SVM Classifier":
                model, scaler, acc, pre, conf, cv_scores = SVM_classifier(X, Y)
                st.session_state.scaler = scaler
                col1, col2, col3 = st.columns(3)
                col1.metric("Accuracy", f"{acc:.4f}")
                col2.metric("Precision", f"{pre:.4f}")
                col3.metric("Avg CV Score", f"{cv_scores.mean():.4f}")
                with st.expander("📊 Cross-Validation Details"):
                    st.write(f"CV Scores: {cv_scores}")
                    st.write(f"Std Dev: {cv_scores.std():.4f}")
                    if cv_scores.std() > 0.1:
                        st.warning("⚠️ High variance in CV scores - possible overfitting")
                    else:
                        st.success("✓ Consistent CV scores - good generalization")

            else:
                model, acc, pre, conf, cv_scores = naive_bayes(X, Y)
                col1, col2, col3 = st.columns(3)
                col1.metric("Accuracy", f"{acc:.4f}")
                col2.metric("Precision", f"{pre:.4f}")
                col3.metric("Avg CV Score", f"{cv_scores.mean():.4f}")
                with st.expander("📊 Cross-Validation Details"):
                    st.write(f"CV Scores: {cv_scores}")
                    st.write(f"Std Dev: {cv_scores.std():.4f}")
                    if cv_scores.std() > 0.1:
                        st.warning("⚠️ High variance in CV scores - possible overfitting")
                    else:
                        st.success("✓ Consistent CV scores - good generalization")

            st.write("Confusion Matrix:")
            st.dataframe(pd.DataFrame(conf))

    st.session_state.model = model
    st.success("Model trained successfully!")

# Prediction Section
st.subheader("Make Prediction")

if st.session_state.feature_columns is not None:
    input_data = []
    for col in st.session_state.feature_columns:
        val = st.number_input(f"Enter {col}", key=col)
        input_data.append(val)

    if st.button("Predict"):
        if st.session_state.model is None:
            st.error("Please train the model first!")
        else:
            input_array = np.array([input_data])
            if st.session_state.scaler is not None:
                input_array = st.session_state.scaler.transform(input_array)
            prediction = st.session_state.model.predict(input_array)
            
            # Decode prediction if label encoder exists
            if st.session_state.label_encoder is not None and st.session_state.problem_type == "classification":
                try:
                    prediction_label = st.session_state.label_encoder.inverse_transform(prediction)[0]
                except:
                    prediction_label = prediction[0]
            else:
                prediction_label = prediction[0]
            
            st.success(f"🎯 Prediction: {prediction_label}")
            
            # Show more details
            with st.expander("📊 Prediction Details"):
                st.write(f"Raw prediction value: {prediction[0]}")
                st.write(f"Problem type: {st.session_state.problem_type}")
                if st.session_state.label_encoder is not None:
                    st.write(f"Possible values: {list(st.session_state.original_labels)}")
else:
    st.info("Please select features and train a model first.")