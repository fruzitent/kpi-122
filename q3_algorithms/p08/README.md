### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q3_algorithms/p08
$ git checkout

$ cd ./q3_algorithms/p08
```

### Install
```shell
$ cmake --preset unix-gcc-debug
```

### Build
```shell
$ cmake --build --preset unix-gcc-debug
$ ./out/build/unix-gcc-debug/task1
```
