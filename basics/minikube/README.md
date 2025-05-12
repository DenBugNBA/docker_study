Установка [minikube](https://minikube.sigs.k8s.io/docs/start)
Развернуть кластер:
```shell
  minikube start --driver=docker
```
Проверить статус:
```shell
  minikube status
```

Остановить кластер
```shell
  minikube stop
```

Удалить кластер
```shell
  minikube delete
```

Проверить ноды:
```shell
  kubectl get nodes
```

Проверить поды:
```shell
  kubectl get pods
```

Проверить деплойменты:
```shell
  kubectl get deploy
```

Проверить неймспейсы:
```shell
  kubectl get ns
```

Проверить ReplicaSet:
```shell
  kubectl get rs
```

Применить настройки из файла:
```shell
  kubectl apply -f deployment.yaml
```

Удалить под:
```shell
  kubectl delete pods nginx-deployment-f85448466-594gg
```

Откат к предыдущей версии:
```shell
  kubectl rollout undo -f deployment.yaml
```
