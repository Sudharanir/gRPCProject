# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import example_pb2 as example__pb2


class RPCServicerStub(object):
    """service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MsgDelivery = channel.unary_unary(
                '/RPCServicer/MsgDelivery',
                request_serializer=example__pb2.Request.SerializeToString,
                response_deserializer=example__pb2.Response.FromString,
                )


class RPCServicerServicer(object):
    """service definition
    """

    def MsgDelivery(self, request, context):
        """defining RPC service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RPCServicerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MsgDelivery': grpc.unary_unary_rpc_method_handler(
                    servicer.MsgDelivery,
                    request_deserializer=example__pb2.Request.FromString,
                    response_serializer=example__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RPCServicer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RPCServicer(object):
    """service definition
    """

    @staticmethod
    def MsgDelivery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RPCServicer/MsgDelivery',
            example__pb2.Request.SerializeToString,
            example__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
