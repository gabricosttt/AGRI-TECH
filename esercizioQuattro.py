X = df[['umidita', 'temp', 'ore_secco']]
y = df['irrigare']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modello = RandomForestClassifier(n_estimators=50, random_state=42)
modello.fit(X_train, y_train)
y_pred = modello.predict(X_test)

print(f"{accuracy_score(y_test, y_pred)*100:.1f}%")