# api-arachar-classification
in this repo we make an api that given an image of an arabic letter returns the letter in characters 

Running api: 
 
```python api-start-point.py``` 

running api docker
to create the docker container extract the docker_files.zip and open a cmd in the extracted folder

the folder structure should look like this : 


```
| project
    |_ Dockerfile
    |_ enviroment_droplet.yml
    |_ serve.sh
    |_ api-arcachar-classification
        |_ README.md
        |_ api-start-point.py
        |_ models
            |_model_weights.h5
        |_utility_py
            |_ letter_classification.py
            |_ ...
```
then in the project folder run:

```
docker build -t py/letter_classification:0.0 . 
```

```
docker run -it --name py_letter_classification -d -p 5000:5000 py/letter_classification:0.0
```

then you can head to the specified link and attempt to make requests to it 
to hit the letter classification end point use

http://127.0.0.1:5000/classify-letter

the code expects a base64 image to arrive in the request.form['img'] 
and will respond with a message in the format of 
```
{'letter': char, 'confidence': float}
# example of response 
{
  "letter": "س",
  "Probability": 0.9999841451644897
}
```