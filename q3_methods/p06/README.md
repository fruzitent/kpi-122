### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q3_methods/p06
$ git checkout

$ cd ./q3_methods/p06
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

### Docs
```shell
$ latexmk -pdflua -file-line-error -halt-on-error -shell-escape -outdir=../out -cd tex/main.tex
```

### Continuous Integration
```shell
$ poe ci
```
