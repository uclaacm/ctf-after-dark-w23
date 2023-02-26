CREATE DATABASE IF NOT EXISTS bankdb;
USE bankdb;

CREATE TABLE IF NOT EXISTS users (
  id INT(11) NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO users (username, password) VALUES
  ('admin', 'not_the_flag{}'),
  ('alice', 'password123'),
  ('bob', 'qwerty123'),
  ('urmom', 'changed_my_mind this isnt the one either. flag{}');

CREATE TABLE IF NOT EXISTS flags (
  flag VARCHAR(255) NOT NULL,
  value VARCHAR(255) NOT NULL,
  PRIMARY KEY (flag)
);

INSERT INTO flags (flag, value) VALUES
  ('USA', 'gets the patriotism flowing'),
  ('Mexico', 'too similar to italy'),
  ('Canada', 'stole too many colors from the US'),
  ('China', 'the spirit of Mao lives on in the non-GMO milk'),
  ('Chall has nothing to do with slim shady', 'flag{3min3m_kind@_wa$hed}');
