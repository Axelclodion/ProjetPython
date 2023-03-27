import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('example.db')

# Création de la table
conn.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT,
             description TEXT,
             price REAL);''')

# Insertion des données
data = [
    {
        'title': 'Product 1',
        'description': 'Description of product 1',
        'price': 10.99
    },
    {
        'title': 'Product 2',
        'description': 'Description of product 2',
        'price': 19.99
    }
]

for product in data:
    conn.execute('''INSERT INTO products (title, description, price)
                 VALUES (?, ?, ?)''', (product['title'], product['description'], product['price']))

# Sauvegarde des modifications
conn.commit()

# Fermeture de la connexion
conn.close()

