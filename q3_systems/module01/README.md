### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi
$ git sparse-checkout set q3_systems/module01
$ git checkout
$ cd ./q3_systems/module01
```

### Docs
```shell
$ cd ./tex
$ lualatex --shell-escape -file-line-error -halt-on-error -output-format=pdf -synctex=1 ./main.tex
```
