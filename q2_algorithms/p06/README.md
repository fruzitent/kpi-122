### Checkout
```shell
$ git clone -n https://github.com/fruzitent/kpi
$ cd ./kpi

$ git sparse-checkout set q2_algorithms/p06
$ git checkout

$ cd ./q2_algorithms/p06
```

### Install
```shell
$ cmake --preset "x64-debug" -S "." -B "./out/build/x64-debug"
```

### Build
```shell
$ cmake --build --preset "x64-debug"
$ ./out/build/x64-debug/task1
$ ./out/build/x64-debug/task2
```