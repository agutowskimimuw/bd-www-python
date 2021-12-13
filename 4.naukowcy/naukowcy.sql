--
-- Filip Murlak, http://www.mimuw.edu.pl/~fmurlak/bdlab/
-- 
-- Klasowka z SQLa 2012/2013
-- 
-- Baza danych naukowcow: schemat i przykladowe dane
--
-- Wersja dla bazy Postgres

CREATE TABLE naukowiec (
  id INTEGER PRIMARY KEY,
  imie VARCHAR(10) NOT NULL,
  nazwisko VARCHAR(13) NOT NULL,
  promotor INTEGER REFERENCES naukowiec,
  publikacje INTEGER NOT NULL
);

INSERT INTO naukowiec VALUES (1, 'Kazimierz', 'Kuratowski', NULL, 23);
INSERT INTO naukowiec VALUES (2, 'Andrzej', 'Mostowski', 1, 4);
INSERT INTO naukowiec VALUES (3, 'Stanislaw', 'Ulam', 1, 20);
INSERT INTO naukowiec VALUES (4, 'Zofia', 'Adamowicz', 2, 19);
INSERT INTO naukowiec VALUES (5, 'Krzysztof', 'Apt', 2, 32);
INSERT INTO naukowiec VALUES (6, 'Wojciech', 'Guzicki', 2, 18);
INSERT INTO naukowiec VALUES (7, 'Janusz', 'Onyszkiewicz', 2, 0);
INSERT INTO naukowiec VALUES (8, 'Helena', 'Rasiowa', 2, 25);
INSERT INTO naukowiec VALUES (9, 'Piotr', 'Zakrzewski', 6, 16);
INSERT INTO naukowiec VALUES (10, 'Jerzy', 'Tiuryn', 8, 20);
INSERT INTO naukowiec VALUES (11, 'Damian', 'Niwinski', 8, 12);
