# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor_source.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensor_source.proto',
  package='common.sensor',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13sensor_source.proto\x12\rcommon.sensor*\xb8\x0e\n\x0cSensorSource\x12\x11\n\rUnknownSource\x10\x00\x12\r\n\tLidarMain\x10\x01\x12\x11\n\rLidarTailLeft\x10\x02\x12\x12\n\x0eLidarTailRight\x10\x03\x12\x10\n\x0cLidarHeadMid\x10\x04\x12\x0e\n\nLidarMerge\x10\x05\x12\x10\n\x0cLidarTailMid\x10\x06\x12\x11\n\rLidarHeadLeft\x10\x07\x12\x12\n\x0eLidarHeadRight\x10\x08\x12\x10\n\x0cLidarMidLeft\x10\\\x12\x11\n\rLidarMidRight\x10]\x12\x10\n\x0cLidarTopLeft\x10^\x12\x11\n\rLidarTopRight\x10_\x12\x10\n\x0bLidarTopMid\x10\xfa\x01\x12\x10\n\x0cRadarTailMid\x10\x14\x12\x10\n\x0cRadarHeadMid\x10\x15\x12\x12\n\x0e\x43\x61meraHeadLeft\x10(\x12\x13\n\x0f\x43\x61meraHeadRight\x10)\x12\x13\n\x0f\x43\x61meraFrontLeft\x10*\x12\x14\n\x10\x43\x61meraFrontRight\x10+\x12\x11\n\rCameraMidLeft\x10,\x12\x12\n\x0e\x43\x61meraMidRight\x10-\x12\x12\n\x0e\x43\x61meraTailLeft\x10.\x12\x13\n\x0f\x43\x61meraTailRight\x10/\x12\x16\n\x12\x43\x61meraTrafficLight\x10\x30\x12\x11\n\rVehicleCenter\x10<\x12\x0f\n\x0b\x41sensingIns\x10=\x12\t\n\x05World\x10\x46\x12\x0c\n\x08\x45goFront\x10G\x12\x0f\n\x0b\x46usionTrack\x10Q\x12\r\n\tFusionPre\x10R\x12\x19\n\x15\x46usionLidarRadarMerge\x10S\x12\x10\n\x0cVisualizeRaw\x10[\x12\x11\n\rSyncLidarHead\x10\x64\x12\x16\n\x12SyncLidarFrontLeft\x10\x65\x12\x17\n\x13SyncLidarFrontRight\x10\x66\x12\x14\n\x10SyncLidarMidLeft\x10g\x12\x15\n\x11SyncLidarMidRight\x10h\x12\x15\n\x11SyncLidarTailLeft\x10i\x12\x16\n\x12SyncLidarTailRight\x10j\x12\x15\n\x11SyncLidarHeadLeft\x10k\x12\x16\n\x12SyncLidarHeadRight\x10l\x12\x14\n\x10SyncLidarTailMid\x10m\x12\x14\n\x0fSyncLidarTopMid\x10\xfb\x01\x12\x1c\n\x17UltrasonicRadarHeadLeft\x10\x83\x01\x12\x1b\n\x16UltrasonicRadarHeadMid\x10\x84\x01\x12\x1d\n\x18UltrasonicRadarHeadRight\x10\x85\x01\x12\x1e\n\x19UltrasonicRadarRightFront\x10\x86\x01\x12!\n\x1cUltrasonicRadarRightMidFront\x10\x87\x01\x12 \n\x1bUltrasonicRadarRightMidRear\x10\x88\x01\x12\x1d\n\x18UltrasonicRadarRightRear\x10\x89\x01\x12\x1d\n\x18UltrasonicRadarLeftFront\x10\x8a\x01\x12 \n\x1bUltrasonicRadarLeftMidFront\x10\x8b\x01\x12\x1f\n\x1aUltrasonicRadarLeftMidRear\x10\x8c\x01\x12\x1c\n\x17UltrasonicRadarLeftRear\x10\x8d\x01\x12\x1c\n\x17UltrasonicRadarTailLeft\x10\x8e\x01\x12\x1b\n\x16UltrasonicRadarTailMid\x10\x8f\x01\x12\x1d\n\x18UltrasonicRadarTailRight\x10\x90\x01\x12\x1f\n\x1aUltrasonicRadarCenterFront\x10\x91\x01\x12\x1d\n\x18UltrasonicRadarCenterMid\x10\x92\x01\x12\x1e\n\x19UltrasonicRadarCenterRear\x10\x93\x01\x12\x14\n\x0fUltrasonicRadar\x10\x94\x01\x12\x1f\n\x1aUltrasonicRadarHeadLeftSub\x10\x95\x01\x12\x1e\n\x19UltrasonicRadarHeadMidSub\x10\x96\x01\x12 \n\x1bUltrasonicRadarHeadRightSub\x10\x97\x01\x12\x1f\n\x1aUltrasonicRadarTailLeftSub\x10\x98\x01\x12\x1e\n\x19UltrasonicRadarTailMidSub\x10\x99\x01\x12 \n\x1bUltrasonicRadarTailRightSub\x10\x9a\x01\x12\x1b\n\x16UltrasonicRadarHubZero\x10\xa0\x01\x12\x1a\n\x15UltrasonicRadarHubOne\x10\xa1\x01\x12\x1a\n\x15UltrasonicRadarHubTwo\x10\xa2\x01\x12\x1c\n\x17UltrasonicRadarHubThree\x10\xa3\x01\x12\n\n\x05Laser\x10\xb4\x01\x12\x0e\n\tLaserZero\x10\xb5\x01\x12\x10\n\x0bV2X_BROADXT\x10\xc8\x01\x12\r\n\x08Rainfall\x10\x84\x02\x12\x0f\n\nEleMonitor\x10\x85\x02\x12\x0e\n\tBayuRadar\x10\x8e\x02*w\n\nSensorType\x12\x0b\n\x07Unknown\x10\x00\x12\t\n\x05Lidar\x10\x01\x12\t\n\x05Radar\x10\x02\x12\n\n\x06\x43\x61mera\x10\x03\x12\n\n\x06\x46usion\x10\x04\x12\x0e\n\nUltrasonic\x10\x05\x12\x08\n\x04Sync\x10\x06\x12\x07\n\x03V2X\x10\x07\x12\x0b\n\x07Monitor\x10\x08'
)

