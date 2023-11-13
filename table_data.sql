USE fbslms;

Insert into team values('Barcelona','Xavi Hernandez'),('Realmadrid','Carlo Ancelotti'),('Mancity','Pep Guardiola'),('PSG','Luis Enrique');
Insert into team values('Liverpool','Jurgen Klopp'),('Chelsea','Mauricio Pochettino'),('Manutd','Erik Ten Hag'),('Arsenal','Mikel Arteta');

Insert into stadium values('Camp Nou','Barcelona','100000','50000'),('Bernabeu','Madrid','75000','40000'),('Etihad Stadium','Manchester','53000','53000'),('Parc des Princes','Paris','50000','35000');
Insert into stadium values('Anfield','London','40000','40000'),('Stamford','North London','20000','10000'),('Old Trafford','Manchester','80000','10000'),('Emirates Stadium','North London','80000','75000');

Insert into sponsors values('Spotify','5 years','i','Barcelona'),('Fly Emirates','3 years','f','Realmadrid'),('Etihad Airways','10 years','i','Mancity'),('Jordans','1 year','i','PSG');
Insert into sponsors values('Standard Chartered','5 years','f','Liverpool'),('Three','2 years','f','Chelsea'),('Team Viewer','3 years','f','Manutd'),('Emirates','6 years','i','Arsenal');

INSERT INTO league_employees VALUES
(1, 'John Doe', 50000),
(2, 'Jane Doe', 60000),
(3, 'Bob Smith', 55000),
(4, 'Alice Johnson', 70000),
(5, 'Charlie Brown', 48000),
(6, 'Diana Miller', 52000),
(7, 'Ethan Davis', 63000),
(8, 'Fiona White', 59000),
(9, 'George Taylor', 51000),
(10, 'Holly Wilson', 67000);

insert into inkind values('Emirates','Jersey,Shorts'),('Etihad Airways','Jersey,Shorts'),('Jordans','Boots'),('Spotify','Jersey');
insert into financial values('Fly Emirates',100000),('Standard Chartered',500000),('Team Viewer',400000),('Three',10000);

INSERT INTO player (p_id, p_name, p_position, p_stats, t_name) VALUES
('B9', 'Robert Lewandowski', 'Forward', 'Goals: 25', 'Barcelona'),
('B22', 'Yamal Khoukhi', 'Midfielder', 'Assists: 15', 'Barcelona'),
('B7', 'Joao Felix', 'Forward', 'Goals: 18', 'Barcelona'),
('B16', 'Gavi', 'Midfielder', 'Passing Accuracy: 88%', 'Barcelona'),
('B21', 'Frenkie de Jong', 'Midfielder', 'Assists: 10', 'Barcelona'),
('B18', 'Pedri Gonzalez', 'Midfielder', 'Goals: 8', 'Barcelona'),
('B29', 'Boubacar Kamara', 'Defender', 'Clean Sheets: 12', 'Barcelona'),
('B4', 'Jules Kounde', 'Defender', 'Tackles: 30', 'Barcelona'),
('B3', 'Ronald Araujo', 'Defender', 'Interceptions: 25', 'Barcelona'),
('B27', 'Joao Cancelo', 'Defender', 'Assists: 5', 'Barcelona'),
('B1', 'Marc-Andre ter Stegen', 'Goalkeeper', 'Clean Sheets: 15', 'Barcelona');

