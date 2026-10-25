import os
from scipy.io import wavfile

def strip_metadata(diretorio_origem):
    pasta_destino = os.path.join(diretorio_origem, "sp404_limpos")
    os.makedirs(pasta_destino, exist_ok=True)

    for arquivo in os.listdir(diretorio_origem):
        if arquivo.lower().endswith('.wav'):
            caminho_completo = os.path.join(diretorio_origem, arquivo)
            
            try:
                # O scipy.io lê apenas os chunks puros (fmt e data)
                taxa_amostragem, dados_audio = wavfile.read(caminho_completo)
                
                # Salva um novo arquivo com cabeçalho RIFF/WAVE "vanilla"
                caminho_saida = os.path.join(pasta_destino, arquivo)
                wavfile.write(caminho_saida, taxa_amostragem, dados_audio)
                
                print(f"Limpo: {arquivo}")
            except Exception as e:
                print(f"Erro ao processar {arquivo}: {e}")

# Basta apontar para a pasta onde o Ableton salvou os exports
strip_metadata("./meus_exports")