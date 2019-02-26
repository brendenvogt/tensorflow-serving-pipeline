# Flask Api Client receiving predictions from Tensorflow Serving Api using GRPC 

## Setup 
### Clone Repo

```
mkdir ~/Documents/Docker
cd ~/Documents/Docker
```

```
git clone https://github.com/brendenvogt/tensorflow-serving-pipeline
cd tensorflow-serving-pipeline
```

```
curl -s https://storage.googleapis.com/download.tensorflow.org/models/official/20181001_resnet/savedmodels/resnet_v2_fp32_savedmodel_NHWC_jpg.tar.gz | tar --strip-components=2 -C . -xvz
```

```
docker pull tensorflow/serving
docker run -p 8501:8501 --name tfs --mount type=bind,source=/Users/brendenvogt/Documents/Docker/tensorflow-serving-pipeline,target=/models/resnet -e MODEL_NAME=resnet -t tensorflow/serving &
```

```
python resnet_filestream_client.py
```

```
curl -F "image=@./test.jpeg" localhost:5000/predict
```
