from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadForm
from django.views.generic import TemplateView
from .models import Fruits,Uploads,Diseases
from keras.models import load_model
from keras.preprocessing.image import image
import numpy as np
import random
from keras import backend as k

def home(request):
    template_name = 'index.html'
    form=UploadForm()
    return render(request,template_name,{'form':form})

class Model:
    def __init__(self):
        self.FruitModel=load_model('new102_final_model.h5')
        self.D_indices={'c_0': 0, 'Apple_Black_Rot': 1, 'Corn_Northern_Leaf_B': 2, 'Grape_Black_Measles': 3, 'c_13': 4, 'c_14': 5, 'c_15': 6, 'c_16': 7, 'c_17': 8, 'Bell_Pepper_Bacteria': 9, 'c_19': 10, 'Potato_Early_Blight': 11, 'Potato_Late_Blight': 12, 'c_23': 13, 'c_24': 14, 'c_25': 15, 'c_26': 16, 'Strawberry_Leaf_Scorch': 17, 'Tomato_Early_Blight': 18, 'c_3': 19, 'c_31': 20, 'c_35': 21, 'c_5': 22, 'c_6': 23, 'c_7': 24, 'Common_Rust_Of_Corn': 25, 'c_9': 26}
        #self.disease_classes={'Apple_Black_Rot':0,'Common_Rust_Of_Corn':25,'Common_Rust_Of_Corn':26,'Common_Rust_Of_Corn':24,'Common_Rust_Of_Corn':27,'Apple_Black_Rot':5,'Apple_Black_Rot':6,'Apple_Black_Rot':7,'Common_Rust_Of_Corn':8,'Corn_Northern_Leaf_Blight':'c_10','Grape Black Measles':'c_12','Bell_Pepper_Bacterial_Spot':'c_18','Bell_Pepper_Healthy':'c_19','Potato Early Blight':'c_20','Strawberry Leaf Scorch':'c_27','Tomato Early Blight':'c_29','Tomato Mosaic Virus':'c_35',}

    def predict(self,mode,sample_image):
        test_image = image.load_img(sample_image, target_size=(154,154))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = self.FruitModel.predict(test_image)
        result=np.argmax(result)
        #k.clear_session()
        return result

class DeepAgri(TemplateView):
    template_name = 'DeepAgri.html'
    def post(self,request):
        if request.method=='POST':
            form=UploadForm(request.POST,request.FILES)
            if form.is_valid():
                num = random.randint(0, 1000)
                model = Uploads(image=request.FILES['image'], name=str(num))
                model.save()

                fobj=Diseases.objects.all()
                iobj=Uploads.objects.all()
                mode=form.cleaned_data['mode']
                for object in iobj:
                    if object.name==str(num):
                        upload_image=object.image

                str_image = str(upload_image)
                list = str_image.split("/")
                img = list[1]
                main_model = Model()
                for i, j in enumerate(main_model.D_indices):
                    res = main_model.predict(mode,'media\\images\\' + img)
                    if (i == res):
                        prediction = j
                        break
                img_addr='media\\images\\' + img
                li='unknlown image'
                for object in fobj:
                    if object.name == prediction:
                        li=[object.name,object.symptoms,object.desc,object.sol]

                audio='http://127.0.0.1:8000/media/audio/diseases/'+li[0]+'.mp3'
                return render(request, self.template_name,{'image':upload_image,'mode':mode,'name':li[0],'symptoms':li[1],'desc':li[2],'sol':li[3],'audio':audio,})
        else:
            form=UploadForm()
        return render(request,'index.html',{'form':form})