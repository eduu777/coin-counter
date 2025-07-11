# Coin Counter — Detecção de Moedas com YOLOv8 e OpenCV 🪙💰

---

Uma aplicação Python que utiliza **YOLOv8** e **OpenCV** para detectar moedas em tempo real pela **webcam** e informar o valor de cada uma.


## ⚠️ Arquivos Ignorados pelo Git ⚠️

Para manter o repositório leve e seguro, os seguintes arquivos/pastas **não são versionados** e devem ser criados ou obtidos manualmente:

- `.venv/` — Ambiente virtual Python (evita subir pacotes instalados)
- `*.pt` — Arquivos de pesos do modelo YOLOv8 (geralmente grandes e específicos)

---

## Instruções para usar o projeto ⚙️

### 1. Clone o repositório

```bash
    git clone https://github.com/eduu777/coin-counter.git
    cd coin-counter
```

### 2. Crie o ambiente virtual
```bash
    python -m venv .venv
```

### 3. Ative o ambiente virtual
- Windows
```bash
    .venv\Scripts\activate
```
- Linux
```bash
    source .venv/bin/activate
```

### 4. Instale as dependências manualmente
```bash
    pip install ultralytics opencv-python
```

### 5. Execute a aplicação
```bash
    python detectar_moedas.py
```

> Caso tenha problemas com o best.pt [clique aqui](https://drive.google.com/file/d/13FZEc0tYWR4xKh9HZy8s3MQk4e7d2-ZS/view?usp=sharing) para fazer o download, após baixar o arquivo crie uma pasta na raiz do projeto com o nome `weights` caso ela não exista, e cole o arquivo dentro.

---

## Dicas 💡

- Realize os testes em um ambiente bem iluminado para melhor qualidade da webcam e maior precisão nas detecções.
- Para encerrar o programa, pressione "ESC".

---

## Contribuições 🤝
> Pull requests são muito bem-vindos neste projeto!

---

## Autor 🧑‍💻
- Eduardo Nobre 
- 📩 nobreeduardo680@gmail.com 
- 🔗 https://www.linkedin.com/in/eduardo-nobre-8500a2209/