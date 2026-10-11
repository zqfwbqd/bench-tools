# bench-tools

A small harness for timing functions with warmup and repeat runs.

## Why

The existing libraries were either abandoned or pulled in a large dependency tree.

## Install

```bash
pip install bench-tools
```

## Usage

```python
from bench_tools import benchTools

result = benchTools("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
