import xmlrpc.client

# Paramètres de connexion à Odoo
username = input("Veuillez entrer votre email Odoo : ")
url = input("Veuillez entrer l'URL de votre instance Odoo (ex : https://monodoo.com) : ")
password = input("Veuillez entrer votre clé API Odoo : ")
db = input("Veuillez entrer le nom de votre base de données Odoo : ")

# Connectez-vous à l'API Odoo
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
uid = common.authenticate(db, username, password, {})

# Connectez-vous au service d'objet
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Recherchez tous les actifs
asset_ids = models.execute_kw(db, uid, password, 'asset.model', 'search', [[]])

# Lire les détails des actifs
assets = models.execute_kw(db, uid, password, 'asset.model', 'read', [asset_ids])

# Afficher les informations de chaque actif
for asset in assets:
    print(asset)
