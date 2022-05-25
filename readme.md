<h1 style="text-align: center;">
    To-do Flask
</h1>
<p>Simple to-do list for training pure Flask.<p>
<p>It was used Postgresql as database, SQLAlchemy was not used in this app, just direct statements to INSERT, UPDATE, etc.<p>
<h2>Instructions<h2>
    
1. Git clone the repository.

2. install requirements with:
```sh
pip install -r requirements.txt
```

3. You need to set up your postgresql in your desktop. If you have not done it yet, go to https://www.postgresql.org/download/ and look for installation instructions.

4. Create a database in the postgres CLI, then initialize database by executing the init_db script, first, you need to replace the password with your user password on the init_db file if its demanded and the other information as well.
    
```sh
python init_db.py
```
5.After table successfully created, you need to save your password in a .env file or export the variable in the terminal and pass it on the app.py through os.environ.get('USER_PASSWORD')

6. Start flask server:
```sh
flask run
```
<h2>Sample Image<h2>
    
![image](https://user-images.githubusercontent.com/79537042/170330086-d6ddcdbd-d544-4069-8526-6a45f39073b3.png)



