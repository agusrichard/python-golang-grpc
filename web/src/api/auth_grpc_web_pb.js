/**
 * @fileoverview gRPC-Web generated client stub for auth
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = {};
proto.auth = require('./auth_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.auth.AuthServiceClient =
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
proto.auth.AuthServicePromiseClient =
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
 *   !proto.auth.RegisterRequest,
 *   !proto.auth.RegisterResponse>}
 */
const methodDescriptor_AuthService_Register = new grpc.web.MethodDescriptor(
  '/auth.AuthService/Register',
  grpc.web.MethodType.UNARY,
  proto.auth.RegisterRequest,
  proto.auth.RegisterResponse,
  /**
   * @param {!proto.auth.RegisterRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.auth.RegisterResponse.deserializeBinary
);


/**
 * @param {!proto.auth.RegisterRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.auth.RegisterResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.auth.RegisterResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.auth.AuthServiceClient.prototype.register =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/auth.AuthService/Register',
      request,
      metadata || {},
      methodDescriptor_AuthService_Register,
      callback);
};


/**
 * @param {!proto.auth.RegisterRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.auth.RegisterResponse>}
 *     Promise that resolves to the response
 */
proto.auth.AuthServicePromiseClient.prototype.register =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/auth.AuthService/Register',
      request,
      metadata || {},
      methodDescriptor_AuthService_Register);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.auth.LoginRequest,
 *   !proto.auth.LoginResponse>}
 */
const methodDescriptor_AuthService_Login = new grpc.web.MethodDescriptor(
  '/auth.AuthService/Login',
  grpc.web.MethodType.UNARY,
  proto.auth.LoginRequest,
  proto.auth.LoginResponse,
  /**
   * @param {!proto.auth.LoginRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.auth.LoginResponse.deserializeBinary
);


/**
 * @param {!proto.auth.LoginRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.auth.LoginResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.auth.LoginResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.auth.AuthServiceClient.prototype.login =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/auth.AuthService/Login',
      request,
      metadata || {},
      methodDescriptor_AuthService_Login,
      callback);
};


/**
 * @param {!proto.auth.LoginRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.auth.LoginResponse>}
 *     Promise that resolves to the response
 */
proto.auth.AuthServicePromiseClient.prototype.login =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/auth.AuthService/Login',
      request,
      metadata || {},
      methodDescriptor_AuthService_Login);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.auth.ValidateTokenRequest,
 *   !proto.auth.ValidateTokenResponse>}
 */
const methodDescriptor_AuthService_ValidateToken = new grpc.web.MethodDescriptor(
  '/auth.AuthService/ValidateToken',
  grpc.web.MethodType.UNARY,
  proto.auth.ValidateTokenRequest,
  proto.auth.ValidateTokenResponse,
  /**
   * @param {!proto.auth.ValidateTokenRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.auth.ValidateTokenResponse.deserializeBinary
);


/**
 * @param {!proto.auth.ValidateTokenRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.auth.ValidateTokenResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.auth.ValidateTokenResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.auth.AuthServiceClient.prototype.validateToken =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/auth.AuthService/ValidateToken',
      request,
      metadata || {},
      methodDescriptor_AuthService_ValidateToken,
      callback);
};


/**
 * @param {!proto.auth.ValidateTokenRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.auth.ValidateTokenResponse>}
 *     Promise that resolves to the response
 */
proto.auth.AuthServicePromiseClient.prototype.validateToken =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/auth.AuthService/ValidateToken',
      request,
      metadata || {},
      methodDescriptor_AuthService_ValidateToken);
};


module.exports = proto.auth;

