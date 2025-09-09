import sqlite3
import os
import time

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


def criar_banco():
    os.system("cls")
    cursor.execute('''CREATE TABLE IF NOT EXISTS contas
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    chave VARCHAR(255) NOT NULL UNIQUE,
                    saldo FLOAT DEFAULT 0.0)''')
    conexao.commit()
    
def adicionar_contas():
    while True:
        criar_conta = input("(S/N) Deseja criar uma conta? ")
        if criar_conta == "S":
            try:
                time.sleep(1)
                nome = input("Nome da conta: ")
                chave = input("Chave da conta: ")
            
                cursor.execute("INSERT INTO contas (nome, chave, saldo) VALUES (?, ?, ?)", (nome, chave, 0.0))
                conexao.commit()
            
                time.sleep(1)
                print("Usuário inserido com sucesso!")
                time.sleep(1)
                
                os.system("cls")
                break
            except sqlite3.IntegrityError:
                print("A chave já existe. Por favor, escolha outra.")
        elif criar_conta == "N":
            print("Passando para transferência de saldo.")
            os.system("cls")
            time.sleep(1)
            break
        else:
            print("Por favor, use N para Não e S para Sim")
            time.sleep(2)
            os.system("cls")

def fazer_pix():
    while True:
        try:
            pix = input("(S/N) Deseja fazer um pix? ")
            break
        except ValueError:
            print("Por favor escolha S para sim, ou N para não")
    
    if pix == "N":
        time.sleep(1)
        print("Programa encerrado.")
    
    if pix == "S":
        while True:       
            pix_chave = input("Para qual chave você quer enviar? ")
            cursor.execute("SELECT chave FROM contas WHERE chave = ?", (pix_chave,))
            if cursor.fetchone() is None:
                print("Chave não encontrada.")
                time.sleep(1)
                os.system("cls")
            else:
                break
        valor = float(input("Valor a ser enviado: "))
        time.sleep(1)

        cursor.execute("UPDATE contas SET saldo = saldo + ? WHERE chave = ?", (valor, pix_chave))
        conexao.commit()
        
        print("Pix realizado com sucesso!")

criar_banco()
adicionar_contas()
fazer_pix()