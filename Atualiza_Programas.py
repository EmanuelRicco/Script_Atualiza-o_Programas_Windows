import os
import subprocess
import re
from datetime import datetime

# Definir diretório e arquivo de log no C:
diretorio_log = r"C:\Logs"
arquivo_log = os.path.join(diretorio_log, "atualizacao_winget.txt")

# Criar diretório de log, se não existir
if not os.path.exists(diretorio_log):
    os.makedirs(diretorio_log)

# Função para registrar mensagens no log
def registrar_log(mensagem):
    with open(arquivo_log, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {mensagem}\n")

# Função para limpar a saída do winget
def limpar_saida(saida):
    linhas = saida.split("\n")
    linhas_filtradas = []
    ignorar = False

    for linha in linhas:
        # Remover linhas com animação de instalação
        if re.match(r"^\s*[-\\|/]+\s*$", linha):
            continue
        # Remover espaços vazios excessivos
        if linha.strip() == "":
            continue
        # Filtrar mensagens irrelevantes
        if "Microsoft não é responsável" in linha or "licenciado para você" in linha:
            continue
        # Parar a coleta após "Iniciando a instalação do pacote..."
        if "Iniciando a instalação do pacote" in linha:
            ignorar = True
        if not ignorar:
            linhas_filtradas.append(linha.strip())

    return "\n".join(linhas_filtradas)

# Registrar início da atualização
registrar_log("🔄 Iniciando verificação de atualizações...")

# Verificar se há atualizações disponíveis
resultado = subprocess.run(["winget", "upgrade"], capture_output=True, text=True, encoding="utf-8")

# Se não houver pacotes para atualizar ou não houver pacotes instalados
if "No installed package" in resultado.stdout or "Nenhum pacote instalado foi encontrado" in resultado.stdout:
    registrar_log("✅ Nenhuma atualização disponível no momento.")
else:
    # Registrar lista de atualizações disponíveis
    registrar_log("📋 Atualizações disponíveis:")
    registrar_log(limpar_saida(resultado.stdout))

    # Executar atualização silenciosa somente se houver atualizações
    registrar_log("🚀 Iniciando atualização dos pacotes...")
    atualizar = subprocess.run(["winget", "upgrade", "--all", "--silent"], capture_output=True, text=True, encoding="utf-8")

    # Registrar a saída filtrada do winget
    if atualizar.stdout:
        registrar_log("✅ Atualização concluída.")
        registrar_log("📜 Saída do winget:")
        registrar_log(limpar_saida(atualizar.stdout))
    else:
        registrar_log("✅ Nenhuma atualização foi realizada.")

# Exibir mensagem final
print(f"✅ Processo concluído! Verifique o log em: {arquivo_log}")
