
```
mkdir ~/Documents/Docker/resnet
curl -s https://storage.googleapis.com/download.tensorflow.org/models/official/20181001_resnet/savedmodels/resnet_v2_fp32_savedmodel_NHWC_jpg.tar.gz | tar --strip-components=2 -C ~/Documents/Docker/resnet -xvz
```

```
ls ~/Documents/Docker/resnet
```

```
docker pull tensorflow/serving
docker run -p 8501:8501 --name tfs --mount type=bind,source=/Users/brendenvogt/Documents/Docker/resnet,target=/models/resnet -e MODEL_NAME=resnet -t tensorflow/serving &
```

```
curl -F "image=@/Users/brendenvogt/Documents/Docker/resnet/test.jpeg" localhost:5000/predict
```