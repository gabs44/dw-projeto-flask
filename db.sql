Create table carros(
	id serial,
	marca varchar(30),
	modelo varchar(30),
	cor varchar(30),
	combustivel varchar(30),
	ano varchar(4),
	primary key (id)
);

Create table usuarios(
	username varchar(40),
	senha varchar(30),
	primary key(username)
);


insert into usuarios values('admin', '12345');