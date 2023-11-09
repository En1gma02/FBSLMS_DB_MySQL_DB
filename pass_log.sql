CREATE DATABASE pass_log;
USE pass_log;

CREATE TABLE main(
   username VARCHAR(30),
   pass VARCHAR(20),
   access VARCHAR(1) DEFAULT '0',
   PRIMARY KEY(username,pass)
);

INSERT INTO main VALUES("Dragon","1234",'1'),("Platypus","1234",'1'),("Shark","1234",'1'),("Oyster","1",'0');

SELECT * FROM main;