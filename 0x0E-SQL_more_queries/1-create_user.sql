-- create the user privilage
CREATE USER IF NOT EXITS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;;
