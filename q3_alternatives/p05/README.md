### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q3_alternatives/p05
$ git checkout

$ cd ./q3_alternatives/p05
```

### Docs
```shell
$ latexmk -pdflua -file-line-error -halt-on-error -shell-escape -outdir=../out -cd tex/main.tex
```
