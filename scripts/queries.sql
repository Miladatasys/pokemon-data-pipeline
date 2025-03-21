SELECT * FROM pokemon;


SELECT * FROM pokemon WHERE ARRAY_CONTAINS(abilities, 'blaze');

SELECT name, attack, FROM pokemon ORDER BY attack DESC;


SELECT
    AVG(hp) AS avg_hp,
    AVG(attack) as avg_attack,
FROM pokemon;

SELECT * FROM pokemon WHERE LIST_CONTAINS(types, 'fire');

DESCRIBE pokemon