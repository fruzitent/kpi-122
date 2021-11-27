### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q1_bases/module01
$ git checkout

$ cd ./q1_bases/module01
```

### Install
```shell
$ poetry install --only main
$ poetry shell
```

### Build
```shell
$ poetry run dev
```

### Continuous Integration
```shell
$ poe ci
```
