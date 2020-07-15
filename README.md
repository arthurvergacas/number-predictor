# Number Predictor with MNIST Dataset

## Made with <a href="www.tensorflow.org">Tensorflow</a> and <a href="www.pygame.org">Pygame</a>

# About

This project was made with the <a href="https://pjreddie.com/projects/mnist-in-csv/">MNIST dataset of handwritten digits</a>, while the user interface was made using Pygame. <br><br>
The neural network architecture was provided by Tensorflow library, and in this case I used one hidden layer with 128 neurons and the Rectified Linear Unit as the activation function, while the ouptut layer was activated with Softmax function. <br><br>
The compiler was a standard one (adam optmization and categorical crossentropy as loss function). <br><br>
The data was gathered from <a href="https://pjreddie.com/projects/mnist-in-csv/">this site</a>, which contains the MNIST dataset in .csv files, so I could easily work with pandas library and preprocess the data.
<br><br>
Despite the accuracy of the model being in average 90%, with a loss cost of something near 0.07, the prediction doesn't always work perfectly, whose cause I suppose has something to do with Pygame conversion of the surface to an array. I first tried to simply draw onto the canvas and then convert the surface to an array, but to do so I had to scale the surface down, to match the 28 x 28 format from the dataset. I'm not sure of the way that Pygame does it, but it has a ridiculous downgrade in resolution, and if even I couldn't recognize the numbers after the scale-down, imagine the Neural Network. <br><br>
To handle the problem, I made myself a <em>pixel-ish</em> class, that is painted white when clicked, and then scaled it to the size of the screen that I had - however it has a downside, which is an awful resolution. For my surprise, this approach not only made the predictions more precise, but also improved the performance. My guess is that it has something to do with the manner that Pygame does the array conversion, but again, I'm not sure.

# How to use and test

### The program has only three features:

- Draw with the mouse
- Reset the screen
- Make a guess

### The commands are simple:

| Command           | Function                        |
| ----------------- | ------------------------------- |
| Keyboard R        | Erase the content of the screen |
| Keyboard G        | Make a guess                    |
| Left Mouse Button | Draw                            |

### How to see the prediction

The prediction is shown in the console that you are running the program. It is just a simple print(prediction) line of code.
