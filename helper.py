import gzip, pickle 

def get_MNIST():
	with gzip.open('mnist.pkl.gz', 'rb') as f:
		((X_train, y_train), (X_valid, y_valid), _) = pickle.load(f, encoding='latin-1')
		return ((X_train, y_train), (X_valid, y_valid))
