### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q3_alternatives/p03
$ git checkout

$ cd ./q3_alternatives/p03
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
