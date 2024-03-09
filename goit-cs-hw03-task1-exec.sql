;SELECT * FROM users WHERE id = (SELECT MIN(id) FROM users)
;SELECT * FROM tasks INNER JOIN status ON tasks.status_id = status.id WHERE status.name = 'new'
;UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1
;SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks)
;INSERT INTO tasks(name, description, status_id, user_id) SELECT 'test', 'test', status.id, users.id FROM status, users WHERE status.name = 'new' AND users.fullname = 'Joseph Mercado'
;SELECT * FROM tasks WHERE status_id <> (SELECT id FROM status WHERE name = 'completed')
;DELETE FROM tasks WHERE id = 1
;SELECT * FROM users WHERE email LIKE '%@gmail.com'
;UPDATE users SET fullname = 'test' WHERE id = (SELECT MIN(id) FROM users)
;SELECT status_id, COUNT(*) FROM tasks GROUP BY status_id
;SELECT * FROM tasks INNER JOIN users ON tasks.user_id = users.id WHERE users.email LIKE '%@gmail.com'
;SELECT * FROM users INNER JOIN tasks ON users.id = tasks.user_id WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress')
;SELECT * FROM users LEFT JOIN (SELECT user_id, COUNT(*) AS count FROM tasks GROUP BY user_id) tasks ON users.id = tasks.user_id