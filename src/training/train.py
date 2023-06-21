def split(df):
    from sklearn.model_selection import train_test_split
    x = df.iloc[:, :-1]
    last_column_name = df.columns[-1]
    y = df[last_column_name]
    X_train, X_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.3,
                                                    stratify=y,
                                                    random_state=32)

    return X_train, X_test, y_train, y_test
    print('X_train: {X_train.shape[0]}')
    print('X_test: {X_test.shape[0]}')
    print('y_train: {y_train.shape[0]}')
    print('y_test: {y_test.shape[0]}')
