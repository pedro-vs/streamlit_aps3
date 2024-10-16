import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"  

st.title("Gerenciamento de Usuários, Bicicletas e Empréstimos")

# -------------------- Gerenciamento de Usuários --------------------
st.header("Gerenciamento de Usuários")

# Listar usuários
if st.button("Listar Usuários"):
    response = requests.get(f"{API_URL}/usuarios")
    if response.status_code == 200:
        usuarios = response.json()
        st.write(usuarios)
    else:
        st.error("Erro ao buscar usuários.")

# Cadastrar usuário
st.subheader("Cadastrar Usuário")
nome = st.text_input("Nome")
cpf = st.text_input("CPF")
data_nascimento = st.text_input("Data Nascimento")

if st.button("Cadastrar Usuário"):
    if nome and cpf and data_nascimento:
        user_data = {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento}
        response = requests.post(f"{API_URL}/usuarios", json=user_data)
        if response.status_code == 201:
            st.success("Usuário cadastrado com sucesso!")
        else:
            st.error("Erro ao cadastrar usuário.")

# Buscar usuário
st.subheader("Buscar Usuário")
id_usuario = st.text_input("ID do Usuário")

if st.button("Buscar Usuário"):
    response = requests.get(f"{API_URL}/usuarios/{id_usuario}")
    if response.status_code == 200:
        usuario = response.json()
        st.write(usuario)
    else:
        st.error("Usuário não encontrado.")

# Atualizar usuário
st.subheader("Atualizar Usuário")
id_usuario_atualizar = st.text_input("ID do Usuário a ser atualizado")
novo_nome = st.text_input("Novo Nome", key="nome_input")
novo_cpf = st.text_input("Novo CPF", key="cpf_input")
nova_data_nascimento = st.text_input("Data Nascimento", key="data_nascimento_input")

if st.button("Atualizar Usuário"):
    if id_usuario_atualizar:
        update_data = {}
        if novo_nome:
            update_data["nome"] = novo_nome
        if novo_cpf:
            update_data["cpf"] = novo_cpf
        if nova_data_nascimento:
            update_data["data_nascimento"] = nova_data_nascimento
        
        response = requests.put(f"{API_URL}/usuarios/{id_usuario_atualizar}", json=update_data)
        if response.status_code == 200:
            st.success("Usuário atualizado com sucesso!")
        else:
            st.error("Erro ao atualizar usuário.")

# Deletar usuário
st.subheader("Deletar Usuário")
id_usuario_deletar = st.text_input("ID do Usuário a ser deletado")

if st.button("Deletar Usuário"):
    response = requests.delete(f"{API_URL}/usuarios/{id_usuario_deletar}")
    if response.status_code == 200:
        st.success("Usuário deletado com sucesso!")
    else:
        st.error("Erro ao deletar usuário.")

# -------------------- Gerenciamento de Bicicletas --------------------
st.header("Gerenciamento de Bicicletas")

# Listar bicicletas
if st.button("Listar Bicicletas"):
    response = requests.get(f"{API_URL}/bikes")
    if response.status_code == 200:
        bicicletas = response.json()
        st.write(bicicletas)
    else:
        st.error("Erro ao buscar bicicletas.")

# Cadastrar bicicleta
st.subheader("Cadastrar Bicicleta")
marca = st.text_input("Marca da Bicicleta")
modelo = st.text_input("Modelo da Bicicleta")
cidade = st.text_input("Cidade")

if st.button("Cadastrar Bicicleta"):
    if marca and modelo and cidade:
        bike_data = {"marca": marca, "modelo": modelo, "cidade": cidade}
        response = requests.post(f"{API_URL}/bikes", json=bike_data)
        if response.status_code == 201:
            st.success("Bicicleta cadastrada com sucesso!")
        else:
            st.error("Erro ao cadastrar bicicleta.")

# Buscar bicicleta
st.subheader("Buscar Bicicleta")
id_bike = st.text_input("ID da Bicicleta")

if st.button("Buscar Bicicleta"):
    response = requests.get(f"{API_URL}/bikes/{id_bike}")
    if response.status_code == 200:
        bicicleta = response.json()
        st.write(bicicleta)
    else:
        st.error("Bicicleta não encontrada.")

# Atualizar bicicleta
st.subheader("Atualizar Bicicleta")
id_bike_atualizar = st.text_input("ID da Bicicleta a ser atualizada")
novo_modelo = st.text_input("Novo Modelo")
nova_cidade = st.text_input("Nova Cidade")

if st.button("Atualizar Bicicleta"):
    if id_bike_atualizar:
        update_data = {}
        if novo_modelo:
            update_data["modelo"] = novo_modelo
        if nova_cidade:
            update_data["cidade"] = nova_cidade
        
        response = requests.put(f"{API_URL}/bikes/{id_bike_atualizar}", json=update_data)
        if response.status_code == 200:
            st.success("Bicicleta atualizada com sucesso!")
        else:
            st.error("Erro ao atualizar bicicleta.")

# Deletar bicicleta
st.subheader("Deletar Bicicleta")
id_bike_deletar = st.text_input("ID da Bicicleta a ser deletada")

if st.button("Deletar Bicicleta"):
    response = requests.delete(f"{API_URL}/bikes/{id_bike_deletar}")
    if response.status_code == 200:
        st.success("Bicicleta deletada com sucesso!")
    else:
        st.error("Erro ao deletar bicicleta.")

# -------------------- Gerenciamento de Empréstimos --------------------
st.header("Gerenciamento de Empréstimos")

# Listar empréstimos
if st.button("Listar Empréstimos"):
    response = requests.get(f"{API_URL}/emprestimos")
    if response.status_code == 200:
        emprestimos = response.json().get("emprestimos", [])
        st.write(emprestimos)
    else:
        st.error("Erro ao buscar empréstimos.")

# Cadastrar empréstimo
st.subheader("Cadastrar Empréstimo")
id_usuario_emprestimo = st.text_input("ID do Usuário para Empréstimo")
id_bike_emprestimo = st.text_input("ID da Bicicleta para Empréstimo")

if st.button("Cadastrar Empréstimo"):
    if id_usuario_emprestimo and id_bike_emprestimo:
        response = requests.post(f"{API_URL}/emprestimos/usuarios/{id_usuario_emprestimo}/bikes/{id_bike_emprestimo}")
        if response.status_code == 201:
            st.success("Empréstimo cadastrado com sucesso!")
        else:
            st.error(response.json().get("erro", "Erro ao cadastrar empréstimo."))


# Deletar empréstimo
st.subheader("Deletar Empréstimo")
id_emprestimo_deletar = st.text_input("ID do Empréstimo a ser deletado")

if st.button("Deletar Empréstimo"):
    response = requests.delete(f"{API_URL}/emprestimos/{id_emprestimo_deletar}")
    if response.status_code == 200:
        st.success("Empréstimo deletado com sucesso!")
    else:
        st.error("Erro ao deletar empréstimo.")
