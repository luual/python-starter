# Python boilerplate for Flask Rest-API

WIP

This example show how to create a minimal Flask api with docker integration

## Docker integration

Build the application with the following command:

```docker build -t <YOUR_CONTAINER_NAME> .```


### With Docker Desktop

In Docker desktop, the image should be available with the <YOUR_CONTAINER_NAME> label.

You can start the image with the run button don't forget to port forward the application.

### Command Line

In command line, you can start the application with

```docker run -dp 127.0.0.1:5050:5050 <YOUR_CONTAINER_NAME>```

