# Memória e transferência entre chats

## 1. Princípio
O repositório é a memória explícita do trabalho. O chat é uma interface de execução temporária. Nenhuma informação crítica de continuidade deve existir apenas no chat. A retomada deve reconstruir o contexto, não apenas repetir um resumo superficial.

## 2. Arquivos obrigatórios por execução
- `RUN_STATE.md` — estado, fase, progresso e próxima ação.
- `RESUME_PACKET.md` — pacote canônico de retomada rápida, com identidade do projeto, execução, pesquisa ativa, evidências, decisões, restrições e arquivos detalhados.
- `RESEARCH_PLAN.md` — perguntas, hipóteses, escopo e método.
- `SOURCE_LEDGER.md` — fontes e consultas relevantes.
- `FINDINGS.md` — achados consolidados e evidências.
- `OPEN_QUESTIONS.md` — dúvidas, lacunas, contradições e pesquisas pendentes.
- `MEMORY_HANDOFF.md` — resumo de transferência.
- `USER_INPUT_LOG.md` — comentários, correções, preferências, decisões e autorizações do usuário que alterem o trabalho.
- `FINAL_SYNTHESIS.md` — síntese final, inicialmente em elaboração.

## 3. Ao encerrar uma sessão ou checkpoint
Atualizar o que foi concluído; o que foi tentado e falhou; fontes consultadas; decisões e motivos; arquivos alterados; estado exato da fase; próxima ação concreta; decisões aguardando usuário; comentários recentes que alteraram o plano. Sincronizar RESUME_PACKET, RUN_STATE, MEMORY_HANDOFF, plano, arquitetura e operations/STATE.

## 4. Ao iniciar outro chat
Executar `PROMPT_VIVO/BOOTSTRAP.md`. Em resumo:
1. ler os documentos de identidade e governança do projeto;
2. identificar execução ativa por operations/STATE;
3. ler RESUME_PACKET antes de detalhes;
4. ler RUN_STATE, arquitetura, controlador, plano, handoff e checkpoint;
5. abrir instrução completa da fase ativa e artefatos citados;
6. conferir fontes, achados e perguntas abertas relevantes;
7. reconstruir projeto, execução, build/entrega em investigação, fase, hipóteses, evidências, decisões, restrições e próxima ação;
8. incorporar mensagens do usuário na conversa atual e registrar impacto;
9. auditar divergências e completude antes de executar.

Não pedir que o usuário repita dados já documentados. Não afirmar certeza total se os arquivos não cobrem algum detalhe. Declarar o que não foi possível verificar.

## 5. Feedback e evolução da execução
Comentários do usuário podem modificar prioridade, escopo, método, critério de sucesso, preferência de canal ou arquitetura. Antes de continuar:
- classificar o comentário (correção, preferência, nova hipótese, restrição, autorização ou observação sem impacto);
- avaliar se conflita com decisão anterior;
- registrar em USER_INPUT_LOG com data, impacto e status;
- atualizar arquivos afetados, preservando histórico;
- não interpretar "próxima" como consentimento para gasto ou ação externa.

## 6. Conteúdo mínimo do RESUME_PACKET
- ID/título e objetivo da execução;
- missão maior do projeto e meta contextual;
- pesquisa específica em andamento e por que ela existe;
- fase/subfase e gate exatos;
- decisões humanas;
- descobertas e fontes-chave, incluindo o que elas NÃO provam;
- tentativas malsucedidas e contraprovas;
- lacunas e dependências;
- recursos, cotas, prazos e limites;
- ações proibidas sem aprovação;
- próxima ação executável;
- lista dos arquivos que precisam ser lidos.

## 7. Falha de acesso
Se a IA não conseguir ler ou escrever no GitHub:
- não fingir que leu ou salvou;
- pedir os arquivos necessários ou fornecer instruções para acesso;
- entregar conteúdo atualizado em formato copiável;
- preservar no chat o checkpoint mínimo até que seja salvo.

## 8. Limite de confiabilidade
A continuidade depende da qualidade, atualização e acessibilidade dos registros. O protocolo reduz perda de contexto, mas não garante onisciência nem substitui validação de arquivos. Se houver contradição, sinalizar e reconciliar antes de prosseguir.


## 9. Sistema operacional de continuidade (obrigatório)
Consultar `PROMPT_VIVO/CONTINUITY_SYSTEM.md`. Além dos arquivos já listados, manter:
- `PROMPT_VIVO/SESSION_LOG.md`: log global append-only;
- `runs/<RUN_ID>/SESSION_LOG.md`: log append-only da execução;
- `PROMPT_VIVO/NEXT_CHAT_PROMPT.md`: texto copiável para iniciar novo chat.

Em cada checkpoint, atualizar primeiro fontes/achados/perguntas e controlador; depois RUN_STATE, MEMORY_HANDOFF, RESUME_PACKET e operations/STATE; por último registrar eventos nos logs. Confirmar escrita antes de declarar persistência. O pacote de retomada deve refletir o estado mais recente, não apenas resumir a missão original.

Quando a conversa se aproximar do limite, parar a pesquisa, salvar o checkpoint e deixar a próxima ação específica. A retomada em novo chat deve executar BOOTSTRAP, ler os logs e continuar automaticamente sem reiniciar a pesquisa.
