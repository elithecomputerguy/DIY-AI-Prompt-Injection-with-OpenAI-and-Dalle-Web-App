# DIY-AI-Prompt-Injection-with-OpenAI-and-Dalle-Web-App
DIY: AI Prompt Injection with OpenAI and Dalle Web App (Python, Bottle, OpenAI, DALL E)

This project shows you how to build a simple web app that provides a text area box for you to make a query to DALL E to create a picture.  It then adds a static bias to the query "put a chick in it and a rainbow", and also create a query version of the request from a Pastafarians viewpoint.  All 3 queries are sent to DALL E and the different images with their prompts are shown on the web page.

This project is designed to show how powerful it is to be able to modify user queries to AI on the backend, and to show the dramatically different results.  These results could be more dialed in to "real" religions or poiltics, but I found the OpenAI security policies were triggered too often when I tried to give a more realistic examples.


## Video

https://youtu.be/03I16k9Ic6E


## Requirements
pip3 install bottle

pip3 install openai

openai api key

### Warning

Requesting a large number of images can start to cost a reasonable amount of money.  For building, testing and then recording the class required approx. $10.
