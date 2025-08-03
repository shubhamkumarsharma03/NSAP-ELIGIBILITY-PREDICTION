from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd

# Load synthetic data
df = pd.read_csv("synthetic_applicant_data.csv")

# Encode categorical features
df_encoded = pd.get_dummies(df.drop(columns=['Scheme']), drop_first=True)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['Scheme'])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df_encoded, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))