_SENSORSOURCE = _descriptor.EnumDescriptor(
  name='SensorSource',
  full_name='common.sensor.SensorSource',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UnknownSource', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarMain', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarTailLeft', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarTailRight', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarHeadMid', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarMerge', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarTailMid', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarHeadLeft', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarHeadRight', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarMidLeft', index=9, number=92,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarMidRight', index=10, number=93,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarTopLeft', index=11, number=94,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarTopRight', index=12, number=95,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LidarTopMid', index=13, number=250,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RadarTailMid', index=14, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RadarHeadMid', index=15, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CameraHeadLeft', index=16, number=40,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CameraHeadRight', index=17, number=41,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CameraFrontLeft', index=18, number=42,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CameraFrontRight', index=19, number=43,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CameraMidLeft', index=20, number=44,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CameraMidRight', index=21, number=45,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CameraTailLeft', index=22, number=46,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CameraTailRight', index=23, number=47,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CameraTrafficLight', index=24, number=48,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VehicleCenter', index=25, number=60,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AsensingIns', index=26, number=61,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='World', index=27, number=70,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EgoFront', index=28, number=71,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FusionTrack', index=29, number=81,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FusionPre', index=30, number=82,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FusionLidarRadarMerge', index=31, number=83,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VisualizeRaw', index=32, number=91,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SyncLidarHead', index=33, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SyncLidarFrontLeft', index=34, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SyncLidarFrontRight', index=35, number=102,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SyncLidarMidLeft', index=36, number=103,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SyncLidarMidRight', index=37, number=104,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SyncLidarTailLeft', index=38, number=105,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SyncLidarTailRight', index=39, number=106,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SyncLidarHeadLeft', index=40, number=107,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SyncLidarHeadRight', index=41, number=108,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SyncLidarTailMid', index=42, number=109,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SyncLidarTopMid', index=43, number=251,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarHeadLeft', index=44, number=131,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarHeadMid', index=45, number=132,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarHeadRight', index=46, number=133,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarRightFront', index=47, number=134,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarRightMidFront', index=48, number=135,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarRightMidRear', index=49, number=136,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarRightRear', index=50, number=137,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarLeftFront', index=51, number=138,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarLeftMidFront', index=52, number=139,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarLeftMidRear', index=53, number=140,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarLeftRear', index=54, number=141,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarTailLeft', index=55, number=142,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarTailMid', index=56, number=143,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarTailRight', index=57, number=144,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarCenterFront', index=58, number=145,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarCenterMid', index=59, number=146,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarCenterRear', index=60, number=147,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadar', index=61, number=148,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarHeadLeftSub', index=62, number=149,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarHeadMidSub', index=63, number=150,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarHeadRightSub', index=64, number=151,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarTailLeftSub', index=65, number=152,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarTailMidSub', index=66, number=153,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarTailRightSub', index=67, number=154,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarHubZero', index=68, number=160,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarHubOne', index=69, number=161,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarHubTwo', index=70, number=162,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UltrasonicRadarHubThree', index=71, number=163,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Laser', index=72, number=180,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LaserZero', index=73, number=181,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V2X_BROADXT', index=74, number=200,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Rainfall', index=75, number=260,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EleMonitor', index=76, number=261,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BayuRadar', index=77, number=270,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=39,
  serialized_end=1887,
)
_sym_db.RegisterEnumDescriptor(_SENSORSOURCE)

