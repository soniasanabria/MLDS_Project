def split(df):
    from sklearn.model_selection import train_test_split
    x = df.iloc[:, :-2]
    y = df.iloc[:, -1]
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

def train_model (X_train, y_train, C, gamma, X_test):
    from sklearn import svm
    from sklearn.utils import class_weight
    import numpy as np
    class_weights = class_weight.compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
    class_weights_dict = {class_label: weight for class_label, weight in zip(np.unique(y_train), class_weights)}
    wf_rbf_svm = svm.SVC(kernel='rbf', 
                    C=10, 
                    gamma = 10,
                    class_weight=class_weights_dict)  

    wf_rbf_svm.fit(X_train, y_train)
    y_pred = wf_rbf_svm.predict(X_test)
    return y_pred


def list_confusion_matrix(df, y_test, y_pred):
    
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)
    
    classes =df.iloc[:,-1].unique()
    classes_report = [classes[1], classes[0]]

    import pandas as pd
    conf_matrix = pd.DataFrame(data = cm,
                    index = pd.MultiIndex.from_product([['Valor real'], classes_report]),
                    columns = pd.MultiIndex.from_product([['Valor predicho'], classes_report]))
    return conf_matrix
    
def classification_report(y_test, y_pred):
    from sklearn.metrics import classification_report
    class_report = classification_report(y_test, y_pred)
    return class_report


