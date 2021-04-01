import sqlite3
import sys

from PyQt5 import QtWidgets

from conf import telainicial, cadastro


class MainWindow(QtWidgets.QMainWindow, telainicial.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.entrar.clicked.connect(self.login_botao)

    def login_botao(self):
        db = sqlite3.connect("infodb.db")
        query_pesquisar = db.cursor()

        for login in query_pesquisar.execute("SELECT * FROM InfoUsuario;"):
            email = login[1]
            senha = login[2]

            if self.email.text() == email and self.senha.text() == senha:
                print("Logado")

            else:
                print("Não logado")

        query_pesquisar.close()
        db.close()


# class CadastroPagina(QtWidgets.QMainWindow, cadastro.Ui_MainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.cadastrar.clicked.connect(self.cadastrar_botao)
#
#     def cadastrar_botao(self):
#         db = sqlite3.connect("infodb.db")
#         cursor = db.cursor()
#         cursor.execute("INSERT INTO InfoUsuario(id, email, senha, nome, sobrenome) VALUES (?, ?, ?, ?, ?)",
#                        (None, self.email.text(), self.senha.text(), self.nome.text(), self.sobrenome.text()))
#         print(self.email.text(), self.senha.text(), self.nome.text(), self.sobrenome.text())
#         print("Usuário cadastrado.")
#
#         cursor.close()
#         db.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

# def cadastro_pagina():
#     app = QtWidgets.QApplication(sys.argv)
#     window = CadastroPagina()
#     window.show()
#     app.exec_()


if __name__ == '__main__':
    main()
    # cadastro_pagina()
