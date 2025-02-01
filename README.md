# 💻 Automação de Envio de E-mails com PyAutoGUI

## 📕 Descrição
Este script automatiza o processo de exportação de contatos do Gmail e envio de e-mails utilizando a biblioteca `pyautogui`. Ele:
- Abre o Google Chrome e acessa o Gmail.
- Localiza e exporta a lista de contatos.
- Lê os contatos exportados e envia e-mails automaticamente.
- Utiliza a biblioteca `pyperclip` para copiar e colar o conteúdo do e-mail.

## ☕ Como Usar
### Pré-requisitos
Antes de executar o script, certifique-se de ter instalado as seguintes bibliotecas:
```bash
pip install pyautogui pandas pyperclip
```

Além disso, garanta que as imagens referenciadas (`google.png`, `pontinhos.png`, `contatos.png`, `exportar.png`, `confirmar_exportar.png`, `escrever.png`) estejam na mesma pasta do script para que a automação funcione corretamente.

### Executando o Script
1. Execute o script Python.
2. O código exibirá um alerta informando que a automação está iniciando.
3. Não mexa no computador até que o processo seja concluído.
4. Ao final, um alerta aparecerá informando que a automação foi finalizada.

### Observações
- O script pressupõe que os ícones do Gmail e dos botões de exportação de contatos não mudem de posição.
- Se houver falha na localização de imagens, ajuste a `confidence=0.9` no `pyautogui.locateOnScreen()` para valores entre 0.7 e 0.95 conforme necessário.
- Certifique-se de que o arquivo `contacts.csv` está corretamente formatado com a coluna `E-mail 1 - Value` contendo os e-mails a serem utilizados.

## Contribuindo para o Projeto
Caso queira contribuir com melhorias ou correções para este projeto, siga os seguintes passos:
1. Faça um fork do repositório.
2. Crie uma branch para sua modificação (`git checkout -b minha-modificacao`).
3. Faça commit das suas alterações (`git commit -m 'Melhoria no script'`).
4. Faça push para a branch (`git push origin minha-modificacao`).
5. Abra um Pull Request para análise.

Sinta-se à vontade para sugerir melhorias!
