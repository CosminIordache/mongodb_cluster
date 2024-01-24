# MongoDB Cluster + Docker Compose
Esto es un repositorio simple para una instalacion de un cluster de mongodb mediante docker compose.

### INSTALACIÓN

Clonar el repositorio
```bash
git clone https://github.com/CosminIordache/mongodb_cluster.git
```

Levantamos los contenedores
```bash
docker compose up -d
```

En el contenedor pricipal en este caso <strong>mongo1</strong> iniciamos la replica set del cluster
```bash
docker exec -it mongo1 mongosh --eval "rs.initiate({
 _id: \"myReplicaSet\",
 members: [
   {_id: 0, host: \"mongo1\"},
   {_id: 1, host: \"mongo2\"},
   {_id: 2, host: \"mongo3\"}
 ]
})"
```

Ahora comprobamos que todo se a configurado correctamente 
```bash
docker exec -it mongo1 mongosh --eval "rs.status()"
```

Y ya tendremos el cluster de mongodb funcionado. Para comprobar que funciona tiraremos el nodo principal.
```bash
docker stop mongo1
```

Comprobaremos que sigue funcionando.
```bash
docker exec -it mongo2 mongosh --eval "rs.status()"
```
