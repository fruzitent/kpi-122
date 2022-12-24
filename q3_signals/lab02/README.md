### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q3_signals/lab02
$ git checkout

$ cd ./q3_signals/lab02
```

### Install
```shell
$ poetry install --with jupyter
$ poetry shell
```

### Build
```shell
$ poe lab
```

### Continuous Integration
```shell
$ poe ci
```
