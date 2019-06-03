create table user(
    id integer unsigned primary key auto_increment,
    name varchar(20),
    password varchar(20),
    birthday date
);

insert into user(name, password, birthday)
values ('Jon Snow', '123456', '1993-1-1');
