# 3-file-repo
3-file-repo is a python package for saving files in a tree-folder-structure way

## Installation

```
pip install tree-file-repo
```

## Getting Started

These instructions will get you a recipe to use 3-file-repo

## Mock your repo

If you want to mock your repo and test the file save process you can use get_mock_path

```
from filerepo.repomanager import RepoManager
...
rm = RepoManager("ROOT_PATH")
rm.get_mock_path("..path")
#it will return ..path/files

```