INSERT INTO player (p_id, p_name, p_position, p_stats, t_name) VALUES
('R1', 'Kepa Arrizabalaga', 'Goalkeeper', 'Clean Sheets: 10', 'Realmadrid'),
('R2', 'Dani Carvajal', 'Defender', 'Assists: 8', 'Realmadrid'),
('R3', 'Antonio Rudiger', 'Defender', 'Tackles: 25', 'Realmadrid'),
('R4', 'David Alaba', 'Defender', 'Clean Sheets: 12', 'Realmadrid'),
('R5', 'Eduardo Camavinga', 'Midfielder', 'Passing Accuracy: 85%', 'Realmadrid'),
('R6', 'Aurelien Tchouameni', 'Midfielder', 'Interceptions: 20', 'Realmadrid'),
('R8', 'Federico Valverde', 'Midfielder', 'Goals: 7', 'Realmadrid'),
('R22', 'Jude Bellingham', 'Midfielder', 'Assists: 12', 'Realmadrid'),
('R11', 'Vinicius Jr', 'Forward', 'Goals: 15', 'Realmadrid'),
('R19', 'Rodrigo', 'Forward', 'Assists: 6', 'Realmadrid'),
('R7', 'Joselu', 'Forward', 'Goals: 9', 'Realmadrid');

INSERT INTO player (p_id, p_name, p_position, p_stats, t_name) VALUES
('MC31', 'Ederson Santana de Moraes', 'Goalkeeper', 'Clean Sheets: 18', 'Mancity'),
('MC2', 'Kyle Walker', 'Defender', 'Clean Sheets: 14', 'Mancity'),
('MC6', 'Ruben Dias', 'Defender', 'Tackles: 20', 'Mancity'),
('MC15', 'Manuel Akanji', 'Defender', 'Interceptions: 22', 'Mancity'),
('MC3', 'Nathan Ake', 'Defender', 'Clean Sheets: 10', 'Mancity'),
('MC16', 'Rodrigo Hernandez', 'Midfielder', 'Passing Accuracy: 89%', 'Mancity'),
('MC17', 'Mateo Kovacic', 'Midfielder', 'Assists: 12', 'Mancity'),
('MC8', 'Phil Foden', 'Forward', 'Goals: 12', 'Mancity'),
('MC9', 'Erling Haaland', 'Forward', 'Goals: 20', 'Mancity'),
('MC19', 'Julian Alvarez', 'Forward', 'Assists: 10', 'Mancity'),
('MC20', 'Bernardo Silva', 'Midfielder', 'Assists: 15', 'Mancity');

INSERT INTO player (p_id, p_name, p_position, p_stats, t_name) VALUES
('A1', 'David Raya', 'Goalkeeper', 'Clean Sheets: 14', 'Arsenal'),
('A22', 'Oleksandr Zinchenko', 'Defender', 'Assists: 10', 'Arsenal'),
('A4', 'William Saliba', 'Defender', 'Tackles: 18', 'Arsenal'),
('A6', 'Gabriel Magalhaes', 'Defender', 'Interceptions: 20', 'Arsenal'),
('A15', 'Ben White', 'Defender', 'Clean Sheets: 12', 'Arsenal'),
('A29', 'Kai Havertz', 'Midfielder', 'Goals: 15', 'Arsenal'),
('A10', 'Declan Rice', 'Midfielder', 'Passing Accuracy: 88%', 'Arsenal'),
('A5', 'Jorginho', 'Midfielder', 'Assists: 12', 'Arsenal'),
('A7', 'Bukayo Saka', 'Forward', 'Goals: 10', 'Arsenal'),
('A11', 'Leandro Trossard', 'Forward', 'Assists: 8', 'Arsenal'),
('A35', 'Gabriel Martinelli', 'Forward', 'Goals: 12', 'Arsenal');

INSERT INTO player (p_id, p_name, p_position, p_stats, t_name) VALUES
('P1', 'Gianluigi Donnarumma', 'Goalkeeper', 'Clean Sheets: 20', 'PSG'),
('P23', 'Theo Hernandez', 'Defender', 'Assists: 15', 'PSG'),
('P37', 'Milan Skriniar', 'Defender', 'Tackles: 25', 'PSG'),
('P5', 'Marquinhos', 'Defender', 'Interceptions: 22', 'PSG'),
('P2', 'Achraf Hakimi', 'Defender', 'Assists: 18', 'PSG'),
('P6', 'Marco Verratti', 'Midfielder', 'Passing Accuracy: 90%', 'PSG'),
('P18', 'Carlos Soler', 'Midfielder', 'Assists: 10', 'PSG'),
('P28', 'Vitinha', 'Midfielder', 'Goals: 8', 'PSG'),
('P21', 'Moussa Dembele', 'Forward', 'Goals: 15', 'PSG'),
('P7', 'Kylian Mbappe', 'Forward', 'Goals: 30', 'PSG'),
('P11', 'Randal Kolo Muani', 'Forward', 'Assists: 12', 'PSG');

