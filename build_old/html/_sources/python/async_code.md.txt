
# Asynchronous Code

`ctc` uses `async` functions for network calls and database calls. This allows for high levels of concurrency and makes it easy to dispatch large numbers of complex interdependent queries.

`async` is an intermediate-level python topic with a bit of a learning curve. If you've never used `async` before, you should probably read a tutorial or two before trying to use it in `ctc`.

To use `async` functions, they must be run from an event loop. These functions can be called from synchronous code as follows:

```python
import asyncio

result = asyncio.run(some_async_function(input1, input2))
```

If you are using IPython or Jupyter notebooks, you can directly `await` the `async` functions inside code cells without using `asyncio.run()`:


```python
result = await some_async_function(input1, input2)
```

If your code opens up network connections, you should also close those connections at the end of your scipt. For example:

```python
from ctc import rpc

await rpc.async_close_http_session(provider=provider)
```
