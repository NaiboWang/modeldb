package ai.verta.modeldb.entities.audit_log;

import ai.verta.common.ModelDBResourceEnum.ModelDBServiceResourceTypes;
import ai.verta.modeldb.common.exceptions.ModelDBException;
import ai.verta.modeldb.utils.ModelDBUtils;
import ai.verta.uac.Action;
import ai.verta.uac.ModelDBActionEnum.ModelDBServiceActions;
import ai.verta.uac.ResourceType;
import ai.verta.uac.ServiceEnum.Service;
import ai.verta.uac.versioning.AuditLog;
import ai.verta.uac.versioning.AuditResource;
import ai.verta.uac.versioning.AuditUser;
import com.google.protobuf.InvalidProtocolBufferException;
import com.google.protobuf.Value;
import io.grpc.Status;
import java.util.UUID;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "audit_service_local_audit_log")
public class AuditLogLocalEntity {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Column(name = "local_id")
  private String localId;

  @Column(name = "user_id")
  private String userId;

  @Column(name = "action")
  private Integer action;

  @Column(name = "resource_id")
  private String resourceId;

  @Column(name = "resource_type")
  private Integer resourceType;

  @Column(name = "resource_service")
  private Integer resourceService;

  @Column(name = "ts_nano")
  private Long tsNano;

  @Column(name = "method_name", columnDefinition = "text")
  private String methodName;

  @Column(name = "request", columnDefinition = "text")
  private String request;

  @Column(name = "response", columnDefinition = "text")
  private String response;

  @Column(name = "workspace_id")
  private Long workspaceId;

  private AuditLogLocalEntity() {}

  public AuditLogLocalEntity(
      String serviceName,
      String userId,
      ModelDBServiceActions action,
      String resourceId,
      ModelDBServiceResourceTypes resourceType,
      Service resourceService,
      String methodName,
      String request,
      String response,
      Long workspaceId) {
    tsNano = System.currentTimeMillis() * 1000000;
    localId = String.format("%s_%s", serviceName, UUID.randomUUID());
    this.userId = userId;
    this.action = action.getNumber();
    this.resourceId = resourceId;
    this.resourceType = resourceType.getNumber();
    this.resourceService = resourceService.getNumber();
    this.methodName = methodName;
    this.request = request;
    this.response = response;
    this.workspaceId = workspaceId;
  }

  public AuditLog toProto() {
    final AuditResource.Builder resource =
        AuditResource.newBuilder().setResourceId(resourceId).setWorkspaceId(workspaceId);
    if (resourceType != null) {
      resource.setResourceType(
          ResourceType.newBuilder().setModeldbServiceResourceTypeValue(resourceType).build());
    }
    if (resourceService != null) {
      resource.setResourceServiceValue(resourceService);
    }
    AuditLog.Builder builder =
        AuditLog.newBuilder()
            .setLocalId(localId)
            .setUser(AuditUser.newBuilder().setUserId(userId))
            .setAction(
                Action.newBuilder()
                    .setModeldbServiceAction(ModelDBServiceActions.forNumber(action))
                    .setServiceValue(resourceService)
                    .build())
            .setResource(resource);
    if (tsNano != null) {
      builder.setTsNano(tsNano);
    }
    builder.setMethodName(methodName);

    try {
      Value.Builder requestBuilder = Value.newBuilder();
      ModelDBUtils.getProtoObjectFromString(request, requestBuilder);
      builder.setRequest(requestBuilder.build());
    } catch (InvalidProtocolBufferException e) {
      throw new ModelDBException(e.getMessage(), Status.Code.INTERNAL);
    }

    try {
      Value.Builder responseBuilder = Value.newBuilder();
      ModelDBUtils.getProtoObjectFromString(response, responseBuilder);
      builder.setResponse(responseBuilder.build());
    } catch (InvalidProtocolBufferException e) {
      throw new ModelDBException(e.getMessage(), Status.Code.INTERNAL);
    }

    return builder.build();
  }
}
