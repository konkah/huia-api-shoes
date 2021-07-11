# Huia Shoes

autor: Karlos Helton Braga

## Como rodar o projeto

A máquina docker para rodar o projeto está disponível no dockerhub.

```
docker run --name huia -it -p 8000:8000 konkah/huia_shoes
```

Para sair, aperte CTRL+C.

Caso queira fazer o build a partir do dockerfile disponível no repositório, execute:

```
dockerbuild . -f huia.Dockerfile -t konkah/huia_shoes --network=host
```

## Como utilizar a api

### Lote

### Produto

### Cliente

### Pedido

## Decisões de arquitetura

### Usado usuário do django como cadastro do vendedor

Para o vendedor ter login e senha, foi usado o usuário nativo do django admin.

### CPF colocado com 14 dígitos

O Serializador do Rest Framework não deixa a pessoa colocar um CPF com pontos e traços,
mesmo eles sendo removidos antes de ir para o banco de dados, se o CPF não tiver
14 caracteres no banco de dados.

## Bibliotecas externas usadas

### Django Rest Framework (3.12.4)

Usada para facilitar o desenvolvimento da API.

(https://www.django-rest-framework.org/)

### Validate DOC BR (1.8.2)

Usada para validar o CPF do cliente.

(https://pypi.org/project/validate-docbr/)