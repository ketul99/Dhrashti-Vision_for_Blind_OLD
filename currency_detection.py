import config
from keras.models import load_model
import pandas as pd
from tensorflow.keras.preprocessing import image
from keras.applications.inception_resnet_v2 import preprocess_input

model=load_model("{}\\currency_detection.hdf5".format(config.model_path))

def currency_detection():

    class_dictionary = {'10': 0,
     '100': 1,
     '20': 2,
     '200': 3,
     '2000': 4,
     '50': 5,
     '500': 6,
     'Background': 7}
     
    data_list = ['10', '100', '20', '200', '2000', '50', '500', 'Background']

    IMAGE_SIZE = (299, 299)

    test_image = image.load_img(config.image_path+"captured_image.jpg",target_size=IMAGE_SIZE)
    test_image = image.img_to_array(test_image)

    test_image = test_image.reshape((1, test_image.shape[0], test_image.shape[1], test_image.shape[2]))
    test_image = preprocess_input(test_image)

    prediction = model.predict(test_image)

    df = pd.DataFrame({'pred':prediction[0]})
    df = df.sort_values(by='pred', ascending=False, na_position='first')

    for x in data_list:
        if class_dictionary[x] == (df[df == df.iloc[0]].index[0]):
            break
    
    if(x!='Background'):
        output="It is a {} rupee note.".format(x)
    else:
        output="Unable to detect currency, Please try again."
    return output