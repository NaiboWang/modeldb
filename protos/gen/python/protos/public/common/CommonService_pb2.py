# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/public/common/CommonService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/public/common/CommonService.proto',
  package='ai.verta.common',
  syntax='proto3',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n(protos/public/common/CommonService.proto\x12\x0f\x61i.verta.common\x1a\x1cgoogle/api/annotations.proto\":\n\x0bTernaryEnum\"+\n\x07Ternary\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04TRUE\x10\x01\x12\t\n\x05\x46\x41LSE\x10\x02\x42\x02P\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_TERNARYENUM_TERNARY = _descriptor.EnumDescriptor(
  name='Ternary',
  full_name='ai.verta.common.TernaryEnum.Ternary',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRUE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FALSE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=106,
  serialized_end=149,
)
_sym_db.RegisterEnumDescriptor(_TERNARYENUM_TERNARY)


_TERNARYENUM = _descriptor.Descriptor(
  name='TernaryEnum',
  full_name='ai.verta.common.TernaryEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TERNARYENUM_TERNARY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=149,
)

_TERNARYENUM_TERNARY.containing_type = _TERNARYENUM
DESCRIPTOR.message_types_by_name['TernaryEnum'] = _TERNARYENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TernaryEnum = _reflection.GeneratedProtocolMessageType('TernaryEnum', (_message.Message,), dict(
  DESCRIPTOR = _TERNARYENUM,
  __module__ = 'protos.public.common.CommonService_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.common.TernaryEnum)
  ))
_sym_db.RegisterMessage(TernaryEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
