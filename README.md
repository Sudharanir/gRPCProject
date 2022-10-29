**gRPC project for distributed banking system**

  This project is about creating a Distributed banking system application that takes customer requests to deposit and withdraw money and processes the requests using gRPC. It makes real time updates to the bank balance in all the branches after processing each customer request.

**Getting Started:**

Below step by step instructions will enable you to get the application up and running in your local machine for development and testing purposes.

**Prerequisites:**

Minimum system requirements for running the program in local machine:
	Python 3.5 or higher
	pip version 9.0.1 or higher

If necessary, upgrade your version of pip:

python -m pip install --upgrade pip

Step1: Install gRPC : python -m pip install grpcio

Step2: Install gRPC tools : python -m pip install grpcio-tools

Step3: Generate gRPC code : python -m grpc_tools.protoc -I./protos protos/example.proto --python_out=. --grpc_python_out=.

**Steps for starting the banking application software:**

Step1: Run the server : python branch.python

Step2: Run the client : python customer.py

Note : Input data is provided in input.json file

**Usage:**

input.json is the key input file through which we can provide customer requests and bank branches information as inputs to the application.

This program can be used by customers:
1. To deposit money into branch
2. To withdraw money from branch
3. To retrieve bank balance amount
	
