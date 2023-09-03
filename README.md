##Instructions

1. Clone repo
2. Start minikube: `minikube start`
3. In new terminal window, start tunnels: `minikube tunnel`
4. Use minikube's internal docker engine: `minikube docker-env | Invoke-Expression`
5. Build frontend docker image: `docker build -t frontend:0.0.1 . -f .\frontend\Dockerfile`
6. Build backend docker image: `docker build -t backend:0.0.1 . -f .\backend\Dockerfile`
7. Apply all yaml files: `minikube kubectl -- apply -f .\{app}\{file_name}.yaml`
8. Add frontend ingress to C:\Windows\System32\drivers\etc\hosts: `127.0.0.1 test-frontend.info`
9. Add backend ingress to C:\Windows\System32\drivers\etc\hosts: `127.0.0.1 test-backend.info`
10. Open test-frontend.info in browser window