INSERT INTO player (p_id, p_name, p_position, p_stats, t_name) VALUES
('C1', 'Robert Sanchez', 'Goalkeeper', 'Clean Sheets: 18', 'Chelsea'),
('C44', 'Lewis Colwill', 'Defender', 'Assists: 10', 'Chelsea'),
('C6', 'Thiago Silva', 'Defender', 'Tackles: 20', 'Chelsea'),
('C23', 'Axel Disasi', 'Defender', 'Interceptions: 22', 'Chelsea'),
('C24', 'Reece James', 'Defender', 'Assists: 15', 'Chelsea'),
('C10', 'Moises Caicedo', 'Midfielder', 'Passing Accuracy: 88%', 'Chelsea'),
('C14', 'Agustin Fernandez', 'Midfielder', 'Assists: 8', 'Chelsea'),
('C7', 'Raheem Sterling', 'Forward', 'Goals: 12', 'Chelsea'),
('C17', 'Conor Palmer', 'Midfielder', 'Goals: 10', 'Chelsea'),
('C19', 'Dmitriy Mudryk', 'Forward', 'Goals: 15', 'Chelsea'),
('C11', 'Tino Anjorin', 'Forward', 'Assists: 12', 'Chelsea');

INSERT INTO player (p_id, p_name, p_position, p_stats, t_name) VALUES
('MU1', 'Andre Onana', 'Goalkeeper', 'Clean Sheets: 16', 'Manutd'),
('MU23', 'Luke Shaw', 'Defender', 'Assists: 12', 'Manutd'),
('MU6', 'Lisandro Martinez', 'Defender', 'Tackles: 18', 'Manutd'),
('MU5', 'Harry Maguire', 'Defender', 'Interceptions: 20', 'Manutd'),
('MU20', 'Diogo Dalot', 'Defender', 'Assists: 8', 'Manutd'),
('MU8', 'Christian Eriksen', 'Midfielder', 'Passing Accuracy: 90%', 'Manutd'),
('MU39', 'Scott McTominay', 'Midfielder', 'Goals: 10', 'Manutd'),
('MU40', 'Alejandro Garnacho', 'Forward', 'Goals: 15', 'Manutd'),
('MU18', 'Bruno Fernandes', 'Midfielder', 'Assists: 20', 'Manutd'),
('MU10', 'Marcus Rashford', 'Forward', 'Goals: 18', 'Manutd'),
('MU11', 'Victor Hojlund', 'Forward', 'Assists: 10', 'Manutd');

INSERT INTO player (p_id, p_name, p_position, p_stats, t_name) VALUES
('L1', 'Alisson Becker', 'Goalkeeper', 'Clean Sheets: 18', 'Liverpool'),
('L66', 'Trent Alexander-Arnold', 'Defender', 'Assists: 15', 'Liverpool'),
('L12', 'Joe Gomez', 'Defender', 'Tackles: 20', 'Liverpool'),
('L4', 'Virgil van Dijk', 'Defender', 'Interceptions: 22', 'Liverpool'),
('L5', 'Ibrahima Konate', 'Defender', 'Clean Sheets: 12', 'Liverpool'),
('L13', 'Alisson Becker', 'Midfielder', 'Passing Accuracy: 92%', 'Liverpool'),
('L17', 'Dominik Szoboszlai', 'Midfielder', 'Goals: 12', 'Liverpool'),
('L21', 'Konstantinos Tsimikas', 'Defender', 'Assists: 8', 'Liverpool'),
('L23', 'Luis Diaz', 'Forward', 'Goals: 15', 'Liverpool'),
('L11', 'Mohamed Salah', 'Forward', 'Goals: 30', 'Liverpool'),
('L7', 'Darwin Nunez', 'Forward', 'Assists: 10', 'Liverpool');

