# Use uma imagem base do MySQL
FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=senha_root
ENV MYSQL_DATABASE=nome_do_banco
ENV MYSQL_USER=nome_do_usuario
ENV MYSQL_PASSWORD=senha_do_usuario

EXPOSE 3306

CMD ["mysqld"]
