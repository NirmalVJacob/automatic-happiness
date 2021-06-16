-- CREATE TABLES --
create table publisher(
  id integer primary key,
  name text ,
  country text);
  
create table books(
  id integer primary key,
  title text ,
  publisher integer references publisher_id);
  
create table subjects(
  id integer primary key,
  name text);

create table books_subjects(
  book integer refernces subjects_id ,
  subject integer references subjects_id);
