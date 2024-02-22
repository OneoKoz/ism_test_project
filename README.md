# ISM test project 

Run this command from directory

```
docker build -t ism-image
```

```
docker run --name ism-container -it -p 7860:7860 ism-image
```

после этого программа будет запущена на локальном хосте на порту 7860
