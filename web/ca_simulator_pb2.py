# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ca_simulator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x63\x61_simulator.proto\x12\x0c\x63\x61_simulator\"\x1c\n\nSimRequest\x12\x0e\n\x06params\x18\x01 \x01(\t\"\x1e\n\x08SimReply\x12\x12\n\nsimulation\x18\x01 \x01(\t2S\n\tSimEngine\x12\x46\n\x10RunSimulationGif\x12\x18.ca_simulator.SimRequest\x1a\x16.ca_simulator.SimReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ca_simulator_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIMREQUEST._serialized_start=36
  _SIMREQUEST._serialized_end=64
  _SIMREPLY._serialized_start=66
  _SIMREPLY._serialized_end=96
  _SIMENGINE._serialized_start=98
  _SIMENGINE._serialized_end=181
# @@protoc_insertion_point(module_scope)
