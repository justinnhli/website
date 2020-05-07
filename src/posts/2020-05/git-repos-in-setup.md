title: Sharing git Repositories between `pip` and `setup.py`
date: 2020-05-06

I recently had to change my [research repository](https://github.com/justinnhli/research) into an `pip`-installable Python package for my students. The first problem I ran into is that I use several unpublished packages, which I link from my `requirements.txt`:

```
# requirements.txt
...
# experiment packages
git+https://github.com/justinnhli/permspace.git
git+https://github.com/justinnhli/clusterun.git
...
```

To get it working in `setup.py`, I had to create dependency links:

```python
setup(
    # ...
    install_requires=[
        # ...
        # experiment packages
        'permspace',
        'clusterun',
        # ...
    ],
    dependency_links=[
        'https://github.com/justinnhli/permspace.git#egg=permspace',
        'https://github.com/justinnhli/clusterun.git#egg=clusterun',
    ],
)
```

The `egg=` component tells setuptools which package it provides. I could [specified more details as well](https://setuptools.readthedocs.io/en/latest/setuptools.html#dependencies-that-aren-t-in-pypi), including a version, but it wasn't necessary here.

The second problem I ran into is that I now have two places to list dependencies, which set off my [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) alarm. It would be ideal if I can make `pip install` read `setup.py`, which is how I learned about the `-e`/`--editable` option. I don't completely understand the rather obtuse documentation - "Install a project in editable mode (i.e. setuptools "develop mode") from a local project path or a VCS url." - but regardless, it doesn't work by itself:

```
$ pip install -e .
Obtaining file:///Users/justinnhli/git/research
ERROR: Could not find a version that satisfies the requirement permspace (from justinnhli-research==0.0.0) (from versions: none)
ERROR: No matching distribution found for permspace (from justinnhli-research==0.0.0)
$
```

It turns out `pip install` doesn't read `dependency_links`, which is why it failed to find the `permspace` package. I finally found the answer buried in a [StackOverflow post](https://stackoverflow.com/questions/12518499/pip-ignores-dependency-links-in-setup-py#comment94736800_13587734): instead of just specifying `permspace` in `setup.py`, it must also specify the git URL:

```python
setup(
    # ...
    install_requires=[
        # ...
        # experiment packages
        'permspace @ git+https://github.com/justinnhli/permspace.git',
        'clusterun @ git+https://github.com/justinnhli/clusterun.git',
        # ...
    ],
    dependency_links=[
        'https://github.com/justinnhli/permspace.git#egg=permspace',
        'https://github.com/justinnhli/clusterun.git#egg=clusterun',
    ],
)
```

This set off another DRY alarm, and my final change is to write a function that reads from a dictionary and returns the correct string:

```python
DEPENDENCIES = {
    'pydictionary': 'https://github.com/justinnhli/PyDictionary.git',
    'permspace': 'https://github.com/justinnhli/permspace.git',
    'clusterun': 'https://github.com/justinnhli/clusterun.git',
}

def get_dependency(package, location):
    if location == 'install':
        return f'{package} @ git+{DEPENDENCIES[package]}'
    elif location == 'link':
        return f'{DEPENDENCIES[package]}#egg={package}'
    else:
        raise ValueError(f'Unknown location: {location}')

setup(
    # ...
    install_requires=[
        # ...
        # experiment packages
        get_dependency('permspace', location='install'),
        get_dependency('clusterun', location='install'),
        # ...
    ],
    dependency_links=[
        get_dependency('permspace', location='link'),
        get_dependency('clusterun', location='link'),
    ],
)
```
