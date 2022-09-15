from sklearn.decomposition import PCA

def our_pca(X_train, X_test, n_compenents):
    pca = PCA(n_components=n_compenents)
    X_train_proj = pca.fit_transform(X_train)
    X_test_proj = pca.transform(X_test)
    return X_train_proj, X_test_proj, pca