-- Assuming you have a table named 'contracts'
INSERT INTO contract (c_id, c_fees, c_duration, p_id) VALUES
('c1', 5000000, '3 years', 'B9'),
('c2', 3000000, '2 years', 'B22'),
('c3', 4000000, '3 years', 'B7'),
('c4', 4500000, '3 years', 'B16'),
('c5', 3500000, '2 years', 'B21'),
('c6', 3200000, '2 years', 'B18'),
('c7', 6000000, '4 years', 'B29'),
('c8', 3800000, '2 years', 'B4'),
('c9', 4200000, '3 years', 'B3'),
('c10', 5500000, '4 years', 'B27'),
('c11', 4800000, '3 years', 'B1');


INSERT INTO contract (c_id, c_fees, c_duration, p_id) VALUES
('c67', 5000000, '3 years', 'R1'),
('c68', 3000000, '2 years', 'R2'),
('c69', 4000000, '3 years', 'R3'),
('c70', 4500000, '3 years', 'R4'),
('c71', 3500000, '2 years', 'R5'),
('c72', 3200000, '2 years', 'R6'),
('c73', 6000000, '4 years', 'R8'),
('c74', 3800000, '2 years', 'R22'),
('c75', 4200000, '3 years', 'R11'),
('c76', 5500000, '4 years', 'R19'),
('c77', 4800000, '3 years', 'R7');

-- Assuming you have a table named 'contracts'
INSERT INTO contract (c_id, c_fees, c_duration, p_id) VALUES
('c12', 5200000, '3 years', 'MC31'),
('c13', 3100000, '2 years', 'MC2'),
('c14', 4200000, '3 years', 'MC6'),
('c15', 4600000, '3 years', 'MC15'),
('c16', 3600000, '2 years', 'MC3'),
('c17', 3300000, '2 years', 'MC16'),
('c18', 6100000, '4 years', 'MC17'),
('c19', 3900000, '2 years', 'MC8'),
('c20', 4300000, '3 years', 'MC9'),
('c21', 5600000, '4 years', 'MC19'),
('c22', 4900000, '3 years', 'MC20');

-- Assuming you have a table named 'contracts'
INSERT INTO contract (c_id, c_fees, c_duration, p_id) VALUES
('c23', 5300000, '3 years', 'A1'),
('c24', 3200000, '2 years', 'A22'),
('c25', 4300000, '3 years', 'A4'),
('c26', 4800000, '3 years', 'A6'),
('c27', 3800000, '2 years', 'A5'),
('c28', 3500000, '2 years', 'A29'),
('c29', 6100000, '4 years', 'A10'),
('c30', 3900000, '2 years', 'A5'),
('c31', 4200000, '3 years', 'A7'),
('c32', 5500000, '4 years', 'A11'),
('c33', 4900000, '3 years', 'A35');

-- Assuming you have a table named 'contracts'
INSERT INTO contract (c_id, c_fees, c_duration, p_id) VALUES
('c34', 5400000, '3 years', 'P1'),
('c35', 3300000, '2 years', 'P23'),
('c36', 4400000, '3 years', 'P37'),
('c37', 4700000, '3 years', 'P5'),
('c38', 3700000, '2 years', 'P2'),
('c39', 3400000, '2 years', 'P6'),
('c40', 6200000, '4 years', 'P18'),
('c41', 4000000, '2 years', 'P28'),
('c42', 4300000, '3 years', 'P21'),
('c43', 5600000, '4 years', 'P7'),
('c44', 5000000, '3 years', 'P11');

