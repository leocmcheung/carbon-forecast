from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

def our_tx(X):
    num_col = sorted(X.select_dtypes(include=["int64", "float64"]).columns)
    cat_col = sorted(list(set(X.columns) - set(num_col)))
    breakpoint()
    num_transformer = MinMaxScaler()
    cat_transformer = OneHotEncoder(handle_unknown='ignore')
    tx = ColumnTransformer([
        ('num_tr', num_transformer, num_col),
        ('cat_tr', cat_transformer, cat_col)
    ])#sparse_threshold=0)
    return tx

def tt_split(X,y,transformer):
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,\
         random_state=37)
    X_train_transformed = transformer.fit_transform(X_train)
    X_test_transformed = transformer.transform(X_test)
    return X_train_transformed, X_test_transformed, y_train, y_test



