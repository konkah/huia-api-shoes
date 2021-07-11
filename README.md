# Huia Shoes

autor: Karlos Helton Braga

## Como rodar o projeto

<!-- Montar o docker com superuser admin/admin e colocar as instruções aqui -->

## Como utilizar a api

### Lote

### Produto

### Cliente

### Pedido

## Decisões de arquitetura

### Usado usuário do django como cadastro do vendedor

Para que o vendedor tenha login e senha, foi usado o usuário nativo do django admin.

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