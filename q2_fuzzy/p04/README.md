### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q2_fuzzy/p04
$ git checkout

$ cd ./q2_fuzzy/p04
```

### Install
```shell
$ poetry install --only main
$ poetry shell
```

### Build
```shell
$ python ./src/task1.py
$ python ./src/task2.py
```

### Continuous Integration
```shell
$ poe ci
```