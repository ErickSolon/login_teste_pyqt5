import sqlite3

try:
    db = sqlite3.connect("../infodb.db")
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO InfoUsuario(id, email, senha, nome, sobrenome) VALUES (?, ?, ?, ?, ?)",
        (None, "fodase@mail.com", "123", "teste", "bosta")
    )
    print("Usuário cadastrado.")

    cursor.close()
    db.close()

except Exception as e:
    print("ERRO:", e)