# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import interfaces.libreasr_pb2 as libreasr__pb2


class ASRStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.Transcribe = channel.unary_unary(
            "/ASR.ASR/Transcribe",
            request_serializer=libreasr__pb2.Audio.SerializeToString,
            response_deserializer=libreasr__pb2.Transcript.FromString,
        )
        self.TranscribeStream = channel.stream_stream(
            "/ASR.ASR/TranscribeStream",
            request_serializer=libreasr__pb2.Audio.SerializeToString,
            response_deserializer=libreasr__pb2.Transcript.FromString,
        )


class ASRServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Transcribe(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TranscribeStream(self, request_iterator, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ASRServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Transcribe": grpc.unary_unary_rpc_method_handler(
            servicer.Transcribe,
            request_deserializer=libreasr__pb2.Audio.FromString,
            response_serializer=libreasr__pb2.Transcript.SerializeToString,
        ),
        "TranscribeStream": grpc.stream_stream_rpc_method_handler(
            servicer.TranscribeStream,
            request_deserializer=libreasr__pb2.Audio.FromString,
            response_serializer=libreasr__pb2.Transcript.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "ASR.ASR", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))