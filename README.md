# ML-Task
**Once you download the repo you should run the following in cmd**

**We should have python installed first!**
```
pip install -r requirements.txt
```

**then run this command in the cmd**

```
flask run
```
the api should be running!

## Testing the endpoint

the endpoint link should be like (depending on the your configuration) this **http://127.0.0.1:5000/predict**

**you should have inputs like this in json format**

**for example**
```python
FEATS = {
    'Age': 80,
    'Balance':1000 ,
    'HasCrCard': 1,
    'IsActiveMember': 0,
    'EstimatedSalary': 1000,
    'Geography_France': 1,
    'Geography_Germany': 0,
    'Geography_Spain': 0,
    'Gender_Female': 1,
    'Gender_Male': 1,
    'Card Type_DIAMOND': 0,
    'Card Type_GOLD': 1,
    'Card Type_PLATINUM': 0,
    'Card Type_SILVER': 0,
}
```
