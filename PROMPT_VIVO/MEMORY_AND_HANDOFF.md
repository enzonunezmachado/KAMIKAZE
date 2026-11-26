# Memória e transferência entre chats

## 1. Princípio

O repositório é a memória explícita do trabalho. O chat é uma interface de execução temporária. Nenhuma informação crítica de continuidade deve existir apenas no chat.

## 2. Arquivos obrigatórios por execução

- `RUN_STATE.md` — estado atual, fase, progresso e próxima ação.
- `RESEARCH_PLAN.md` — perguntas, hipóteses, escopo e método.
- `SOURCE_LEDGER.md` — fontes e consultas relevantes.
- `FINDINGS.md` — achados consolidados e evidências.
- `OPEN_QUESTIONS.md` — dúvidas, lacunas, contradições e pesquisas pendentes.
- `MEMORY_HANDOFF.md` — resumo para o próximo chat.
- `FINAL_SYNTHESIS.md` — síntese final, inicialmente marcada como em elaboração.

Arquivos adicionais devem ser criados apenas quando houver necessidade real: análise de concorrentes, base de dados, mapa de público, cálculos, entrevistas etc.

## 3. Ao encerrar uma sessão

Atualizar:
- o que foi concluído;
- o que foi tentado e não funcionou;
- fontes consultadas;
- decisões e motivos;
- arquivos alterados;
- estado exato da fase;
- próxima ação concreta;
- decisões que aguardam o usuário.

## 4. Ao iniciar outro chat

A nova IA deve:
1. ler o Master Prompt e documentos centrais;
2. localizar a execução ativa no índice ou em `runs/`;
3. ler RUN_STATE e MEMORY_HANDOFF;
4. consultar apenas arquivos adicionais referenciados como necessários;
5. verificar se houve mudança relevante de contexto;
6. continuar da próxima ação, sem repetir fases concluídas.

## 5. Resumo de transferência

O `MEMORY_HANDOFF.md` deve caber em uma leitura rápida e conter:
- ID e objetivo da execução;
- estado e fase;
- decisões já tomadas;
- descobertas essenciais;
- fontes-chave;
- lacunas;
- próxima ação exata;
- arquivos que precisam ser lidos;
- avisos sobre o que não repetir.

## 6. Falha de acesso

Se a IA não conseguir ler ou escrever no GitHub:
- não fingir que leu ou salvou;
- pedir os arquivos necessários ou fornecer instruções para acesso;
- entregar o conteúdo atualizado em formato copiável;
- preservar no chat o checkpoint mínimo até que seja salvo.
