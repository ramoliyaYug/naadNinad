# notes

## banega kya kya
- android app
- linux app
- website
- gnome extension
- backend

## tech stack
- node js
- dynamoDB
- S3
- Api Gateway

## questions
1. the main question is that from where the music came like who will upload and even if there will come the artist then from where the initial tracks came?

2. how many portals will be there and which exact

3. and what exactly all portals will do

4. will music be streamed or not and yes then how we can do this in serverless without repeating lambda calls and if not then how we will securly play that from cilent won't this be depend on the which client we are making and how to handle that exactly 


## pointers
- we will not give the user the control to manipulate audio library instead we will give the thing called request song then user will give the url of the youtube or anything about that and then it will shows up in admin portal then if i approve that then it will hit the pipe line and iit will produce the song from url and then update s3 and dynamodb and after successfull completion that song will officially on the app.  