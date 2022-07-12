from statsmodels.tsa.vector_ar.vecm import *

# make 40 n+1 predictions
def get_predictions(local_data):
    preds = []
    for i in range(40):

        # We create the n-sized window to used for thid prediction
        window = local_data.iloc[i:-(40-i)]
        
        # We create the model and predict one value
        model = VECM(window, deterministic="ci", seasons=0)
        vecm_res = model.fit()

        prediction = vecm_res.predict(steps=1)
        
        preds.append(prediction[0][0]) # first index of the first TS predicted
    
    return preds

