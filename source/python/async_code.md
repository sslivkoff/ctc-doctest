
# Asynchronous Code

`ctc` uses `async` functions for network calls and database calls. This allows for high levels of concurrency and makes it easy to dispatch large numbers of complex interdependent queries.

`async` is an intermediate-level python topic with a bit of a learning curve. If you've never used `async` before, you should probably read a tutorial or two before trying to use it in `ctc`. To use `async` functions, they must be run from an event loop. These functions can be called from synchronous code as follows:

```python
import asyncio

result = asyncio.run(some_async_function(input1, input2))
```

__Inside of IPython or Jupyter notebooks, `await` can be used directly, without `asyncio.run()`__. Many of the code examples in these docs assume this is the context and omit `asyncio.run()`.


```python
# no asyncio.run() necessary inside of IPython / Jupyter
result = await some_async_function(input1, input2)
```

If your code opens up network connections, you should also close those connections at the end of your script. For example:

```python
from ctc import rpc

await rpc.async_close_http_session()
```
