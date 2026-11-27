# AGENTS — Regras obrigatórias para agentes neste repositório

Antes de qualquer trabalho, leia este arquivo e o README.md da raiz.

## Entrada e navegação

1. Para retomar trabalho anterior ou alterar documentação/metodologia, leia `PROMPT_VIVO/README.md`, `PROMPT_VIVO/AGENTS.md` e `PROMPT_VIVO/BOOTSTRAP.md`.
2. Leia `PROMPT_VIVO/CURRENT_WORK.md` antes de escolher a frente mais recente.
3. Para entrar em uma pasta, leia primeiro o README.md daquela pasta, quando existir. Se não existir, registre a lacuna e crie um índice antes de adicionar vários arquivos.
4. Siga os links e a ordem de leitura definidos pelos índices; não varra o repositório inteiro sem necessidade.
5. Antes de decidir pesquisar mais, construir ou executar, consulte `PROMPT_VIVO/OPERATING_PRINCIPLES.md`. Diga explicitamente quando a informação já basta e o próximo passo deve ser prático.
6. **Ao criar, revisar ou modificar qualquer site**, leia primeiro `web/README.md` e `web/AI_WEB_DEVELOPMENT_GUIDE.md`; inspecione o projeto existente e reutilize os assets canônicos quando compatíveis.

## Governança

- Consulte `PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md` para saber a função de cada classe de documento e a fonte canônica de cada informação.
- Não duplique estado atual em documentos de resumo. Resumos apontam para a fonte canônica.
- Preserve histórico; corrija o presente por novo registro, sem apagar decisões antigas.
- Não invente estado, evidência, aprovação, execução, teste ou persistência.
- Não altere NEXUS ou ATLAS a partir deste repositório.
- Não execute contatos, publicações, compras, assinaturas, deploys ou outras ações externas sem autorização explícita.

## Escrita e conclusão

- Antes de criar arquivo, verifique se já existe um documento com a mesma responsabilidade.
- Cada arquivo novo deve ter propósito, proprietário lógico, leitores, gatilho de atualização e referências de entrada/saída.
- Ao criar pasta navegável, inclua README.md com escopo, ordem de leitura, regras de gravação e arquivos subordinados.
- Faça checkpoint: atualize estado canônico, ponteiro, resumo e logs necessários.
- Execute `python scripts/validate_docs.py` quando disponível. A CI também executa verificações.
- Só declare conclusão após verificar as gravações e os resultados de validação.

## Limites de contexto

Não carregue todos os arquivos por padrão. Leia primeiro índices e resumos; abra documentos detalhados sob demanda conforme a tarefa.


## Proteção contra regressão do portfólio

- O layout público do portfólio é controlado por `portfolio_site/theme/main.html`; CSS isolado não substitui estrutura e navegação.
- Toda alteração de tema, templates, páginas ou pipeline do portfólio deve manter `custom_dir: portfolio_site/theme` e a etapa `python scripts/validate_portfolio_build.py` no workflow de Pages.
- Não remover nem afrouxar a validação automatizada para fazer uma publicação passar. Corrigir a causa da falha.
- Build concluída não equivale a inspeção visual. Nunca declarar que a aparência foi conferida sem evidência de navegador ou captura de tela.
