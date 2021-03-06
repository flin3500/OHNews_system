CREATE TABLE news(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	title VARCHAR(40) NOT NULL,
	editor_id INT UNSIGNED NOT NULL,
	type_id INT UNSIGNED NOT NULL,
	cotent_id CHAR(12) NOT NULL,
	if_top TINYINT UNSIGNED NOT NULL,
	create_time TIMESTAMP NOT NULL DEFAULT(CURRENT_TIMESTAMP),
	update_time TIMESTAMP NOT NULL DEFAULT(CURRENT_TIMESTAMP),
	status ENUM("Draft", "Reviewing", "Hide", "POST") NOT NULL,
	INDEX(editor_id),
	INDEX(type_id),
	INDEX(status),
	INDEX(create_time),
	INDEX(if_top)
);
