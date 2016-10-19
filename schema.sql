drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    username text not null,
    password text not null,
    historyviews text 
);

drop table if exists admins;
    create table admins (
    id integer primary key autoincrement,
    admin text not null,
    password text not null
);

drop table if exists info;
    create table info (
    id integer primary key autoincrement,
    companyname text not null,
    views real not null
);


insert into admins values (1,"ian", "12345");
insert into admins values (2,"jake", "12345"); 
insert into admins values (3,"joaquin", "12345");
insert into admins values (4,"justin", "12345");
insert into admins values (5,"naif", "12345");
insert into admins values (6,"hannie", "12345");


