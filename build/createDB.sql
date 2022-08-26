
CREATE TABLE IF NOT EXISTS stats (
    id INT PRIMARY KEY,
    date date NOT NULL,
    course VARCHAR ( 50 ) NOT NULL,
    score INT NOT NULL,
    fairways INT NOT NULL,
    gir INT NOT NULL,
    threep INT NOT NULL
);
