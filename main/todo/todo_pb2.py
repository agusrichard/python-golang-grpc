# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo.proto',
  package='todo',
  syntax='proto3',
  serialized_options=b'Z\005/todo',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ntodo.proto\x12\x04todo\"G\n\x11\x43reateTodoRequest\x12\x0e\n\x06userID\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"6\n\x12\x43reateTodoResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"!\n\x0fGetTodosRequest\x12\x0e\n\x06userID\x18\x01 \x01(\x03\"B\n\x10GetTodosResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"0\n\x0eGetTodoRequest\x12\x0e\n\x06itemID\x18\x01 \x01(\x03\x12\x0e\n\x06userID\x18\x02 \x01(\x03\"A\n\x0fGetTodoResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"C\n\x11UpdateTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"6\n\x12UpdateTodoResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1f\n\x11\x44\x65leteTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"6\n\x12\x44\x65leteTodoResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xcd\x02\n\x0bTodoService\x12\x41\n\nCreateTodo\x12\x17.todo.CreateTodoRequest\x1a\x18.todo.CreateTodoResponse\"\x00\x12;\n\x08GetTodos\x12\x15.todo.GetTodosRequest\x1a\x16.todo.GetTodosResponse\"\x00\x12\x38\n\x07GetTodo\x12\x14.todo.GetTodoRequest\x1a\x15.todo.GetTodoResponse\"\x00\x12\x41\n\nUpdateTodo\x12\x17.todo.UpdateTodoRequest\x1a\x18.todo.UpdateTodoResponse\"\x00\x12\x41\n\nDeleteTodo\x12\x17.todo.DeleteTodoRequest\x1a\x18.todo.DeleteTodoResponse\"\x00\x42\x07Z\x05/todob\x06proto3'
)




_CREATETODOREQUEST = _descriptor.Descriptor(
  name='CreateTodoRequest',
  full_name='todo.CreateTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userID', full_name='todo.CreateTodoRequest.userID', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='todo.CreateTodoRequest.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='todo.CreateTodoRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=91,
)


_CREATETODORESPONSE = _descriptor.Descriptor(
  name='CreateTodoResponse',
  full_name='todo.CreateTodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='todo.CreateTodoResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='todo.CreateTodoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=147,
)


_GETTODOSREQUEST = _descriptor.Descriptor(
  name='GetTodosRequest',
  full_name='todo.GetTodosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userID', full_name='todo.GetTodosRequest.userID', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=182,
)


_GETTODOSRESPONSE = _descriptor.Descriptor(
  name='GetTodosResponse',
  full_name='todo.GetTodosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='todo.GetTodosResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='todo.GetTodosResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='todo.GetTodosResponse.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=250,
)


_GETTODOREQUEST = _descriptor.Descriptor(
  name='GetTodoRequest',
  full_name='todo.GetTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='itemID', full_name='todo.GetTodoRequest.itemID', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userID', full_name='todo.GetTodoRequest.userID', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=300,
)


_GETTODORESPONSE = _descriptor.Descriptor(
  name='GetTodoResponse',
  full_name='todo.GetTodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='todo.GetTodoResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='todo.GetTodoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='todo.GetTodoResponse.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=302,
  serialized_end=367,
)


_UPDATETODOREQUEST = _descriptor.Descriptor(
  name='UpdateTodoRequest',
  full_name='todo.UpdateTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.UpdateTodoRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='todo.UpdateTodoRequest.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='todo.UpdateTodoRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=436,
)


_UPDATETODORESPONSE = _descriptor.Descriptor(
  name='UpdateTodoResponse',
  full_name='todo.UpdateTodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='todo.UpdateTodoResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='todo.UpdateTodoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=492,
)


_DELETETODOREQUEST = _descriptor.Descriptor(
  name='DeleteTodoRequest',
  full_name='todo.DeleteTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.DeleteTodoRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=494,
  serialized_end=525,
)


_DELETETODORESPONSE = _descriptor.Descriptor(
  name='DeleteTodoResponse',
  full_name='todo.DeleteTodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='todo.DeleteTodoResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='todo.DeleteTodoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=581,
)

DESCRIPTOR.message_types_by_name['CreateTodoRequest'] = _CREATETODOREQUEST
DESCRIPTOR.message_types_by_name['CreateTodoResponse'] = _CREATETODORESPONSE
DESCRIPTOR.message_types_by_name['GetTodosRequest'] = _GETTODOSREQUEST
DESCRIPTOR.message_types_by_name['GetTodosResponse'] = _GETTODOSRESPONSE
DESCRIPTOR.message_types_by_name['GetTodoRequest'] = _GETTODOREQUEST
DESCRIPTOR.message_types_by_name['GetTodoResponse'] = _GETTODORESPONSE
DESCRIPTOR.message_types_by_name['UpdateTodoRequest'] = _UPDATETODOREQUEST
DESCRIPTOR.message_types_by_name['UpdateTodoResponse'] = _UPDATETODORESPONSE
DESCRIPTOR.message_types_by_name['DeleteTodoRequest'] = _DELETETODOREQUEST
DESCRIPTOR.message_types_by_name['DeleteTodoResponse'] = _DELETETODORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateTodoRequest = _reflection.GeneratedProtocolMessageType('CreateTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETODOREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.CreateTodoRequest)
  })
