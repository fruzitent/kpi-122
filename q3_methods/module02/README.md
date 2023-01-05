### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q3_methods/module02
$ git checkout

$ cd ./q3_methods/module02
```

### Docs
```shell
$ latexmk -pdflua -file-line-error -halt-on-error -shell-escape -outdir=../out -cd tex/main.tex
```