-- Assuming you have a table named 'contracts'
INSERT INTO contract (c_id, c_fees, c_duration, p_id) VALUES
('c45', 5500000, '3 years', 'C1'),
('c46', 3300000, '2 years', 'C44'),
('c47', 4400000, '3 years', 'C6'),
('c48', 4700000, '3 years', 'C23'),
('c49', 3700000, '2 years', 'C24'),
('c50', 3400000, '2 years', 'C10'),
('c51', 6200000, '4 years', 'C14'),
('c52', 4000000, '2 years', 'C7'),
('c53', 4300000, '3 years', 'C17'),
('c54', 5600000, '4 years', 'C19'),
('c55', 5000000, '3 years', 'C11');

-- Assuming you have a table named 'contracts'
INSERT INTO contract (c_id, c_fees, c_duration, p_id) VALUES
('c56', 5400000, '3 years', 'MU1'),
('c57', 3200000, '2 years', 'MU23'),
('c58', 4300000, '3 years', 'MU6'),
('c59', 4800000, '3 years', 'MU5'),
('c60', 3800000, '2 years', 'MU20'),
('c61', 3500000, '2 years', 'MU8'),
('c62', 6100000, '4 years', 'MU39'),
('c63', 3900000, '2 years', 'MU40'),
('c64', 4200000, '3 years', 'MU18'),
('c65', 5500000, '4 years', 'MU10'),
('c66', 4900000, '3 years', 'MU11');

-- Assuming you have a table named 'contracts'
INSERT INTO contract (c_id, c_fees, c_duration, p_id) VALUES
('c78', 5500000, '3 years', 'L1'),
('c79', 3300000, '2 years', 'L66'),
('c80', 4400000, '3 years', 'L12'),
('c81', 4700000, '3 years', 'L4'),
('c82', 3700000, '2 years', 'L5'),
('c83', 3400000, '2 years', 'L13'),
('c84', 6200000, '4 years', 'L17'),
('c85', 4000000, '2 years', 'L21'),
('c86', 4300000, '3 years', 'L23'),
('c87', 5600000, '4 years', 'L11'),
('c88', 5000000, '3 years', 'L7');


