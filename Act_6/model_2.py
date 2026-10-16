import tensorflow as tf
import keras
from keras import layers

class build:
    @staticmethod

    def build_model():

        inputs = keras.Input(shape=(28,28,1), name="digits")
        x = layers.Flatten()(inputs)
        x = layers.Dense(64,activation="relu",name="dense_1")(x)
        x = layers.Dense(64,activation="relu",name="dense_2")(x)
        outputs = layers.Dense(10,activation="softmax",name="predictions")(x)
        model = keras.Model(inputs=inputs,outputs=outputs)


        model.compile(
            optimizer=keras.optimizers.RMSprop(),
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"]
        )

        return model