CREATE DATABASE fbslms;
USE fbslms;
SELECT * FROM played_by;
CREATE TABLE contract(
   c_id varchar(10) PRIMARY KEY,
   c_fees VARCHAR(50),
   c_duration VARCHAR(20)
);
ALTER TABLE contract MODIFY COLUMN c_fees INT;

CREATE TABLE player(
   p_id varchar(10) PRIMARY KEY,
   p_name VARCHAR(50) NOT NULL,
   p_position VARCHAR(30),
   p_stats VARCHAR(100)
);
ALTER TABLE contract ADD p_id varchar(10), ADD FOREIGN KEY(p_id) REFERENCES player(p_id) ON DELETE CASCADE;

CREATE TABLE sponsors(
   sp_name VARCHAR(50) PRIMARY KEY,
   sp_duration VARCHAR(50),
   sp_type CHAR(1),
   CHECK (sp_type = "i" OR sp_type = "f")
);

CREATE TABLE inKind(
   sp_name VARCHAR(50), 
   goodsServices VARCHAR(100),
   PRIMARY KEY(sp_name,goodsServices),
   FOREIGN KEY(sp_name) REFERENCES sponsors(sp_name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE financial(
   sp_name VARCHAR(50) ,
   amount VARCHAR(100),
   PRIMARY KEY(sp_name,amount),
   FOREIGN KEY(sp_name) REFERENCES sponsors(sp_name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE team(
   t_name VARCHAR(30) PRIMARY KEY,
   t_coach VARCHAR(30) DEFAULT "unassigned"
);
ALTER TABLE player ADD t_name VARCHAR(30), ADD FOREIGN KEY(t_name) REFERENCES team(t_name) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE sponsors ADD t_name VARCHAR(30), ADD FOREIGN KEY(t_name) REFERENCES team(t_name) ON DELETE SET NULL ON UPDATE CASCADE;

CREATE TABLE stadium(
   s_name VARCHAR(30) PRIMARY KEY,
   s_location VARCHAR(40),
   s_capacity INT,
   s_cost INT
);
ALTER TABLE stadium MODIFY COLUMN s_name VARCHAR(50);

CREATE TABLE matches(
   m_number INT PRIMARY KEY,
   m_result VARCHAR(10),
   m_time VARCHAR(10),
   m_date DATE,
   s_name VARCHAR(30),
   FOREIGN KEY(s_name) REFERENCES stadium(s_name) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE played_by(
   t_name VARCHAR(30),
   FOREIGN KEY(t_name) REFERENCES team(t_name) ON DELETE SET NULL ON UPDATE CASCADE,
   m_number INT,
   FOREIGN KEY(m_number) REFERENCES matches(m_number) ON DELETE CASCADE,
   t_name2 VARCHAR(30),
   FOREIGN KEY(t_name2) REFERENCES team(t_name) ON DELETE SET NULL ON UPDATE CASCADE,
   winner VARCHAR(30),
   FOREIGN KEY(winner) REFERENCES team(t_name) ON DELETE SET NULL ON UPDATE CASCADE,
   PRIMARY KEY(m_number)
);

CREATE TABLE league_standin(
   e_id INT PRIMARY KEY,
   e_name VARCHAR(30),
   e_salary INT DEFAULT "50000"
);
RENAME TABLE league_standin TO league_employees;

CREATE TABLE managed_by(
   m_number INT,
   FOREIGN KEY(m_number) REFERENCES matches(m_number) ON DELETE CASCADE,
   e_id INT,
   FOREIGN KEY(e_id) REFERENCES league_employees(e_id),
   PRIMARY KEY(m_number,e_id)
);

CREATE TABLE league_standings(
   ls_rank INT UNIQUE,
   ls_matches INT,
   ls_points INT,
   ls_wins INT,
   ls_loss INT,
   t_name VARCHAR(30),
   FOREIGN KEY(t_name) REFERENCES team(t_name) ON DELETE SET NULL ON UPDATE CASCADE
);
