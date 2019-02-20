# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vector.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='vector.proto',
    package='robotics.messages',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x0cvector.proto\x12\x11robotics.messages\"6\n\x08Vector4d\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\t\n\x01w\x18\x04 \x01(\x01\"6\n\x08Vector4f\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01w\x18\x04 \x01(\x02\"+\n\x08Vector3d\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"+\n\x08Vector3f\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\" \n\x08Vector2d\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\" \n\x08Vector2f\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"\x1b\n\x07Vectord\x12\x10\n\x04\x64\x61ta\x18\x01 \x03(\x01\x42\x02\x10\x01\"\x1b\n\x07Vectorf\x12\x10\n\x04\x64\x61ta\x18\x01 \x03(\x02\x42\x02\x10\x01\x62\x06proto3'
    ))

_VECTOR4D = _descriptor.Descriptor(
    name='Vector4d',
    full_name='robotics.messages.Vector4d',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='x',
            full_name='robotics.messages.Vector4d.x',
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='y',
            full_name='robotics.messages.Vector4d.y',
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='z',
            full_name='robotics.messages.Vector4d.z',
            index=2,
            number=3,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='w',
            full_name='robotics.messages.Vector4d.w',
            index=3,
            number=4,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=35,
    serialized_end=89,
)

_VECTOR4F = _descriptor.Descriptor(
    name='Vector4f',
    full_name='robotics.messages.Vector4f',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='x',
            full_name='robotics.messages.Vector4f.x',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='y',
            full_name='robotics.messages.Vector4f.y',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='z',
            full_name='robotics.messages.Vector4f.z',
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='w',
            full_name='robotics.messages.Vector4f.w',
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=91,
    serialized_end=145,
)

_VECTOR3D = _descriptor.Descriptor(
    name='Vector3d',
    full_name='robotics.messages.Vector3d',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='x',
            full_name='robotics.messages.Vector3d.x',
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='y',
            full_name='robotics.messages.Vector3d.y',
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='z',
            full_name='robotics.messages.Vector3d.z',
            index=2,
            number=3,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=147,
    serialized_end=190,
)

_VECTOR3F = _descriptor.Descriptor(
    name='Vector3f',
    full_name='robotics.messages.Vector3f',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='x',
            full_name='robotics.messages.Vector3f.x',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='y',
            full_name='robotics.messages.Vector3f.y',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='z',
            full_name='robotics.messages.Vector3f.z',
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=192,
    serialized_end=235,
)

_VECTOR2D = _descriptor.Descriptor(
    name='Vector2d',
    full_name='robotics.messages.Vector2d',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='x',
            full_name='robotics.messages.Vector2d.x',
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='y',
            full_name='robotics.messages.Vector2d.y',
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=237,
    serialized_end=269,
)

_VECTOR2F = _descriptor.Descriptor(
    name='Vector2f',
    full_name='robotics.messages.Vector2f',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='x',
            full_name='robotics.messages.Vector2f.x',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='y',
            full_name='robotics.messages.Vector2f.y',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=271,
    serialized_end=303,
)

_VECTORD = _descriptor.Descriptor(
    name='Vectord',
    full_name='robotics.messages.Vectord',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='data',
            full_name='robotics.messages.Vectord.data',
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')),
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=305,
    serialized_end=332,
)

_VECTORF = _descriptor.Descriptor(
    name='Vectorf',
    full_name='robotics.messages.Vectorf',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='data',
            full_name='robotics.messages.Vectorf.data',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')),
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=334,
    serialized_end=361,
)

DESCRIPTOR.message_types_by_name['Vector4d'] = _VECTOR4D
DESCRIPTOR.message_types_by_name['Vector4f'] = _VECTOR4F
DESCRIPTOR.message_types_by_name['Vector3d'] = _VECTOR3D
DESCRIPTOR.message_types_by_name['Vector3f'] = _VECTOR3F
DESCRIPTOR.message_types_by_name['Vector2d'] = _VECTOR2D
DESCRIPTOR.message_types_by_name['Vector2f'] = _VECTOR2F
DESCRIPTOR.message_types_by_name['Vectord'] = _VECTORD
DESCRIPTOR.message_types_by_name['Vectorf'] = _VECTORF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vector4d = _reflection.GeneratedProtocolMessageType(
    'Vector4d',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_VECTOR4D,
        __module__='vector_pb2'
        # @@protoc_insertion_point(class_scope:robotics.messages.Vector4d)
    ))
_sym_db.RegisterMessage(Vector4d)

Vector4f = _reflection.GeneratedProtocolMessageType(
    'Vector4f',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_VECTOR4F,
        __module__='vector_pb2'
        # @@protoc_insertion_point(class_scope:robotics.messages.Vector4f)
    ))
_sym_db.RegisterMessage(Vector4f)

Vector3d = _reflection.GeneratedProtocolMessageType(
    'Vector3d',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_VECTOR3D,
        __module__='vector_pb2'
        # @@protoc_insertion_point(class_scope:robotics.messages.Vector3d)
    ))
_sym_db.RegisterMessage(Vector3d)

Vector3f = _reflection.GeneratedProtocolMessageType(
    'Vector3f',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_VECTOR3F,
        __module__='vector_pb2'
        # @@protoc_insertion_point(class_scope:robotics.messages.Vector3f)
    ))
_sym_db.RegisterMessage(Vector3f)

Vector2d = _reflection.GeneratedProtocolMessageType(
    'Vector2d',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_VECTOR2D,
        __module__='vector_pb2'
        # @@protoc_insertion_point(class_scope:robotics.messages.Vector2d)
    ))
_sym_db.RegisterMessage(Vector2d)

Vector2f = _reflection.GeneratedProtocolMessageType(
    'Vector2f',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_VECTOR2F,
        __module__='vector_pb2'
        # @@protoc_insertion_point(class_scope:robotics.messages.Vector2f)
    ))
_sym_db.RegisterMessage(Vector2f)

Vectord = _reflection.GeneratedProtocolMessageType(
    'Vectord',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_VECTORD,
        __module__='vector_pb2'
        # @@protoc_insertion_point(class_scope:robotics.messages.Vectord)
    ))
_sym_db.RegisterMessage(Vectord)

Vectorf = _reflection.GeneratedProtocolMessageType(
    'Vectorf',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_VECTORF,
        __module__='vector_pb2'
        # @@protoc_insertion_point(class_scope:robotics.messages.Vectorf)
    ))
_sym_db.RegisterMessage(Vectorf)

_VECTORD.fields_by_name['data'].has_options = True
_VECTORD.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(),
                                                                     _b('\020\001'))
_VECTORF.fields_by_name['data'].has_options = True
_VECTORF.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(),
                                                                     _b('\020\001'))
# @@protoc_insertion_point(module_scope)
