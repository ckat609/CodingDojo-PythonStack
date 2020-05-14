INSERT INTO Wizard (name, house, pet, year) VALUES ('Harry Potter', 'Gryffindor', 'Hedwig', '5');

INSERT INTO Wizard (name, house, pet, year) VALUES ('Hermione Granger', 'Gryffindor', 'Crookshanks', '5');

SELECT * FROM Wizard WHERE id = 1;

SELECT * FROM Wizard WHERE house = 'Gryffindor';

UPDATE Wizard SET year = '6' WHERE id = 1;

INSERT INTO Wizard (name, house, pet, year) VALUES ("Luna Lovegood", "Ravenclaw", "None", "4");

INSERT INTO Wizard (name, house, pet, year) VALUES ("Padma Patil", "Ravenclaw", "None", "5");

UPDATE Wizard SET year = "5" WHERE id = "3";

SELECT * FROM wizard WHERE house='Ravenclaw';