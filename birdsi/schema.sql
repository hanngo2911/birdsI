drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    username text not null,
    email text not null,
    password text not null,
    admin integer
);


drop table if exists keywords;
    create table keywords (
    id integer primary key autoincrement,
    keyword text not null,
    starttime text not null, 
    userID integer not null 
);

drop table if exists tweets;
 	create table tweets (
	id integer primary key autoincrement,
	name text not null, 
	screenname text not null, 
	tweettext text not null,
	retweet integer not null
);

