from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.applications.xception import Xception
from keras.models import load_model
from pickle import load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

def extract_features(filename, model):
        try:
            image = Image.open(filename)
            
        except:
            print("ERROR: Could not open the image! Make sure the image path and extension is correct")
        image = image.resize((299,299))
        image = np.array(image)
        # for images that have 4 channels, we convert them into 3 channels
        if image.shape[2] == 4: 
            image = image[..., :3]
        image = np.expand_dims(image, axis=0)
        image = image/127.5
        image = image - 1.0
        feature = model.predict(image)
        return feature

def word_for_id(integer, tokenizer):
 for word, index in tokenizer.word_index.items():
     if index == integer:
         return word
 return None


def generate_desc(model, tokenizer, photo, max_length):
    in_text = 'start'
    for i in range(max_length):
        sqr = tokenizer.texts_to_sequences([in_text])[0]
        sqr = pad_sequences([sqr], maxlen=max_length)
        pred = model.predict([photo,sqr], verbose=0)
        pred = np.argmax(pred)
        word = word_for_id(pred, tokenizer)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'end':
            break
    return in_text


#path = 'Flicker8k_Dataset/img1.jpg'
max_length = 32
tkzr = load(open("tokenizer.p","rb"))
mod = load_model('models/model_9.h5')
xception_model = Xception(include_top=False, pooling="avg")

pic = extract_features(img_path, xception_model)
img = Image.open(img_path)

desc = generate_desc(mod, tkzr, pic, max_length)
print("\n\n")
print(desc)
plt.imshow(img)


