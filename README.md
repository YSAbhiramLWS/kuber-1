Establishment of connection between 2 clients and 1 server within the same Kubernetes cluster(environment) and same node. 

Architecture:-
<img width="294" height="374" alt="image" src="https://github.com/user-attachments/assets/0bd7ac98-9e84-4b71-8d6c-9fc2d9755229" />


1) A server is developed and tested.
2) Server -> Docker image(with the help of Dockerfile)
3) Docker image -> Docker container
4) Docker container -> Kuberenetes pod.
5) Created a server service to route the client request traffic to a properly working server.
6) Developed a clinet and converted it into a Docker image.
7) Client-1 docker image is copied to create client-2 docker image.
8) Created client pod for image-1,2.
9) Verified connection among them.

Commands used:

docker ps

docker build -t smo-server . (build server image)

docker images 

docker run -p 8080:8080 smo-server (image to container)

curl.exe http://localhost:8080 (testing the server)

docker stop <container-id>

kubectl get nodes (check kubernetes nodes)

kubectl apply -f server-pod.yaml (apply pods)

kubectl get pods (check pods)

kubectl get pod -o wide (check pods in detail)

kubectl apply -f server-service.yaml (apply service)

kubectl get service (check service)

kubectl get endpoints server-service (check endpoints of service)

docker build -t smo-client . (build client image)

kubectl logs client1-pod (verify client 1 communication)

kubectl logs smo-server-pod (check communication from server side)
