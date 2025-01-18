import psycopg2

conn = psycopg2.connect(database = "postgres",
                        user = "postgres",
                        host = 'localhost',
                        password = "postgres",
                        port = 5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS questiondb(
              id SERIAL PRIMARY KEY,
              question TEXT,
              answer TEXT)
""");

cur.execute("""INSERT INTO questiondb(question, answer) VALUES 
('What is the capital of France?', 'Paris'),
('What is the capital of Germany?', 'Berlin'),
('What is the capital of Italy?', 'Rome'),
('What is the biggest fruit in the world?', 'Watermelon'),
('What is the tallest building in the world?','Burj Khalifa')
""");


conn.commit()

cur.close()
conn.close()