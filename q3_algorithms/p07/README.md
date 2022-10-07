### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q3_algorithms/p07
$ git checkout

$ cd ./q3_algorithms/p07
```

### Install
```shell
$ cmake --preset "x64-debug" -S "." -B "./out/build/x64-debug"
```

### Build
```shell
$ cmake --build --preset "x64-debug"
$ ./out/build/x64-debug/task1
```