INSERT INTO matches(m_number, m_result, m_date, m_time, s_name) VALUES
(6, '3-0', '2023-01-01', '12:00:00', 'Camp Nou'),
(38, '5-0', '2023-01-02', '13:30:00', 'Camp Nou'),
(18, '3-2', '2023-01-03', '15:00:00', 'Camp Nou'),
(29, '9-2', '2023-01-04', '16:30:00', 'Camp Nou'),
(41, '3-1', '2023-01-05', '18:00:00', 'Camp Nou'),
(47, '2-0', '2023-01-06', '19:30:00', 'Camp Nou'),
(56, '1-0', '2023-01-07', '21:00:00', 'Camp Nou'),
(2, '0-2', '2023-01-08', '22:30:00', 'Bernabeu'),
(9, '1-3', '2023-02-26', '12:00:00', 'Anfield'),
(15, '1-0', '2023-02-27', '13:30:00', 'Etihad Stadium'),
(22, '2-5', '2023-02-28', '15:00:00', 'Stamford'),
(30, '1-3', '2023-03-01', '16:30:00', 'Parc des Princes'),
(37, '0-5', '2023-03-02', '18:00:00', 'Old Trafford'),
(51, '0-1', '2023-03-03', '19:30:00', 'Emirates Stadium'),
(17, '0-1', '2023-03-04', '21:00:00', 'Bernabeu'),
(25, '3-5', '2023-04-21', '12:00:00', 'Bernabeu'),
(44, '1-0', '2023-04-22', '13:30:00', 'Bernabeu'),
(28, '1-3', '2023-04-23', '15:00:00', 'Bernabeu'),
(34, '0-4', '2023-04-24', '16:30:00', 'Bernabeu'),
(42, '1-2', '2023-04-25', '18:00:00', 'Bernabeu'),
(55, '2-1', '2023-04-26', '19:30:00', 'Anfield'),
(5, '5-0', '2023-04-27', '21:00:00', 'Etihad Stadium'),
(43, '1-0', '2023-06-11', '12:00:00', 'Stamford'),
(21, '2-1', '2023-06-12', '13:30:00', 'Parc des Princes'),
(39, '3-1', '2023-06-13', '15:00:00', 'Old Trafford'),
(49, '3-0', '2023-06-14', '16:30:00', 'Emirates Stadium'),
(7, '5-0', '2023-06-15', '18:00:00', 'Etihad Stadium'),
(20, '3-0', '2023-06-16', '19:30:00', 'Etihad Stadium'),
(26, '1-0', '2023-06-17', '21:00:00', 'Etihad Stadium'),
(33, '4-0', '2023-08-02', '12:00:00', 'Etihad Stadium'),
(48, '1-0', '2023-08-03', '13:30:00', 'Etihad Stadium'),
(1, '1-3', '2023-08-04', '15:00:00', 'Anfield'),
(11, '0-3', '2023-08-05', '16:30:00', 'Stamford'),
(53, '1-2', '2023-08-06', '18:00:00', 'Parc des Princes'),
(35, '1-7', '2023-08-07', '19:30:00', 'Old Trafford'),
(45, '1-0', '2023-08-08', '21:00:00', 'Emirates Stadium'),
(4, '1-3', '2023-10-02', '12:00:00', 'Stamford'),
(13, '2-0', '2023-10-03', '13:30:00', 'Stamford'),
(27, '1-0', '2023-10-04', '15:00:00', 'Stamford'),
(36, '1-3', '2023-10-05', '16:30:00', 'Stamford'),
(10, '3-0', '2023-10-06', '18:00:00', 'Parc des Princes'),
(19, '3-0', '2023-10-07', '19:30:00', 'Anfield'),
(32, '0-1', '2023-10-08', '21:00:00', 'Old Trafford'),
(46, '5-0', '2023-12-02', '12:00:00', 'Emirates Stadium'),
(8, '5-0', '2023-12-03', '13:30:00', 'Emirates Stadium'),
(31, '3-0', '2023-12-04', '15:00:00', 'Emirates Stadium'),
(16, '5-1', '2023-12-05', '16:30:00', 'Emirates Stadium'),
(24, '0-1', '2023-12-06', '18:00:00', 'Parc des Princes'),
(40, '2-3', '2023-12-07', '19:30:00', 'Anfield'),
(52, '2-4', '2023-12-08', '21:00:00', 'Old Trafford'),
(3, '0-4', '2023-12-09', '22:30:00', 'Old Trafford'),
(12, '3-1', '2023-12-10', '23:59:59', 'Old Trafford'),
(23, '1-3', '2023-12-11', '12:00:00', 'Parc des Princes'),
(50, '7-1', '2023-12-12', '13:30:00', 'Anfield'),
(14, '3-1', '2023-12-13', '15:00:00', 'Parc des Princes'),
(54, '1-3', '2023-12-14', '16:30:00', 'Anfield');

Insert into league_standings values(1,14,39,13,1,'Barcelona'),(8,14,3,1,13,'Realmadrid'),(2,14,36,12,2,'Mancity'),(4,14,24,8,6,'PSG');
Insert into league_standings values(5,14,21,7,7,'Liverpool'),(7,14,9,3,11,'Chelsea'),(6,14,12,4,10,'Manutd'),(3,14,30,10,4,'Arsenal');

