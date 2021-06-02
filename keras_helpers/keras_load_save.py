import tensorflow as tf

# ================ Loading Keras Models ==================

def load_model(json_file, weights):
    with open(json_file, 'r') as json_file:
        json_savedModel = json_file.read()  #load the model architecture
    model = tf.keras.models.model_from_json(json_savedModel)
    model.load_weights(weights)
    return model


# ================ Saving Keras Models ==================

def save_model_json(model, filename="model.json"):
    model_json = model.to_json()
    with open(filename, "w") as json_file:
        json_file.write(model_json)

def save_model_h5(model, filename="model.h5"):
    model.save_weights(filename)

# Save both .h5 and .json
def save_model(model, filename="model"):
    filename = filename.replace(".json", "").replace(".h5", "")
    save_model_json(model, filename + ".json")
    save_model_h5(model, filename + ".h5")
