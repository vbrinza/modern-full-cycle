# The Modern Full Life Cycle of a web application
# Scope
Document the needed technical stack, steps and the code to provision a full life cycle for a web application to satisfy the modern requirements.

Technical stack:
1. Kubernetes (the last version installed by minikube)
2. Helm v3.5.4 or higher
3. Nginx Ingress Controller
4. Prometheus

## Install a Kubernetes cluster on the local machine
To install a Kubernetes cluster on a MacOS machine perform the following steps:
```bash
% curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64
% sudo install minikube-darwin-amd64 /usr/local/bin/minikube
% minikube start
```
## Deploy the application
OWASP Juicebox web application will be used as an example 
Helm package URL: https://artifacthub.io/packages/helm/securecodebox/juice-shop
To install the app into the Kubernetes cluster perfom the following steps:
```bash
ns='demo-web-app'
kubectl create ns $ns
helm repo add securecodebox https://charts.securecodebox.io/
helm --namespace $ns install my-juice-shop securecodebox/juice-shop --version 2.9.1 --set replicaCount=3
sleep 3
kubectl --namespace $ns port-forward service/my-juice-shop 3000:3000
open http://127.0.0.1:3000
```
