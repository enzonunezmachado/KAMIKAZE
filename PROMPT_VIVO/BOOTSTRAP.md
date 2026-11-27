# BOOTSTRAP — Inicialização e retomada entre chats

**Obrigatório** em conversa nova, pedido de continuidade ou referência a trabalho anterior.

## 1. Navegação obrigatória por níveis

1. Leia `AGENTS.md` e `README.md` da raiz.
2. Leia `PROMPT_VIVO/AGENTS.md` e `PROMPT_VIVO/README.md`.
3. Leia `PROMPT_VIVO/CURRENT_WORK.md` e `PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md`.
4. Leia este arquivo e `CONTINUITY_SYSTEM.md`.
5. Leia `operations/README.md`, `operations/state.toml` e `operations/STATE.md`.
6. Leia `PROMPT_VIVO/runs/README.md`; identifique o RUN_ID em state.toml/STATE.
7. Leia `runs/<RUN_ID>/README.md` antes de abrir arquivos da execução.
8. Leia `RESUME_PACKET.md`, depois `RUN_STATE.md` e `PHASE_CONTROL.md`.
9. Abra plano, arquitetura, fontes, achados, handoff e fase somente conforme a tarefa.
10. Ao decidir entre pesquisar mais ou testar, leia `QUALITY_GATE.md` e `RESEARCH_METHOD.md`.

**Regra:** ao entrar em qualquer outra pasta, leia primeiro seu README. Se estiver ausente, registrar a lacuna e criar/atualizar o índice antes de gravar vários arquivos naquela pasta.

## 2. Autoridade de cada arquivo

- `operations/state.toml`: snapshot estruturado para validação automática (RUN_ID, fase/gate, estados e limites).
- `operations/STATE.md`: visão humana do estado do projeto; resumo derivado do TOML.
- `PROMPT_VIVO/CURRENT_WORK.md`: última entrega substantiva e próxima ação de continuidade; não determina a fase ativa.
- `RUN_STATE.md`: fonte canônica do estado detalhado da execução.
- `PHASE_CONTROL.md`: decisão de gate e próxima ação permitida.
- `PHASE_ARCHITECTURE.md`: estrutura e dependências das fases.
- `RESUME_PACKET.md`: resumo curto derivado; nunca substitui estado, gate ou evidência.
- `MEMORY_HANDOFF.md`: contexto ampliado, não estado canônico.
- `SOURCE_LEDGER.md` + fontes originais: proveniência e evidência.
- `FINDINGS.md`: síntese; não substitui fontes.
- `USER_INPUT_LOG.md`: ideias, correções, decisões e autorizações humanas.
- `SESSION_LOG.md`: histórico append-only.
- `*_HISTORY.md`: arquivo histórico, nunca fonte do estado atual.

## 3. Reconstruir contexto

Identifique missão, RUN_ID, pergunta ativa, fase/gate, dependências, evidências, contraprovas, lacunas, decisões humanas, recursos, orçamento, prazo e autorizações. Diferencie fato documentado, inferência e hipótese. Não tratar ideias do usuário como descartáveis por ainda não terem evidência; capturá-las e avaliá-las.

## 4. Auditar consistência antes de agir

1. Comparar state.toml, operations/STATE, CURRENT_WORK, RUN_STATE, PHASE_CONTROL e RESUME_PACKET.
2. Verificar eventos recentes nos logs e commits que confirmam persistência.
3. Rodar `python scripts/validate_docs.py` quando houver ambiente; a CI executa o mesmo verificador.
4. Se houver conflito, determinar a fonte canônica específica, registrar a reconciliação e corrigir os resumos derivados.
5. Nunca escolher pelo timestamp isolado. Se não houver evidência suficiente, marcar BLOCKED/NEEDS_RECONCILIATION.

## 5. Incorporar a conversa atual

Registrar correções, ideias, prioridades, rejeições, decisões e autorizações em USER_INPUT_LOG. Atualizar documentos afetados. A mensagem atual do usuário orienta o próximo passo, respeitando restrições anteriores. Não pedir que repita informação já documentada.

## 6. Executar

- Auditar completude e escolher CONTINUE_PHASE, CREATE_SUBPHASE, REOPEN_PHASE, ADVANCE, SYNTHESIZE ou BLOCK.
- Continuar do próximo passo útil sem reiniciar pesquisas válidas.
- Abrir apenas documentos necessários; evitar carregar o repositório inteiro.
- Não realizar ações externas sem autorização explícita.

## 7. Checkpoint obrigatório

Após unidade substantiva:

1. Atualizar fontes/achados/perguntas/matriz quando aplicável.
2. Atualizar RUN_STATE e PHASE_CONTROL somente se estado/gate realmente mudou.
3. Atualizar state.toml e STATE.md de forma consistente.
4. Atualizar CURRENT_WORK se houve nova entrega substantiva.
5. Atualizar RESUME_PACKET por último; manter dentro de 120 linhas.
6. Atualizar USER_INPUT_LOG e logs append-only; atualizar CHANGELOG se a metodologia mudou.
7. Atualizar índices/README quando a estrutura mudou.
8. Executar validador e conferir o resultado.
9. Confirmar gravações GitHub e registrar commits.

Se não houver escrita/validação disponível, declarar explicitamente NÃO PERSISTIDO ou NÃO VALIDADO. Não alegar sucesso.

## 8. Limites

Não há execução em segundo plano após o chat terminar. AGENTS.md orienta agentes compatíveis; GitHub Actions verifica regras objetivas após push/PR. Nenhum desses mecanismos garante que qualquer IA, em qualquer interface, leia todos os arquivos ou obedeça regras sem integração apropriada.