_sym_db.RegisterMessage(CreateTodoRequest)

CreateTodoResponse = _reflection.GeneratedProtocolMessageType('CreateTodoResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATETODORESPONSE,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.CreateTodoResponse)
  })
_sym_db.RegisterMessage(CreateTodoResponse)

GetTodosRequest = _reflection.GeneratedProtocolMessageType('GetTodosRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTODOSREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.GetTodosRequest)
  })
_sym_db.RegisterMessage(GetTodosRequest)

GetTodosResponse = _reflection.GeneratedProtocolMessageType('GetTodosResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTODOSRESPONSE,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.GetTodosResponse)
  })
_sym_db.RegisterMessage(GetTodosResponse)

GetTodoRequest = _reflection.GeneratedProtocolMessageType('GetTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTODOREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.GetTodoRequest)
  })
_sym_db.RegisterMessage(GetTodoRequest)

GetTodoResponse = _reflection.GeneratedProtocolMessageType('GetTodoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTODORESPONSE,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.GetTodoResponse)
  })
_sym_db.RegisterMessage(GetTodoResponse)

UpdateTodoRequest = _reflection.GeneratedProtocolMessageType('UpdateTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETODOREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.UpdateTodoRequest)
  })
_sym_db.RegisterMessage(UpdateTodoRequest)

UpdateTodoResponse = _reflection.GeneratedProtocolMessageType('UpdateTodoResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETODORESPONSE,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.UpdateTodoResponse)
  })
_sym_db.RegisterMessage(UpdateTodoResponse)

DeleteTodoRequest = _reflection.GeneratedProtocolMessageType('DeleteTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETODOREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.DeleteTodoRequest)
  })
_sym_db.RegisterMessage(DeleteTodoRequest)

DeleteTodoResponse = _reflection.GeneratedProtocolMessageType('DeleteTodoResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETETODORESPONSE,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.DeleteTodoResponse)
  })
_sym_db.RegisterMessage(DeleteTodoResponse)


DESCRIPTOR._options = None

_TODOSERVICE = _descriptor.ServiceDescriptor(
  name='TodoService',
  full_name='todo.TodoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=584,
  serialized_end=917,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateTodo',
    full_name='todo.TodoService.CreateTodo',
    index=0,
    containing_service=None,
    input_type=_CREATETODOREQUEST,
    output_type=_CREATETODORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTodos',
    full_name='todo.TodoService.GetTodos',
    index=1,
    containing_service=None,
    input_type=_GETTODOSREQUEST,
    output_type=_GETTODOSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTodo',
    full_name='todo.TodoService.GetTodo',
    index=2,
    containing_service=None,
    input_type=_GETTODOREQUEST,
    output_type=_GETTODORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTodo',
    full_name='todo.TodoService.UpdateTodo',
    index=3,
    containing_service=None,
    input_type=_UPDATETODOREQUEST,
    output_type=_UPDATETODORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTodo',
    full_name='todo.TodoService.DeleteTodo',
    index=4,
    containing_service=None,
    input_type=_DELETETODOREQUEST,
    output_type=_DELETETODORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODOSERVICE)

DESCRIPTOR.services_by_name['TodoService'] = _TODOSERVICE

# @@protoc_insertion_point(module_scope)