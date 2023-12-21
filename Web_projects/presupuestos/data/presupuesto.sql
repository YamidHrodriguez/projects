ALTER USER 'root'@'localhost' IDENTIFIED BY 'nidian56';
CREATE DATABASE presupuesto;
USE presupuesto;

CREATE TABLE Income (
Id_income INT AUTO_INCREMENT PRIMARY KEY,
Description_income VARCHAR(50),
Amount_income INT,
Date_income DATE,
Total_income INT
);
DROP TABLE Income;

CREATE TABLE Egress (
Id_egress INT PRIMARY KEY,
Description_egress VARCHAR(50),
Amount_egress INT,
Date_egress DATE,
Total_egress INT
);
DROP TABLE Egress;

CREATE TABLE Debt (
Id_debt INT PRIMARY KEY,
Description_debt VARCHAR(50),
Amount_debt INT,
Date_debt DATE,
Total_debt INT,
Check_debt BOOLEAN
);
DROP TABLE Debt;

CREATE TABLE Buy (
Id_buy INT PRIMARY KEY,
Description_buy VARCHAR(50),
Amount_buy INT,
Date_buy DATE,
Total_buy INT,
Check_buy BOOLEAN
);
DROP TABLE Buy;

CREATE TABLE Inform (
Id_inform INT PRIMARY KEY,
Date_inform DATE,
Total_inform INT,
Id_income INT,
Id_egress INT,
Id_debt INT,
Id_buy INT,
FOREIGN KEY (Id_income) REFERENCES Income(Id_income),
FOREIGN KEY (Id_egress) REFERENCES Egress(Id_egress),
FOREIGN KEY (Id_debt) REFERENCES Debt(Id_debt),
FOREIGN KEY (Id_buy) REFERENCES Buy(Id_buy)
);
DROP TABLE Inform;

SELECT * FROM Income;
SELECT * FROM Egress;
SELECT * FROM Debt;
SELECT * FROM Buy;
SELECT * FROM Inform;

FLUSH PRIVILEGES;
