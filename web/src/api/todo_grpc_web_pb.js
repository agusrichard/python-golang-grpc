/**
 * @fileoverview gRPC-Web generated client stub for todo
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = {};
proto.todo = require('./todo_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.todo.TodoServiceClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.todo.TodoServicePromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.todo.CreateTodoRequest,
 *   !proto.todo.CreateTodoResponse>}
 */
const methodDescriptor_TodoService_CreateTodo = new grpc.web.MethodDescriptor(
  '/todo.TodoService/CreateTodo',
  grpc.web.MethodType.UNARY,
  proto.todo.CreateTodoRequest,
  proto.todo.CreateTodoResponse,
  /**
   * @param {!proto.todo.CreateTodoRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.todo.CreateTodoResponse.deserializeBinary
);


/**
 * @param {!proto.todo.CreateTodoRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.todo.CreateTodoResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.todo.CreateTodoResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.todo.TodoServiceClient.prototype.createTodo =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/todo.TodoService/CreateTodo',
      request,
      metadata || {},
      methodDescriptor_TodoService_CreateTodo,
      callback);
};


/**
 * @param {!proto.todo.CreateTodoRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.todo.CreateTodoResponse>}
 *     Promise that resolves to the response
 */
proto.todo.TodoServicePromiseClient.prototype.createTodo =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/todo.TodoService/CreateTodo',
      request,
      metadata || {},
      methodDescriptor_TodoService_CreateTodo);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.todo.GetTodosRequest,
 *   !proto.todo.GetTodosResponse>}
 */
const methodDescriptor_TodoService_GetTodos = new grpc.web.MethodDescriptor(
  '/todo.TodoService/GetTodos',
  grpc.web.MethodType.UNARY,
  proto.todo.GetTodosRequest,
  proto.todo.GetTodosResponse,
  /**
   * @param {!proto.todo.GetTodosRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.todo.GetTodosResponse.deserializeBinary
);


/**
 * @param {!proto.todo.GetTodosRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.todo.GetTodosResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.todo.GetTodosResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.todo.TodoServiceClient.prototype.getTodos =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/todo.TodoService/GetTodos',
      request,
      metadata || {},
      methodDescriptor_TodoService_GetTodos,
      callback);
};


/**
 * @param {!proto.todo.GetTodosRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.todo.GetTodosResponse>}
 *     Promise that resolves to the response
 */
proto.todo.TodoServicePromiseClient.prototype.getTodos =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/todo.TodoService/GetTodos',
      request,
      metadata || {},
      methodDescriptor_TodoService_GetTodos);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.todo.GetTodoRequest,
 *   !proto.todo.GetTodoResponse>}
 */
const methodDescriptor_TodoService_GetTodo = new grpc.web.MethodDescriptor(
  '/todo.TodoService/GetTodo',
  grpc.web.MethodType.UNARY,
  proto.todo.GetTodoRequest,
  proto.todo.GetTodoResponse,
  /**
   * @param {!proto.todo.GetTodoRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.todo.GetTodoResponse.deserializeBinary
);


/**
 * @param {!proto.todo.GetTodoRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.todo.GetTodoResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.todo.GetTodoResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.todo.TodoServiceClient.prototype.getTodo =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/todo.TodoService/GetTodo',
      request,
      metadata || {},
      methodDescriptor_TodoService_GetTodo,
      callback);
};


/**
 * @param {!proto.todo.GetTodoRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.todo.GetTodoResponse>}
 *     Promise that resolves to the response
 */
proto.todo.TodoServicePromiseClient.prototype.getTodo =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/todo.TodoService/GetTodo',
      request,
      metadata || {},
      methodDescriptor_TodoService_GetTodo);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.todo.UpdateTodoRequest,
 *   !proto.todo.UpdateTodoResponse>}
 */
const methodDescriptor_TodoService_UpdateTodo = new grpc.web.MethodDescriptor(
  '/todo.TodoService/UpdateTodo',
  grpc.web.MethodType.UNARY,
  proto.todo.UpdateTodoRequest,
  proto.todo.UpdateTodoResponse,
  /**
   * @param {!proto.todo.UpdateTodoRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.todo.UpdateTodoResponse.deserializeBinary
);


/**
 * @param {!proto.todo.UpdateTodoRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.todo.UpdateTodoResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.todo.UpdateTodoResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.todo.TodoServiceClient.prototype.updateTodo =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/todo.TodoService/UpdateTodo',
      request,
      metadata || {},
      methodDescriptor_TodoService_UpdateTodo,
      callback);
};


/**
 * @param {!proto.todo.UpdateTodoRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.todo.UpdateTodoResponse>}
 *     Promise that resolves to the response
 */
proto.todo.TodoServicePromiseClient.prototype.updateTodo =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/todo.TodoService/UpdateTodo',
      request,
      metadata || {},
      methodDescriptor_TodoService_UpdateTodo);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.todo.DeleteTodoRequest,
 *   !proto.todo.DeleteTodoResponse>}
 */
const methodDescriptor_TodoService_DeleteTodo = new grpc.web.MethodDescriptor(
  '/todo.TodoService/DeleteTodo',
  grpc.web.MethodType.UNARY,
  proto.todo.DeleteTodoRequest,
  proto.todo.DeleteTodoResponse,
  /**
   * @param {!proto.todo.DeleteTodoRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.todo.DeleteTodoResponse.deserializeBinary
);


/**
 * @param {!proto.todo.DeleteTodoRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.todo.DeleteTodoResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.todo.DeleteTodoResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.todo.TodoServiceClient.prototype.deleteTodo =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/todo.TodoService/DeleteTodo',
      request,
      metadata || {},
      methodDescriptor_TodoService_DeleteTodo,
      callback);
};


/**
 * @param {!proto.todo.DeleteTodoRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.todo.DeleteTodoResponse>}
 *     Promise that resolves to the response
 */
proto.todo.TodoServicePromiseClient.prototype.deleteTodo =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/todo.TodoService/DeleteTodo',
      request,
      metadata || {},
      methodDescriptor_TodoService_DeleteTodo);
};


module.exports = proto.todo;

