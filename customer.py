import multiprocessing
import json
import os

import grpc
import example_pb2_grpc
import example_pb2

class Customer:
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # pointer for the stub
        self.stub = None

    def createStub(self):
        server_address = "localhost:50051"
        channel = grpc.insecure_channel(
            server_address,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
                ("grpc.so_reuseport", 1),
                ("grpc.use_local_subchannel_pool", 1),
            ],
        )
        stub = example_pb2_grpc.RPCServicerStub(channel)
        self.stub = stub

    # to send out the events to the Bank
    def executeEvents(self):
        request = example_pb2.Request(id = self.id, events = self.events )
        response = self.stub.MsgDelivery(request)
        return response

def _run_worker_query(customerInput) :
    customerProcess = Customer(customerInput['id'], customerInput['events'])
    customerProcess.createStub()
    response = customerProcess.executeEvents()
    return response

def run() :
    # load customers data from JSON file
    with open('./input.json', 'r') as f:
        data = json.load(f)

    customersInputList = []
    for x in range(len(data)) :
        if data[x]['type'] == 'client' :
            customersInputList.append(data[x])

    worker_pool = multiprocessing.Pool(processes=len(customersInputList),)
    response = worker_pool.map(_run_worker_query, customersInputList)

    # generating output format and displaying in the console
    responseDict = {}
    for x in range(len(response)) :
        responseDict['id'] = response[x].id
        tempList = []
        for y in range(len(response[x].recv)) :
            recvDict = {}
            recvDict['interface'] = response[x].recv[y].interface
            recvDict['result'] = response[x].recv[y].result
            if(response[x].recv[y].money) :
                recvDict['money'] = response[x].recv[y].money
            tempList.append(recvDict)
        responseDict['recv'] = tempList
        print(responseDict)

if __name__ == "__main__":
    run()