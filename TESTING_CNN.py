import cv2
import numpy as np
import time
from keras.models import load_model

model = load_model('NN.h5')
classes = ['Detected Disease: Black rot','Detected Pest: Esca', 'Healthy Leaf','Detected Detected: Leaf blight(Isariopsis Leaf Spot)']
precautionary_measure = ['precautionary measures : Mancozeb, and Ziram are all highly effective against black rot. Because these fungicides are strictly protectants, they must be applied before the fungus infects or enters the plant. They protect fruit and foliage by preventing spore germination. They will not arrest lesion development after infection has occurred.',
'precautionary measures : Curative methods are also used to save esca-infected vines or at least prolong their life. One of these methods is grapevine surgery, where the grapevine trunk is cut open using a chainsaw. Another smaller chainsaw is used to clean the trunk by removing dead/infected wood, leaving the trunk open to dry.',
' ',
"precautionary measures : Spraying of the grapevines at 3-4 leaf stage with fungicides like Bordeaux mixture @ 0.8% or Copper Oxychloride @ 0.25% or Carbendazim @ 0.1% are effective against this disease."]

def get(file_path):
        start_time = time.time()
        img = cv2.imread(file_path)
        height, width = img.shape[:2]
        img = cv2.resize(img, (100,100))

        # predict!
        roi_X = np.expand_dims(img, axis=0)
        predictions = model.predict(roi_X)
        accuracy = max(predictions[0]) * 100

        result_index = np.argmax(predictions[0])
        result  = classes[result_index]
        time2execute = round((time.time() - start_time),3)

        return result, accuracy, time2execute, precautionary_measure[result_index]

