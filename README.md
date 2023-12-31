
![Logo](https://freepngimg.com/thumb/newspaper/7-2-newspaper-free-download-png.png)


# Newspaper Agent

This project was created specifically for a newspaper company. It makes it easy to add posts. Editing and deleting won't be a problem either. The site also has topics for quick filtering of news.
### ⚡ Live DEMO: [NewspaperAgency](https://newspapersagency-w41c.onrender.com/)
- You can use following superuser (or create another one by yourself):
    - Login: ```MajorUser```
    - Password: ```MajorAdmin123```


## 👩‍💻 _Installation & Run_
### 🧠 Set up the environment 


 On Windows:
```python
python -m venv venv 
venv\Scripts\activate
 ```

 On macOS:
```python
python3 -m venv venv 
source venv/bin/activate
 ```

### 👯 Set up requirements 
```python
pip install -r requirements.txt
```


### 🤔 Make migrations and migrate

```python
python manage.py migrate
```
### 📫 Install database fixture
```python
python manage.py loaddata data.json
```
_You can see images inside media folder. You can easily delete it. They was added here just to show you how look like completely filled site._
_If you are not going to use my data just delete it. Or they will be removed by themselves thanks to self-cleaning._
### ⚡️ Run server
```python
python manage.py runserver
```
### 😄 Go to site [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## 🍈 _How that works..._
### 🧠 Total control:
-   Create Posts on website or admin-panel. All fields look the same.
- Create Topics and connect it to posts just on website.
- Users can registrate them self. But **staff** role they can take only in admin-panel.
- Only **staff** user can **CRUD** with the ojects.
## 😋 _GL HF!_