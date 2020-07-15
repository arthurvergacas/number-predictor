import tensorflow as tf
from tensorflow import keras
import numpy as np

from data import DataHandler


class Brain:
    """
    Handles tensorflow library
    """

    def __init__(self):
        # initilize tensorflow model
        self.model = keras.Sequential([
            keras.layers.Dense(128, activation='relu', input_shape=(784,)),
            keras.layers.Dense(10, activation='softmax')
        ])
        self.model.compile(optimizer='adam', loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def train(self):
        """
        Trains the model
        """
        # Gather the training data
        training = DataHandler.loadData("./dataset/mnist_train.csv")
        self.model.fit(training["imgs"],
                       training["labels"], epochs=10)

    def test(self):
        """
        Tests the model
        """
        # Gather the testing data
        testing = DataHandler.loadData("./dataset/mnist_test.csv")
        loss, accuracy = self.model.evaluate(
            testing["imgs"], testing["labels"], verbose=2)

        print(f"Accuracy: {round(accuracy * 100, 2)}%")

    def guess(self, input_):
        """
        Makes a prediction of the given input

        Args:
            input (NumPy Array): A ndarray of 784 elements, each one containing normalized
                                of the brightness of each pixel in the screen

        Returns:
            list: A list containing the prediction
        """
        input_ = (np.expand_dims(input_, 0))
        prediction = self.model.predict(input_)
        return prediction

    def save(self, file_path):
        """
        Saves the model's weights in a .ckpt file

        Args:
            file_path (str): The path to the .ckpt file that you want to store the model
        """
        self.model.save_weights(file_path)

    def load(self, file_path):
        """
        Loads a .ckpt file into the model

        Args:
            file_path (str): The path to the .ckpt file that you want to load the data from
        """
        self.model.load_weights(file_path)


if __name__ == "__main__":

    brain = Brain()

    # brain.train()
    # brain.save("./nn_data/data.ckpt")
    brain.load("./nn_data/data.ckpt")
    # brain.test()
    testing = DataHandler.loadData("./dataset/mnist_test.csv")

    guess = brain.guess(testing["imgs"][0])
    index = np.argmax(guess)
    print(index)
    print(testing["labels"][0])
