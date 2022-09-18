
# Monitoring

## Logging

`ctc` can log outgoing RPC requests and SQL queries. This functionality can be enabled or disabled using `ctc setup`.

Logs are stored in the `ctc` data dir:
- `./logs/rpc_requests.md`
- `./logs/sql_queries.md`

Running `ctc log` in the terminal will start a watching script of the log files. This provides a detailed view of external queries as they happen, which can be useful for debugging and ensuring that external calls are happening as expected.

Logs are written to disk using a non-blocking queue, making it suitable for async applications and imparting minimal impact on performance. These logs are also rotated once they reach a certain size (default = `10MB`). However, being non-blocking also means that the timestamps in the logs lose a bit of temporal precision, and so they do not provide a precise picture of event timing.

Logs are managed by the [Loguru](https://github.com/Delgan/loguru) package. Loguru must be installed for logging to be enabled (`pip install loguru`).


## Other monitoring

Beyond the built-in logging, the best way to monitor `ctc` is through standard 3rd party tools.

Recommended utilities for profiling resource usage:
- **CPU Usage**: [htop](https://htop.dev/), [btop](https://github.com/aristocratos/btop)
- **Storage IO**: [iotop](https://man7.org/linux/man-pages/man8/iotop.8.html), [btop](https://github.com/aristocratos/btop)
- **Storage Capacity**: [du](https://www.man7.org/linux/man-pages/man1/du.1.html), [dust](https://github.com/bootandy/dust), [btop](https://github.com/aristocratos/btop)
- **Network Usage**: [nethogs](https://github.com/raboof/nethogs), [btop](https://github.com/aristocratos/btop)

If your situation calls for a more programmatic monitoring approach, then you probably already know what tools you need.

