
# Binary Data

```{note}
By default `ctc` will perform end-to-end encoding/decoding of many operations. The low-level functions listed here are only needed if you need to work directly with raw binary data.
```

## Examples

```{admonition} Note
These examples are crafted as a [Jupyter notebook](https://jupyter.org/). You can download the original notebook file [here](https://github.com/sslivkoff/ctc-doctest/blob/main/source/python/notebooks/datatypes/binary_data.ipynb).
</br>
</br>
Also note that inside Jupyter notebooks, `await` can be used freely outside of `asyncio.run()`.
```

```{eval-rst}
.. raw:: html
   :file: ../notebooks_html/datatypes/binary_data.html
```

## Reference
[none]
> ```{eval-rst}

> .. autofunction:: ctc.binary.convert
> .. autofunction:: ctc.binary.decode_call_data
> .. autofunction:: ctc.binary.decode_function_output
> .. autofunction:: ctc.binary.decode_types
> .. autofunction:: ctc.binary.encode_call_data
> .. autofunction:: ctc.binary.encode_types
> .. autofunction:: ctc.binary.keccak
> .. autofunction:: ctc.binary.keccak_text
> ```

