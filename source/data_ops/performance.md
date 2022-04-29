
# Performance

The performance of `ctc` can be optimized in a number of ways.

```{admonition} TLDR
Even in suboptimal conditions, `ctc` uses lots of optimizations that allow running many types of workloads at acceptable levels of performance. This page is for those who wish to squeeze additional performance out of `ctc`.
```

## Optimizing Performance

### RPC Provider

Different 3rd party RPC providers can vary significantly in their reliability and speed. For example, some providers have trouble with large historical queries.

Operations in `ctc` that fetch external data are usually bottlenecked by the RPC provider, specifically the latency to the RPC provider. This latency can be reduced by running ctc as closely as possible to the archive node:
- Fastest = running ctc on the same server that is running the archive node
- Fast = running ctc on the same local network as the archive node
- Slower = running ctc in the same geographic region as the archive node
- Slowest = running ctc in a different geographic region than the archive node

If using a 3rd party RPC provider, you should inquire about where their nodes are located and plan accordingly.

`ctc`'s default configuration assumes that the user is querying an rpc node on a remote network. This leads `ctc` to locally store lots of the data that it retrieves. However, it's possible that in heavily optimized setups (such as running `ctc` on the same server as an archive node) that a different set of tradeoffs would be prefered compared to the default. Cache settings are altered using `ctc setup` on the command line.

### Python Versions

More recent versions of python are generally faster. Upgrading to the latest python version is one of the easiest ways to improve code performance. In particular, the upcoming python 3.11 has much faster startup times and it shows improvement across many benchmarks. This makes `ctc`'s cli commands feel especially quick and responsive.

### Python Packages

By default, `ctc` tries to minimize its dependencies and minimize the number of build steps that happen during installation. This does carry a bit of performance cost. Faster versions of various packages can be installed using:

```bash
pip install checkthechain[performance]
```

If `ctc` detects that these performance packages are installed, it will use those instead of the default packages. This can produce a modest performance increase for some workloads.

### Data Storage

`ctc`'s default data directory is `~/.config/ctc/` in the user's home directory. If this directory is on a slow drive (especially a network drive), this will negatively impact performance. To optimize performance, place the data directory on as fast a drive as possible. This can be done by running the setup wizard `ctc setup`.

### Data Caching

For tasks that require many RPC requests, or require lots of post-processing (or are demanding in other ways), you should consider caching the result in-memory or on-disk. One way to do this is with the [toolcache](https://github.com/sslivkoff/toolcache) package. With `toolcache` a simple decorator adds an in-memory or on-disk cache to the expensive function.

For example, if you are using `ctc` to create data payloads for a historical analytics dashboard, you might use a pattern similar to this:

```python
import toolcache


async def create_data_payload(timestamps):
    return [
        compute_timestamp_stats(timestamp=timestamp)
        for timestamp in timestamps
    ]


@toolcache.cache('disk')
async def compute_timestamp_stats(timestamp):
    super_expensive_operation()
```

### Logging

Logging of RPC requests and SQL queries takes up a non-zero amount time. If you don't need logging, disabling it can squeeze out a bit of extra performance. This can be done by running the setup wizard `ctc setup`.

## Benchmarking Performance

To truly optimize your environment and implementation, you will need to run your own benchmarks.

### Benchmarking Speed

The simplest way to benchmark the speed of a CLI command is `time`. Running `time <command>` will run a given command and report the run time. 
Benchmarking speed of python code snippets is slightly more complicated but also has many tools available: 
1. Synchronous code can be easily profiled used IPython's built-in magics `%timeit`, `%%timeit`, `%prun`, and `%%prun`
2. If using a Jupyter notebook, the [Execute Time](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/execute_time/readme.html) extension can be extremely useful for getting a crude estimate of how long each code cell takes to run. This works for both synchronous and asynchronous code.
3. For a more programmatic approach you can use [python's built-in profilers](https://docs.python.org/3/library/profile.html) or 3rd party profilers such as [Scalene](https://github.com/plasma-umass/scalene) or [pyflame](https://github.com/uber-archive/pyflame).

### Measuring Storage Usage

It is also valuable to measure `ctc`'s storage usage to check whether it falls into an acceptable range for a given hardware setup. Storage usage in the `ctc` data folder can be found by running a storage profiling command like `du -h` or `dust`. Storage usage in databases can be found by running `ctc db storage`.

