### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q2_structures/extra02
$ git checkout

$ cd ./q2_structures/extra02
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
$ python ./src/task8.py
$ python ./src/task9.py
$ python ./src/task10.py
$ python ./src/task11.py
$ python ./src/task12.py
```

### Continuous Integration
```shell
$ poe ci
```
