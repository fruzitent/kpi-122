### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q2_structures/p01
$ git checkout

$ cd ./q2_structures/p01
```

### Install
```shell
$ poetry install --only main
$ poetry shell
```

### Build
```shell
$ poetry run main
```

### Continuous Integration
```shell
$ poe ci
```
