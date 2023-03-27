import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('example.db')

# Création de la table "products" avec ses colonnes et types de données
conn.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT,
             description TEXT,
             price REAL);''')

# Données à insérer dans la table "products"
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

# Insertion des données dans la table "products"
for product in data:
    conn.execute('''INSERT INTO products (title, description, price)
                 VALUES (?, ?, ?)''', (product['title'], product['description'], product['price']))

# Sauvegarde des modifications dans la base de données
conn.commit()

# Fermeture de la connexion à la base de données
conn.close()

