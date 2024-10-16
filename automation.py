import subprocess

def run_commando(command):
    try:
        print(f"Executando: {command}")
        subprocess.run(command, check=True, shell=True)
        print("Comando executado com sucesso.\n")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {command}\nErro: {e}")

def install_dependencies():
    print("Instalando dependências...")
    run_command("pip install -r requirements.txt")

def run_tests():
    print("Executando testes automatizados...")
    run_command("pytest tests/")

def deploy():
    print("Simulando deploy local...")
    run_command("python src/main.py")

def automation_pipeline():
    print("Iniciando pipeline de automação...\n")
    install_dependencies()
    run_tests()
    deploy()
    print("Pipeline concluído.")

if __name__ == "__main__":
    automation_pipeline()