INSERT INTO managed_by (m_number, e_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 1),
(12, 2),
(13, 3),
(14, 4),
(15, 5),
(16, 6),
(17, 7),
(18, 8),
(19, 9),
(20, 10),
(21, 1),
(22, 2),
(23, 3),
(24, 4),
(25, 5),
(26, 6),
(27, 7),
(28, 8),
(29, 9),
(30, 10),
(31, 1),
(32, 2),
(33, 3),
(34, 4),
(35, 5),
(36, 6),
(37, 7),
(38, 8),
(39, 9),
(40, 10),
(41, 1),
(42, 2),
(43, 3),
(44, 4),
(45, 5),
(46, 6),
(47, 7),
(48, 8),
(49, 9),
(50, 10),
(51, 1),
(52, 2),
(53, 3),
(54, 4),
(55, 5),
(56, 6);

INSERT INTO played_by(t_name, m_number, t_name2, winner) VALUES
('Liverpool',1,'Barcelona','Barcelona'),
('Realmadrid',2,'Barcelona','Barcelona'),
('Manutd',3,'Liverpool','Liverpool'),
('Chelsea',4,'Liverpool','Liverpool'),
('Mancity',5,'Liverpool','Mancity'),
('Barcelona',6,'Realmadrid','Barcelona'),
('Mancity',7,'Realmadrid','Mancity'),
('Arsenal',8,'Liverpool','Arsenal'),
('Barcelona',9,'Liverpool','Barcelona'),
('PSG',10,'Chelsea','PSG'),
('Chelsea',11,'Mancity','Chelsea'),
('Manutd',12,'PSG','Manutd'),
('Chelsea',13,'PSG','Chelsea'),
('PSG',14,'Liverpool','PSG'),
('Mancity',15,'Arsenal','Mancity'),
('Arsenal',16,'Manutd','Arsenal'),
('Realmadrid',17,'Chelsea','Realmadrid'),
('Barcelona',18,'Mancity','Barcelona'),
('Liverpool',19,'Chelsea','Liverpool'),
('Mancity',20,'Chelsea','Mancity'),
('PSG',21,'Manutd','PSG'),
('Chelsea',22,'Barcelona','Chelsea'),
('PSG',23,'Barcelona','Barcelona'),
('PSG',24,'Mancity','Mancity'),
('Realmadrid',25,'Mancity','Mancity'),
('Mancity',26,'Barcelona','Mancity'),
('Chelsea',27,'Manutd','Chelsea'),
('Realmadrid',28,'PSG','Realmadrid'),
('Barcelona',29,'Chelsea','Barcelona'),
('PSG',30,'Realmadrid','PSG'),
('Arsenal',31,'PSG','Arsenal'),
('Manutd',32,'Chelsea','Chelsea'),
('Mancity',33,'Chelsea','Mancity'),
('Realmadrid',34,'Manutd','Manutd'),
('Manutd',35,'PSG','Manutd'),
('Chelsea',36,'Arsenal','Arsenal'),
('Barcelona',37,'Manutd','Barcelona'),
('Barcelona',38,'Liverpool','Barcelona'),
('Manutd',39,'PSG','Manutd'),
('Liverpool',40,'Arsenal','Arsenal'),
('Barcelona',41,'PSG','Barcelona'),
('Realmadrid',42,'Arsenal','Arsenal'),
('Chelsea',43,'Manutd','Chelsea'),
('Realmadrid',44,'Chelsea','Realmadrid'),
('Arsenal',45,'Mancity','Mancity'),
('Arsenal',46,'Realmadrid','Arsenal'),
('Barcelona',47,'Manutd','Barcelona'),
('Mancity',48,'Arsenal','Mancity'),
('Arsenal',49,'Chelsea','Arsenal'),
('Liverpool',50,'Manutd','Liverpool'),
('Arsenal',51,'Barcelona','Arsenal'),
('Manutd',52,'Arsenal','Arsenal'),
('PSG',53,'Mancity','PSG'),
('Liverpool',54,'PSG','Liverpool'),
('Liverpool',55,'Realmadrid','Liverpool'),
('Barcelona',56,'Arsenal','Barcelona');