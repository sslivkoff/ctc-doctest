
# RPC Client

`ctc.rpc` is a low-level asynchronous RPC client that implements the [EVM JSON-RPC standard](https://eth.wiki/json-rpc/API). This standard consists of many methods such as `eth_call` and `eth_getCode` that query current and historical states of an EVM chain.

## Implementation of Methods

For every method specified by the EVM JSON-RPC standard, `ctc.rpc` implements five python functions:

1. **constructor function**: create method requests
2. **digestor function**: process method responses
3. **executor function**: perform construction, , and digestion all in one step
4. **batch construct**: create method requests in bulk
5. **batch execute**: execute method requests in bulk

(there are no batch digestor functions because they compose naturally from the scalar digestor functions)

## RPC Providers


Unless otherwise specified, requests will be sent to the default RPC provider in `ctc`'s config. Functions in `ctc.rpc` that send RPC requests also take an optional `provider` argument that can be used to specify other RPC providers.

For more details, see the RPC Provider section on the [Data Sources] page.

## Typical RPC Request Lifecycle in `ctc`
1. a constructor function encodes request metadata and parameters into a `RpcRequest` `dict`
2. the request is dispatched to an rpc provider using `rpc.async_send_http()`
3. the client `await`s until the rpc provider returns a response
4. a digestor function decodes the response

For requests that execute contract code (like `eth_call`) or retrieve events (like `getLogs`), `ctc` will encode/decode inputs/outputs using the relevant function abi's and event abi's.

