### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q2_structures/extra01
$ git checkout

$ cd ./q2_structures/extra01
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
$ python ./src/task3.py
$ python ./src/task4.py
$ python ./src/task5.py
$ python ./src/task6.py
$ python ./src/task7.py
```

### Continuous Integration
```shell
$ poe ci
```
