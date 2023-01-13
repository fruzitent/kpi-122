### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q3_methods/p04
$ git checkout

$ cd ./q3_methods/p04
```

### Install
```shell
$ poetry install
$ poetry shell
```

### Build
```shell
$ python ./src/task1.py
$ python ./src/task2.py
$ python ./src/task3.py
```

### Docs
```shell
$ latexmk -pdflua -file-line-error -halt-on-error -shell-escape -outdir=../out -cd tex/main.tex
```

### Continuous Integration
```shell
$ poe ci
```
