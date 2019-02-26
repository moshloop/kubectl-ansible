# kubectl-ansible

A dynamic inventory plugin for ansible that retrieves nodes from kubernetes cluster.

```bash
$ pip install kubectl-ansible
$ kubectl get nodes
NAME        STATUS   ROLES    AGE     VERSION
master01    Ready    master   7d18h   v1.13.2
worker01    Ready    <none>   7d13h   v1.13.2
$ kubectl ansible -m ping all
master01| SUCCESS => {
    "changed": false,
    "ping": "pong"
}
worker01| SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```