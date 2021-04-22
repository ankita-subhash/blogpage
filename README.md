install required packages from requirements.txt file

>> pip install -r requirements.txt
----------------------------------------------------------

Apply migrations to create tables in database

>> python manage.py makemigrations

then 
>> python manage.py migrate

----------------------------------------------------------

Create a super User ( admin user)

>> python manage.py createsuperuser

Login to admin panel using credentials

URL : http://127.0.0.1:8000/admin-panel/login/
Blog list home: http://127.0.0.1:8000
perticular blog page: http://127.0.0.1:8000/your-blog-slug
----------------------------------------------------------

After logging in to dashboard you can CREATE NEW USER ONLY if you  are authicated super user.**

and can add blog, delete or edit blog.


______________________________________________________________

**Dashboard Home page** 


![dashboard home](https://user-images.githubusercontent.com/58456645/115694560-9bcc5b00-a37e-11eb-93bd-82cc04b5dafb.PNG)


_____________________________________________________________
-------------------------------------------------------------


**Blog Home page** 


![blog home page](https://user-images.githubusercontent.com/58456645/115696448-5577fb80-a380-11eb-8f37-192bae086373.PNG)


____________________________________________________________
------------------------------------------------------------

**Blog LIST PAGE WITH CURD operations** 


![Blog List page](https://user-images.githubusercontent.com/58456645/115696886-b4d60b80-a380-11eb-8d1e-0ca3387a21fa.PNG)














