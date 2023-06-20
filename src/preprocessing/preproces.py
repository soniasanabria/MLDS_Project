
def load_data(file):
    import pandas as pd
    data = pd.read_csv(file, encoding='ISO-8859-1', sep = ',')
    return data

def identify_duplicates(df):
    duplicated_rows = df.duplicated()
    duplicated_df = df[duplicated_rows]
    print(duplicated_df)

def eliminate_duplicates (df):
    df = df.drop_duplicates(keep='last')
    return df

def to_categorical(df, labels, serie):
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    df[labels] = label_encoder.fit_transform(serie)
