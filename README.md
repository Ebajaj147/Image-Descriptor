**Introduction -

If you view an image, your brain can easily tell you what that image is representing, but a computer can't tell the difference.
This is exactly what I'll be implementing in this Python based project where I'll be making use of deep learning techniques 
of Convolutional Neural Networks and a type of Recurrent Neural Network (LSTM).

**What is an Image Descriptor?

Image Descriptor is an application that involves Computer Vision and NLP concepts to recognize the context of an image to describe them in a natural language like English.

**About the Project - Image Descriptor with CNN

The objective of this project is to apply the concepts I've learnt in CNN and LSTM models and build a working model of an
Image Descriptor by utilizing them.
Xception is used for extracting the features required by us.
It is a CNN model with a dual layer architecture.
It is trained on the sample dataset mentioned below.
Once the features are extracted, they are fed into the LTSM Model which in turn generates the image descriptions.

**DataSet Used - 

For the Image Descriptor, I've used the Flickr_8K dataset.
Flickr_8K dataset - https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip
Flickr_8k_text - https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip
The Flickr_8k_text folder contains file Flickr8k.token which is the main file of our dataset that contains 
image name and their respective descriptions separated by newline(“\n”).

**Requirements -

1. numpy
2. tensorflow
3. jupyterlab
4. keras
5. pillow
6. tqdm 

**What is a CNN?

Convolutional Neural Networks are specialized deep neural networks which can process the data that have input shapes like a 
2D matrix. Images are easily represented as a 2D matrix and CNN is very useful in working with images.
CNN is basically used for image classifications and identifying if an image is a bird, a plane or Superman, etc.
It scans images from left to right and top to bottom to pull out important features from the image and combines the 
feature to classify images. It can handle the images that have been translated, rotated, scaled and changes in perspective.

**What is LSTM?

LSTM stands for Long Short Term Memory. It is a type of RNN (recurrent neural network) which is well suited for 
sequence prediction problems. Based on the previous text, we can predict what the next word will be. It has 
proven itself effective from the traditional RNN by overcoming the limitations of RNN which had short term memory. 
LSTM can carry out relevant information throughout the processing of inputs and with a forget gate, it discards 
non-relevant information.

**Project Conclusion (Image Descriptor) - 

The concepts of a CNN RNN model have been successfully depicted.
Note - Model accuracy depends on the dataset in use. Words outside its dataset cannot be utilized/generated for providing descriptions.  
Models needing a greater accuracy require training on datasets of a minimum 150,000 sample size.

**Output [Test Cases] - 

1. Input -
<img width="856" alt="img1" src="https://user-images.githubusercontent.com/46665472/110484823-08fa9880-8111-11eb-96bc-38b7dd62a800.png">

Output - 
<img width="981" alt="output-img1" src="https://user-images.githubusercontent.com/46665472/110484910-1f085900-8111-11eb-874e-466616fee5be.png">

2. Input - 
<img width="863" alt="img2" src="https://user-images.githubusercontent.com/46665472/110484973-2c254800-8111-11eb-9fc6-874f1000a1cf.png">

Output - 
<img width="981" alt="output-img2" src="https://user-images.githubusercontent.com/46665472/110485013-38110a00-8111-11eb-874c-d6067015f0df.png">





