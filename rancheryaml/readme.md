# Instructions to get Local Dev environment set up

## Install dependencies
```
brew install k3d kubectl helm
```

## Create K3D Cluster
- Update mounted volume directory to point to project directory
```
k3d cluster create k3d-rancher --api-port 6550 --servers 1 --agents 3 --port 443:443@loadbalancer --port 81:81@loadbalancer --volume [YOUR_DIRECTORY]:/src@all --wait
```

## Export KubeConfig
```
KUBECONFIG_FILE=~/.kube/k3d-rancher
k3d kubeconfig get k3d-rancher > $KUBECONFIG_FILE
export KUBECONFIG=$KUBECONFIG_FILE
kubectl get nodes
```

## Deploy Rancher: 1
```
helm repo add rancher-latest https://releases.rancher.com/server-charts/latest
kubectl create namespace cattle-system
kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v0.15.0/cert-manager.crds.yaml
kubectl create namespace cert-manager
helm repo add jetstack https://charts.jetstack.io
helm repo update
```

## Deploy Rancher: 2
```
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --version v0.15.0 --wait
kubectl -n cert-manager rollout status deploy/cert-manager
```

## Deploy Rancher: 3
```
helm install rancher rancher-latest/rancher \
  --namespace cattle-system \
  --set hostname=rancher.k3d.localhost --wait
kubectl -n cattle-system rollout status deploy/rancher
```

## Build 

* Change directories into backend folder
```
docker build . -t backend:latest
k3d image import backend:latest -c k3d-rancher
```

## Rancher Initial Set up

### Import bitnami charts
Add below Catalog Through UI:
- https://kubernetes-charts.storage.googleapis.com/

Also add below repo
```
helm repo add bitnami https://charts.bitnami.com/bitnami
```

### Create namespaces
Need to create namespaces with the following names through UI:
- database
- services
- web
- worker
- elasticsearch

### Deploy Services

Redis/RabbitMQ
Use App Catalog in Rancher UI to deploy: 
- Redis to services namespace: Don't use Master/Slave topology. Single instance is fine
- RabbitMQ to services namespace 

Postgres
```
helm install -n database postgres bitnami/postgresql
export POSTGRES_PASSWORD=$(kubectl get secret --namespace database postgres-postgresql -o jsonpath="{.data.postgresql-password}" | base64 --decode)
```

Elasticsearch:
- Elasticsearch Deployment into respective namespace
  - docker exec -it k3d-k3d-rancher-agent-0 /bin/sh
  - chmod -R 777 /elasticsearch
  - May have to do this on rancher-agent-0/1/2 depending on where node mounts

Web/Worker Apps
- Web/Worker Deploy yaml from rancheryaml/local into respective namespaces
  - ImportPostgres Service YAML Web/Worker namespace
  - Update Database password in ENV Variable for Web/Worker
  - Update RabbitMQ password in ENV variable for Web/worker
  - Import RabbitMQ Service YAML Worker namespace
