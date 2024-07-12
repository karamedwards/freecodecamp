import numpy as np

def calculate(list):

    if len(list)==9:
        #convert list to 3x3 numpy array
        arr = np.array(list).reshape(3,3)
        
        #perform calculations and create dictionary
        calculations = {
            'mean': [np.mean(arr,axis=0).tolist(), np.mean(arr,axis=1).tolist(), np.mean(arr)],
            'variance': [np.var(arr,axis=0).tolist(), np.var(arr,axis=1).tolist(), np.var(arr)],
            'standard deviation': [np.std(arr,axis=0).tolist(), np.std(arr,axis=1).tolist(), np.std(arr)],
            'max': [np.max(arr,axis=0).tolist(), np.max(arr,axis=1).tolist(), np.max(arr)],
            'min': [np.min(arr,axis=0).tolist(), np.min(arr,axis=1).tolist(), np.min(arr)],
            'sum': [np.sum(arr,axis=0).tolist(), np.sum(arr,axis=1).tolist(), np.sum(arr)]
        }
        
        return calculations
    else:
        raise ValueError('List must contain nine numbers.')