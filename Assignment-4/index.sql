
CREATE TABLE employees (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(256),
    age INT,
    skill JSON
);

INSERT INTO employees (name, age, skill)
SELECT
  'Name ' || g AS name,
  (floor(random()*50) + 18)::int AS age,                           -- ages 18..67
  json_build_object(
    'primary', (ARRAY['Python','Java','SQL','Go','JavaScript','C++'])[(floor(random()*6)+1)],
    'experience_years', (floor(random()*11))::int,                 -- 0..10 years
    'certs', (CASE WHEN random() < 0.3 THEN ARRAY['AWS','GCP','Azure'] ELSE ARRAY[]::text[] END)
  ) AS skill
FROM generate_series(1,1000) g;

SELECT *
FROM employees
ORDER BY age, skill::text;