# Please note: it is best to run this in a Jupyter Notebook 


import tensorflow as tf
import IPython.display as display
import matplotlib.pyplot as plt

# Background - "Thinking Machines"
vid = display.YouTubeVideo('cNxadbrN_aI')
# Needs to be within a Jupyter notebook cell in order to work as expected
vid


# GPU - Complex matrix mathematics 
tf.config.list_physical_devices('GPU')

# Nueral Networks and Training - Copying human learning techinque = Trial & Error

fashion_mnsit = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (valid_images, valid_labels) = fashion_mnsit.load_data()
print(train_labels[:10])
## train_images and train_labels. train_images are like the question on our flashcards and train_labels are like the answer. 

## Present an image
data_idx = 42
plt.figure()
plt.imshow(train_images[data_idx], cmap='gray')
plt.colorbar()
plt.grid(False)
plt.show()

## Classify the image, what is the given label (i.e. correct image classification) as per the data in data_class.txt? 
print(train_labels[data_idx])


# Building a Neuron - Defining the architecture > Initiate Training > Evaluating the model
# y = mx+b | each image is 28 by 28 pixels = a total of 784 weights 
print(valid_images[data_idx])

number_of_classes = train_labels.max() + 1
print(number_of_classes)

# Verifying the Model - https://www.tensorflow.org/js/guide/models_and_layers#model_summary
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(number_of_classes)
])

model.summary()

image_height = 28
image_width = 28

number_of_weights = image_height * image_width * number_of_classes
## number of weights should equal our parameters (-10 in this case)
print(number_of_weights)

model_plot = tf.keras.utils.plot_model(model, show_shapes=True)


# Initiate Training
## Requirement to provide a function for the model to grade its performance - Sparse, Cateogrical, Cross-entrophy & from_logits
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Evaluate training 
## fit method to help model study & quiz - https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit
history = model.fit(
    train_images,
    train_labels,
    epochs=5,
    verbose=True,
    validation_data=(valid_images, valid_labels)
)
### Accuracy ends up around 80% - remember this model only has 10 neurons 

# Prediction - https://www.tensorflow.org/api_docs/python/tf/keras/Model#predict - Raw results for the first 10 items in data-set (requires formatting for interpretation)
model.predict(train_images[0:10])

## Can format and graph the data - In correspondance with the Label, the larger the value, the more confident the neuron is that it corresponds to the correct label
### The more negative the value = The more confident it is *not* the correct label 

data_idx = 8675 # The question number to study with. Feel free to change up to 59999.

plt.figure()
plt.imshow(train_images[data_idx], cmap='gray')
plt.colorbar()
plt.grid(False)
plt.show()

x_values = range(number_of_classes)
plt.figure()
plt.bar(x_values, model.predict(train_images[data_idx:data_idx+1]).flatten())
plt.xticks(range(10))
plt.show()

print("correct answer:", train_labels[data_idx])
