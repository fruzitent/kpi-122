### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q2_structures/p07
$ git checkout

$ cd ./q2_structures/p07
```

### Install
```shell
$ poetry install --only main
$ poetry shell
```

### Build
```shell
$ python ./src/task1.py
```

### Continuous Integration
```shell
$ poe ci
```
