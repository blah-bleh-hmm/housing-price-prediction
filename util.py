# util.py

def preprocess_input(data):
    """
    Converts incoming JSON dict to model-ready format (list or array).
    Modify according to your model's expected input features.
    """
    # Example: data = {"area": 1000, "bedrooms": 2, "bathrooms": 1}
    return [
        data['area'],
        data['bedrooms'],
        data['bathrooms']
    ]
