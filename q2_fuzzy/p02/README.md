### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q2_fuzzy/p02
$ git checkout

$ cd ./q2_fuzzy/p02
```

### Install
```shell
$ poetry install --only main
$ poetry shell
```

### Build
```shell
$ python ./src/task1.py
$ python ./src/task1_hand.py
```

### Continuous Integration
```shell
$ poe ci
```
