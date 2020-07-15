import pandas
import numpy as np


class DataHandler:
    """
    A module to treat the data in .csv files
    """

    @staticmethod
    def loadData(file_path):
        """
        Treat the data in a given .csv file and separes it into "labels" and "imgs".

        Args:
            file_path (str): the path to the file you want to treat

        Returns:
            dict: a dictionary with parameters "labels" and "imgs", where which one contains a list o lists 
        """
        data = pandas.read_csv(file_path, sep=',')
        data_list = data.to_numpy()
        labels = []
        pixels = []
        for image in data_list:
            temp_l, temp_p = np.split(image, [1])
            labels.append(temp_l.astype(float))
            pixels.append(temp_p.astype(float))

        # rearrange the labels to make it fitable to the neural network
        for i in range(len(labels)):
            temp = np.zeros(10)
            temp[int(labels[i])] = 1
            # it needs to be transposed and a numpy array for performance
            labels[i] = np.array(temp, dtype=np.float64)

        # normalize pixels to a range between 0 and 1 - divide i tby 255
        index = 0
        for img in pixels:
            # for i in range(len(img)):
            #     img[i] = img[i] / 255
            # convert it to numpy array
            pixels[index] = np.array(img, dtype=np.float64) / 255
            index += 1

        enhanced_data = {
            "labels": np.array(labels),
            "imgs": np.array(pixels)
        }

        return enhanced_data


if __name__ == "__main__":
    train = DataHandler.loadData("./dataset/mnist_train.csv")
    print(train["imgs"].shape)
    print(train["labels"].shape)
