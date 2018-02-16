# CGFace

## Background

## Documentation

### Installation

You can install `cgface` from source:

```bash
$ git clone https://github.com/Clinical-Genomics/cgface && cd cgface
$ pip install --editable .
```

You also need a YAML config file describing how to connect to the CG instance. It should contain information like this:

```yaml
---
host: https://clinical.api.com
```

### Getting information

You can quickly get information about samples. For a single sample:

```bash
$ cgface apptag WGSPCF030
$ cgface apptag WGSPCF030 target_reads
```

### Using the API

You can also use the API:

```python
from cgface.api import CgFace

def get_apptag(url, tag_name, key):
    cgface_obj = CgFace(url=url)

    print(cgface_obj.apptag(tag_name=tag_name, key=key))
```
