# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ..monitoring import DataMonitoringService_pb2 as monitoring_dot_DataMonitoringService__pb2


class DataMonitoringServiceStub(object):
  """// Alert Definition

  message SeverityEnum {
  enum Severity {
  UNDEFINED = 0;
  LOW = 1;
  MEDIUM = 2;
  HIGH = 3;
  }
  }

  // TODO: pull in all fields from https://vertaai.atlassian.net/browse/VR-9906

  message AlertDefinition {
  uint64 id = 1;
  string name = 2;
  uint64 monitored_entity_id = 3;
  uint64 reference_data_source_id = 4;
  uint64 source_profiler_id = 5;
  uint64 created_at_millis = 6;
  uint64 updated_at_millis = 7;
  float threshold = 8;
  SeverityEnum.Severity severity = 9;
  string webhook = 10;
  }

  message GetAlertDefinitionRequest {
  uint64 id = 1;

  message Response {
  AlertDefinition alert_definition = 1;
  }
  }

  message CreateAlertDefinitionRequest {
  string name = 1;
  uint64 monitored_entity_id = 2;
  uint64 reference_data_source_id = 3;
  uint64 source_profiler_id = 4;
  float threshold = 5;
  SeverityEnum.Severity severity = 6;
  string webhook =7;

  message Response {
  AlertDefinition alert_definition = 1;
  }
  }

  message UpdateAlertDefinitionRequest {
  uint64 id = 1;
  string name = 2;
  uint64 reference_data_source_id = 3;
  uint64 source_profiler_id = 4;
  float threshold = 5;
  SeverityEnum.Severity severity = 6;
  string webhook = 7;

  message Response {
  AlertDefinition alert_definition = 1;
  }
  }

  message ListAlertDefinitionsRequest {
  uint64 monitored_entity_id = 1;
  message Response {
  repeated AlertDefinition alert_definition = 1;
  }
  }

  message DeleteAlertDefinitionRequest {
  uint64 id = 1;

  message Response {
  }
  }

  // Alert

  message Alert {
  uint64 id = 1;
  string name = 2;
  uint64 alert_definition_id = 3;
  uint64 created_at_millis = 4;
  uint64 updated_at_millis = 5;
  uint64 triggered_at_millis = 6;
  uint64 acked_at_millis = 7;
  uint64 closed_at_millis = 8;
  }

  message GetAlertRequest {
  uint64 id = 1;

  message Response {
  Alert alert = 1;
  }
  }

  message CreateAlertRequest {
  string name = 1;
  uint64 alert_definition_id = 2;
  uint64 triggered_at_millis = 3;
  uint64 acked_at_millis = 4;
  uint64 closed_at_millis = 5;

  message Response {
  Alert alert = 1;
  }
  }

  message UpdateAlertRequest {
  uint64 id = 1;
  string name = 2;
  uint64 triggered_at_millis = 3;
  uint64 acked_at_millis = 4;
  uint64 closed_at_millis = 5;

  message Response {
  Alert alert = 1;
  }
  }

  message ListAlertsRequest {
  uint64 alert_definition_id = 1;

  message Response {
  repeated Alert alert = 1;
  }
  }

  message DeleteAlertRequest {
  uint64 id = 1;

  message Response {
  }
  }

  Service definitions
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getMonitoredEntity = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/getMonitoredEntity',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.GetMonitoredEntityRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.GetMonitoredEntityRequest.Response.FromString,
        )
    self.getMonitoredEntityByName = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/getMonitoredEntityByName',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.GetMonitoredEntityByNameRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.GetMonitoredEntityByNameRequest.Response.FromString,
        )
    self.createMonitoredEntity = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/createMonitoredEntity',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.CreateMonitoredEntityRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.CreateMonitoredEntityRequest.Response.FromString,
        )
    self.updateMonitoredEntity = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/updateMonitoredEntity',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.UpdateMonitoredEntityRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.UpdateMonitoredEntityRequest.Response.FromString,
        )
    self.listMonitoredEntities = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/listMonitoredEntities',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.ListMonitoredEntitiesRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.ListMonitoredEntitiesRequest.Response.FromString,
        )
    self.deleteMonitoredEntity = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/deleteMonitoredEntity',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.DeleteMonitoredEntityRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.DeleteMonitoredEntityRequest.Response.FromString,
        )
    self.getDataSource = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/getDataSource',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.GetDataSourceRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.GetDataSourceRequest.Response.FromString,
        )
    self.findDataSources = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/findDataSources',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.FindDataSourcesRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.FindDataSourcesRequest.Response.FromString,
        )
    self.createDataSource = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/createDataSource',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.CreateDataSourceRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.CreateDataSourceRequest.Response.FromString,
        )
    self.listDataSources = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/listDataSources',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.ListDataSourcesRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.ListDataSourcesRequest.Response.FromString,
        )
    self.deleteDataSource = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/deleteDataSource',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.DeleteDataSourceRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.DeleteDataSourceRequest.Response.FromString,
        )
    self.getProfiler = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/getProfiler',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.GetProfilerRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.GetProfilerRequest.Response.FromString,
        )
    self.createProfiler = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/createProfiler',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.CreateProfilerRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.CreateProfilerRequest.Response.FromString,
        )
    self.updateProfiler = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/updateProfiler',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.UpdateProfilerRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.UpdateProfilerRequest.Response.FromString,
        )
    self.listProfilers = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/listProfilers',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.ListProfilersRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.ListProfilersRequest.Response.FromString,
        )
    self.deleteProfiler = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/deleteProfiler',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.DeleteProfilerRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.DeleteProfilerRequest.Response.FromString,
        )
    self.getProfilerStatus = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/getProfilerStatus',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.GetProfilerStatusRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.GetProfilerStatusRequest.Response.FromString,
        )
    self.findProfilersForMonitoredEntity = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/findProfilersForMonitoredEntity',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.FindProfilersForMonitoredEntityRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.FindProfilersForMonitoredEntityRequest.Response.FromString,
        )
    self.enableProfiler = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/enableProfiler',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.EnableProfilerRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.EnableProfilerRequest.Response.FromString,
        )
    self.disableProfiler = channel.unary_unary(
        '/ai.verta.monitoring.DataMonitoringService/disableProfiler',
        request_serializer=monitoring_dot_DataMonitoringService__pb2.DisableProfilerRequest.SerializeToString,
        response_deserializer=monitoring_dot_DataMonitoringService__pb2.DisableProfilerRequest.Response.FromString,
        )


class DataMonitoringServiceServicer(object):
  """// Alert Definition

  message SeverityEnum {
  enum Severity {
  UNDEFINED = 0;
  LOW = 1;
  MEDIUM = 2;
  HIGH = 3;
  }
  }

  // TODO: pull in all fields from https://vertaai.atlassian.net/browse/VR-9906

  message AlertDefinition {
  uint64 id = 1;
  string name = 2;
  uint64 monitored_entity_id = 3;
  uint64 reference_data_source_id = 4;
  uint64 source_profiler_id = 5;
  uint64 created_at_millis = 6;
  uint64 updated_at_millis = 7;
  float threshold = 8;
  SeverityEnum.Severity severity = 9;
  string webhook = 10;
  }

  message GetAlertDefinitionRequest {
  uint64 id = 1;

  message Response {
  AlertDefinition alert_definition = 1;
  }
  }

  message CreateAlertDefinitionRequest {
  string name = 1;
  uint64 monitored_entity_id = 2;
  uint64 reference_data_source_id = 3;
  uint64 source_profiler_id = 4;
  float threshold = 5;
  SeverityEnum.Severity severity = 6;
  string webhook =7;

  message Response {
  AlertDefinition alert_definition = 1;
  }
  }

  message UpdateAlertDefinitionRequest {
  uint64 id = 1;
  string name = 2;
  uint64 reference_data_source_id = 3;
  uint64 source_profiler_id = 4;
  float threshold = 5;
  SeverityEnum.Severity severity = 6;
  string webhook = 7;

  message Response {
  AlertDefinition alert_definition = 1;
  }
  }

  message ListAlertDefinitionsRequest {
  uint64 monitored_entity_id = 1;
  message Response {
  repeated AlertDefinition alert_definition = 1;
  }
  }

  message DeleteAlertDefinitionRequest {
  uint64 id = 1;

  message Response {
  }
  }

  // Alert

  message Alert {
  uint64 id = 1;
  string name = 2;
  uint64 alert_definition_id = 3;
  uint64 created_at_millis = 4;
  uint64 updated_at_millis = 5;
  uint64 triggered_at_millis = 6;
  uint64 acked_at_millis = 7;
  uint64 closed_at_millis = 8;
  }

  message GetAlertRequest {
  uint64 id = 1;

  message Response {
  Alert alert = 1;
  }
  }

  message CreateAlertRequest {
  string name = 1;
  uint64 alert_definition_id = 2;
  uint64 triggered_at_millis = 3;
  uint64 acked_at_millis = 4;
  uint64 closed_at_millis = 5;

  message Response {
  Alert alert = 1;
  }
  }

  message UpdateAlertRequest {
  uint64 id = 1;
  string name = 2;
  uint64 triggered_at_millis = 3;
  uint64 acked_at_millis = 4;
  uint64 closed_at_millis = 5;

  message Response {
  Alert alert = 1;
  }
  }

  message ListAlertsRequest {
  uint64 alert_definition_id = 1;

  message Response {
  repeated Alert alert = 1;
  }
  }

  message DeleteAlertRequest {
  uint64 id = 1;

  message Response {
  }
  }

  Service definitions
  """

  def getMonitoredEntity(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getMonitoredEntityByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def createMonitoredEntity(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateMonitoredEntity(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listMonitoredEntities(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteMonitoredEntity(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getDataSource(self, request, context):
    """rpc getSummary(GetSummaryRequest) returns (GetSummaryRequest.Response) {
    option (google.api.http) = {
    get: "/v1/monitored_entity/getSummary"
    };
    };

    rpc findSummary(FindSummaryRequest) returns (FindSummaryRequest.Response) {
    option (google.api.http) = {
    get: "/v1/monitored_entity/findSummary"
    };
    };

    rpc findSummaries(FindSummariesRequest) returns (FindSummariesRequest.Response) {
    option (google.api.http) = {
    get: "/v1/monitored_entity/findSummaries"
    };
    };

    rpc createSummary(CreateSummaryRequest) returns (CreateSummaryRequest.Response) {
    option (google.api.http) = {
    post: "/v1/monitored_entity/createSummary"
    body: "*"
    };
    };

    rpc listSummaries(ListSummariesRequest) returns (ListSummariesRequest.Response) {
    option (google.api.http) = {
    get: "/v1/monitored_entity/listSummaries"
    };
    };

    rpc deleteSummary(DeleteSummaryRequest) returns (DeleteSummaryRequest.Response) {
    option (google.api.http) = {
    delete: "/v1/monitored_entity/deleteSummary"
    body: "*"
    };
    };

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findDataSources(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def createDataSource(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listDataSources(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteDataSource(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getProfiler(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def createProfiler(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateProfiler(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listProfilers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteProfiler(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getProfilerStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findProfilersForMonitoredEntity(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def enableProfiler(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def disableProfiler(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataMonitoringServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getMonitoredEntity': grpc.unary_unary_rpc_method_handler(
          servicer.getMonitoredEntity,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.GetMonitoredEntityRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.GetMonitoredEntityRequest.Response.SerializeToString,
      ),
      'getMonitoredEntityByName': grpc.unary_unary_rpc_method_handler(
          servicer.getMonitoredEntityByName,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.GetMonitoredEntityByNameRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.GetMonitoredEntityByNameRequest.Response.SerializeToString,
      ),
      'createMonitoredEntity': grpc.unary_unary_rpc_method_handler(
          servicer.createMonitoredEntity,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.CreateMonitoredEntityRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.CreateMonitoredEntityRequest.Response.SerializeToString,
      ),
      'updateMonitoredEntity': grpc.unary_unary_rpc_method_handler(
          servicer.updateMonitoredEntity,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.UpdateMonitoredEntityRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.UpdateMonitoredEntityRequest.Response.SerializeToString,
      ),
      'listMonitoredEntities': grpc.unary_unary_rpc_method_handler(
          servicer.listMonitoredEntities,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.ListMonitoredEntitiesRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.ListMonitoredEntitiesRequest.Response.SerializeToString,
      ),
      'deleteMonitoredEntity': grpc.unary_unary_rpc_method_handler(
          servicer.deleteMonitoredEntity,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.DeleteMonitoredEntityRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.DeleteMonitoredEntityRequest.Response.SerializeToString,
      ),
      'getDataSource': grpc.unary_unary_rpc_method_handler(
          servicer.getDataSource,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.GetDataSourceRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.GetDataSourceRequest.Response.SerializeToString,
      ),
      'findDataSources': grpc.unary_unary_rpc_method_handler(
          servicer.findDataSources,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.FindDataSourcesRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.FindDataSourcesRequest.Response.SerializeToString,
      ),
      'createDataSource': grpc.unary_unary_rpc_method_handler(
          servicer.createDataSource,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.CreateDataSourceRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.CreateDataSourceRequest.Response.SerializeToString,
      ),
      'listDataSources': grpc.unary_unary_rpc_method_handler(
          servicer.listDataSources,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.ListDataSourcesRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.ListDataSourcesRequest.Response.SerializeToString,
      ),
      'deleteDataSource': grpc.unary_unary_rpc_method_handler(
          servicer.deleteDataSource,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.DeleteDataSourceRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.DeleteDataSourceRequest.Response.SerializeToString,
      ),
      'getProfiler': grpc.unary_unary_rpc_method_handler(
          servicer.getProfiler,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.GetProfilerRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.GetProfilerRequest.Response.SerializeToString,
      ),
      'createProfiler': grpc.unary_unary_rpc_method_handler(
          servicer.createProfiler,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.CreateProfilerRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.CreateProfilerRequest.Response.SerializeToString,
      ),
      'updateProfiler': grpc.unary_unary_rpc_method_handler(
          servicer.updateProfiler,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.UpdateProfilerRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.UpdateProfilerRequest.Response.SerializeToString,
      ),
      'listProfilers': grpc.unary_unary_rpc_method_handler(
          servicer.listProfilers,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.ListProfilersRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.ListProfilersRequest.Response.SerializeToString,
      ),
      'deleteProfiler': grpc.unary_unary_rpc_method_handler(
          servicer.deleteProfiler,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.DeleteProfilerRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.DeleteProfilerRequest.Response.SerializeToString,
      ),
      'getProfilerStatus': grpc.unary_unary_rpc_method_handler(
          servicer.getProfilerStatus,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.GetProfilerStatusRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.GetProfilerStatusRequest.Response.SerializeToString,
      ),
      'findProfilersForMonitoredEntity': grpc.unary_unary_rpc_method_handler(
          servicer.findProfilersForMonitoredEntity,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.FindProfilersForMonitoredEntityRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.FindProfilersForMonitoredEntityRequest.Response.SerializeToString,
      ),
      'enableProfiler': grpc.unary_unary_rpc_method_handler(
          servicer.enableProfiler,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.EnableProfilerRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.EnableProfilerRequest.Response.SerializeToString,
      ),
      'disableProfiler': grpc.unary_unary_rpc_method_handler(
          servicer.disableProfiler,
          request_deserializer=monitoring_dot_DataMonitoringService__pb2.DisableProfilerRequest.FromString,
          response_serializer=monitoring_dot_DataMonitoringService__pb2.DisableProfilerRequest.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.monitoring.DataMonitoringService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
