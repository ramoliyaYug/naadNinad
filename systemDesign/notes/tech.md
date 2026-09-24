# Tech Talks & Gambhir Discussion 

- for the playlist playing can we get the order of the tracks in the client and then save some lambda calls and get from direct s3 or we need one lambda call for the presigned url

- and in which format the tracks will be stored in s3 that decision we have to make this is the list (mp3,aac,FLAC)

- i have one flash drive in which there is huge amount of songs and i want that all to added into my app library then how to do that thing

## no's
- cloudfront

## solved things
- yt to mp3 service will be made in python purely and for that we also need ffmpeg and to deploy that to severless we need docker container with all yt-dlp and ffmpeg and then we will host that to fargate, we will have sqs attached to this with s3 

- along with the audio the metadata also will come from the yt-dlp lib and it is giving many informations about the video so we do not need any ai thing for the meta data extraction and the best part is that also we do not need any cover image as well because the yt cdn is also giving the thumbnail url already so yeahhh congo we have saved lots of s3 space 
