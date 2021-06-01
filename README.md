# Social Media APIs

## Installation Process

Python > 3.0

1. First we need to build docker compose file which can create container of required images (make sure you are in directory where docker-compose file exist).

```bash
docker-compose build
```
2. After build we need to up the container
```bash
docker-compose up
```
3. By doing these two steps all the requirements are installed inside the container and also copy all the code directory inside the container. After this  you are given the link in the terminal which can browse your project but not getting any data because, we need token access key.


4. To get Token access key , we need to create django superuser to manage admin interface also. For this we need to open another terminal and use the below mentioned command,
```bash
docker exec -it container_id python manage.py createsuperuser

```
 You can easily create super user here. The container_id is the id of your running container. Now you can use the url to manage admin interface [0.0.0.0:8000/admin].
And after creating super user you must generate token access or refress key by providing same username and password in body parameters the endpoints to generate access key or refresh key are mentioned below,

```bash
/api/token/
```
or
```bash
/api/token/refresh/
```
  

5. Now we are set, Using POSTMAN we can hit the api with endpoints we can access the required data, the given endpoints are as,

    ```bash
        /user-view-set/
    ```
    
    * This endpoint is used to get all users details, register new user, update user's details and delete any specific user by using GET, POST, PUT, DELETE methods respectively.
    
        * if we are using **GET** method and the endpoint is **/user-view-set/** then we will get all user details.
        * if we are using **POST** method and the endpoint is same then we will register 'New User' so we have to provide username, password and email in body parameters for user registration. While registering the user the geolocation data of the IP and holiday details are storing into the database (User Details database) that the register retquest originated from.
        * also using **PUT** and **DELETE** methods we can update and delete any particular user by providing 'id'.
    
    ```bash
        /login/
    ```
    * This endpoint is used with **POST** method and we have to provide username and password in body parameters for login. After login this will return the token of that user.

    ```bash
        /posts/
    ```
    *  This endpoint is used to get all posts details, create new post, update post details and delete any specific post by using GET, POST, PUT, DELETE methods respectively.

        * if we are using **GET** method and the endpoint is **/posts/** then we will get all post's details like user name, id of post and how many likes post have.
        * if we are using **POST** method and the end point is same as above then it means we are creating post so for this we have to provide user and content in body parameters.
        * similarly we can use **PUT** and **DELETE** method for update and delete post by proving 'id'.

    ```bash
        /postlike-view-set/
    ```
    * This end point is used to get details of which post is liked by which user.
    
        * if we are using **GET** method with this endpoint then we will get post's like details.
        * if we are using **POST** method then it means you want to like the post, so for this we have to provide post (id of that post which you want to like) and like_user (id of the user who want to like) in body parameters. You can check and hit the **/posts/** endpoint with **GET** method here you can see the likes field will increments by 1 it means post is liked.
        * if you want to unlike the same post then you have to use **PUT** method and also you have to provide same post and same like_user details in body parameters then this will unlike the post, you can check the **/posts/** endpoint with **GET** method here you can see the likes field will decrements by 1 it means post is unliked.


#### **NOTE 1** : While hitting the APIs endpoints you may suffer with token invalid response then you need to generate or refresh the token again by providing username and password and then you can easily continue your work with APIs.

#### **NOTE 2** : If we down the container and then again up the container then we must create django super user (from another terminal as mentioned above) because it will change the container id.