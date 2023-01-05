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
```

### Docs
```shell
$ latexmk -pdflua -file-line-error -halt-on-error -shell-escape -outdir=../out -cd tex/main.tex
```

### Continuous Integration
```shell
$ poe ci
```
