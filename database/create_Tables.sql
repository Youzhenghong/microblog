drop table if exists user;
create table user(
	id integer primary key autoincrement,
	username string unique not null,
	password string not null
);

drop table if exists posts;
create table posts(
	id integer primary key autoincrement,
	datetime string not null,
	title string not null,
	visNum integer,
	contents text not null
);

drop table if exists comments;
create table comments(
	id integer primary key autoincrement,
	contents text not null,
	datetime string not null,
	username string unique not null,
	title string not null,
	foreign key(username) references user(username),
	foreign key(title) references posts(title)
);