SensorSource = enum_type_wrapper.EnumTypeWrapper(_SENSORSOURCE)
_SENSORTYPE = _descriptor.EnumDescriptor(
  name='SensorType',
  full_name='common.sensor.SensorType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Lidar', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Radar', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Camera', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Fusion', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Ultrasonic', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Sync', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V2X', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Monitor', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1889,
  serialized_end=2008,
)
_sym_db.RegisterEnumDescriptor(_SENSORTYPE)

SensorType = enum_type_wrapper.EnumTypeWrapper(_SENSORTYPE)
UnknownSource = 0
LidarMain = 1
LidarTailLeft = 2
LidarTailRight = 3
LidarHeadMid = 4
LidarMerge = 5
LidarTailMid = 6
LidarHeadLeft = 7
LidarHeadRight = 8
LidarMidLeft = 92
LidarMidRight = 93
LidarTopLeft = 94
LidarTopRight = 95
LidarTopMid = 250
RadarTailMid = 20
RadarHeadMid = 21
CameraHeadLeft = 40
CameraHeadRight = 41
CameraFrontLeft = 42
CameraFrontRight = 43
CameraMidLeft = 44
CameraMidRight = 45
CameraTailLeft = 46
CameraTailRight = 47
CameraTrafficLight = 48
VehicleCenter = 60
AsensingIns = 61
World = 70
EgoFront = 71
FusionTrack = 81
FusionPre = 82
FusionLidarRadarMerge = 83
VisualizeRaw = 91
SyncLidarHead = 100
SyncLidarFrontLeft = 101
SyncLidarFrontRight = 102
SyncLidarMidLeft = 103
SyncLidarMidRight = 104
SyncLidarTailLeft = 105
SyncLidarTailRight = 106
SyncLidarHeadLeft = 107
SyncLidarHeadRight = 108
SyncLidarTailMid = 109
SyncLidarTopMid = 251
UltrasonicRadarHeadLeft = 131
UltrasonicRadarHeadMid = 132
UltrasonicRadarHeadRight = 133
UltrasonicRadarRightFront = 134
UltrasonicRadarRightMidFront = 135
UltrasonicRadarRightMidRear = 136
UltrasonicRadarRightRear = 137
UltrasonicRadarLeftFront = 138
UltrasonicRadarLeftMidFront = 139
UltrasonicRadarLeftMidRear = 140
UltrasonicRadarLeftRear = 141
UltrasonicRadarTailLeft = 142
UltrasonicRadarTailMid = 143
UltrasonicRadarTailRight = 144
UltrasonicRadarCenterFront = 145
UltrasonicRadarCenterMid = 146
UltrasonicRadarCenterRear = 147
UltrasonicRadar = 148
UltrasonicRadarHeadLeftSub = 149
UltrasonicRadarHeadMidSub = 150
UltrasonicRadarHeadRightSub = 151
UltrasonicRadarTailLeftSub = 152
UltrasonicRadarTailMidSub = 153
UltrasonicRadarTailRightSub = 154
UltrasonicRadarHubZero = 160
UltrasonicRadarHubOne = 161
UltrasonicRadarHubTwo = 162
UltrasonicRadarHubThree = 163
Laser = 180
LaserZero = 181
V2X_BROADXT = 200
Rainfall = 260
EleMonitor = 261
BayuRadar = 270
Unknown = 0
Lidar = 1
Radar = 2
Camera = 3
Fusion = 4
Ultrasonic = 5
Sync = 6
V2X = 7
Monitor = 8


DESCRIPTOR.enum_types_by_name['SensorSource'] = _SENSORSOURCE
DESCRIPTOR.enum_types_by_name['SensorType'] = _SENSORTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)