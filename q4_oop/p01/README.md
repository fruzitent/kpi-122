### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q4_oop/p01
$ git checkout

$ cd ./q4_oop/p01
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
