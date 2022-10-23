# Rodando o MYSQL via Docker

```console
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql
```

## Criar banco de dados

```sql
CREATE DATABASE nomebanco
```

## Criar tabela do usuário

```sql
-- dbteste.usuario definition

CREATE TABLE `usuario` (
  `id` int NOT NULL,
  `nome` varchar(100) NOT NULL,
  `senha` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
);
```
