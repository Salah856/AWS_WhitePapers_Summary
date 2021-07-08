def main():
    positive_data = pd.read_csv(args.positive_data_file)[args.columns].dropna().reset_index(drop=True)
    negative_data = (
        pd.read_csv(args.negative_data_file)[args.columns].dropna().reset_index(drop=True)
    )
    training_data = positive_data.append(negative_data, ignore_index=True)
    target = training_data[["label"]]
    features = training_data.drop(["label"], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.3, random_state=0
    )
    print("Features: {}".format(args.columns))
    scaler_train = preprocessing.StandardScaler().fit(x_train)
    x_test = scaler_train.transform(x_test)
    x_train = scaler_train.transform(x_train)
    model = LogisticRegression(penalty="l2", class_weight="balanced", C=0.1).fit(x_train, y_train)
    pred_prob = model.predict_proba(x_test)[:, 1]
    predictions = [round(value) for value in pred_prob]
    print(confusion_matrix(y_test, predictions))
    predicted = pred_prob &gt; args.threshold
    print(metrics.classification_report(y_test, predicted, digits=3))
    accuracy = model.score(x_test, y_test)
    print(accuracy)
    model_feat_imp = pd.Series(abs(model.coef_[0]), features.columns).sort_values(ascending=False)
    print(model_feat_imp)
    # save model 
    time = date.today().strftime("%d%m%Y%H%M%S")
    pickle_file = "model_{}.pkl".format(time)
    pickle_full_path = os.path.join(args.save, pickle_file)
    with open(pickle_full_path, "wb") as file:
         pickle.dump(model, file)
         print("Model is saved as {}".format(pickle_full_path))

        
