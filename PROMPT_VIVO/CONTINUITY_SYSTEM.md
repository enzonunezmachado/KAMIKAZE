# CONTINUITY SYSTEM — Memória, estado e retomada entre sessões

**Escopo:** NEGÓCIO DIGITAL KAMIKAZE.  
**Objetivo:** retomar trabalho com precisão sem depender da memória interna da IA nem carregar todo o repositório em cada conversa.

## 1. Princípio
O GitHub é a memória persistente versionada; a conversa é temporária. Uma alteração só é persistida após confirmação do GitHub. Não existe execução em segundo plano depois do encerramento da sessão.

## 2. Arquitetura de autoridade
| Informação | Fonte canônica | Papel dos demais arquivos |
|---|---|---|
| Estado estruturado do projeto/execução | `operations/state.toml` | STATE.md é projeção humana validada |
| Execução ativa e restrições detalhadas | `operations/STATE.md` | README e resume apontam |
| Última entrega substantiva | `PROMPT_VIVO/CURRENT_WORK.md` | Atalhos apontam |
| Estado da execução/fase | `runs/<RUN_ID>/RUN_STATE.md` | RESUME_PACKET resume |
| Gate e próxima ação permitida | `runs/<RUN_ID>/PHASE_CONTROL.md` | RUN_STATE e RESUME apontam |
| Arquitetura/dependências das fases | `PHASE_ARCHITECTURE.md` | Plano e handoff referenciam |
| Evidência | `SOURCE_LEDGER.md` + fonte original | FINDINGS e resumos citam IDs |
| Decisões/autorizações humanas | `USER_INPUT_LOG.md` | Operação implementa sem reescrever |
| Contexto ampliado | `MEMORY_HANDOFF.md` | RESUME contém só o essencial |
| Histórico | SESSION_LOGs e *_HISTORY.md | Não substituem o presente |

## 3. Leitura progressiva
A IA deve navegar por README e AGENTS em cada nível antes de abrir a pasta seguinte. Começar na raiz, seguir Prompt Vivo, identificar a execução em operations, ler o README da execução e então abrir o pacote de retomada. Detalhes de fontes, fases e dossiês são consultados sob demanda.

## 4. O que cada tipo de arquivo deve conter
- README: propósito, ordem de leitura, conteúdo da pasta e regras de gravação.
- AGENTS: instruções obrigatórias para agentes compatíveis, curtas e acionáveis.
- Estado: somente snapshot atual; não acumular diário.
- Resume packet: resumo curto e links; sem duplicar pesquisa.
- Handoff: contexto ampliado e explicações necessárias à transferência.
- Log: eventos append-only, com mudanças, limites e commit.
- Ledger: fontes e proveniência.
- Findings: síntese ligada às fontes.
- Knowledge: conhecimento reutilizável revisado, com validade e data.
- Template: estrutura vazia; não guardar registros reais no template.
- Dossiê: informação de uma entidade/execução específica.

## 5. Checkpoint
1. Identificar o que realmente mudou e se é substantivo.
2. Atualizar documentos primários afetados.
3. Atualizar state.toml e as projeções de estado relacionadas.
4. Não atualizar ponteiro de última entrega; o estado estruturado já informa prioridade e próxima ação.
5. Atualizar índices e resumos derivados.
6. Acrescentar logs; não reescrever histórico.
7. Rodar `scripts/validate_docs.py` e, no GitHub, aguardar CI.
8. Confirmar cada gravação e registrar commit(s).

Não criar commits por cada busca isolada. Agrupar alterações coerentes, sem deixar lotes importantes sem registro.

## 6. Validação e limites
- `scripts/validate_docs.py` verifica arquivos obrigatórios, limites de tamanho, links locais selecionados e consistência entre state.toml e snapshots Markdown.
- GitHub Actions roda o validador, constrói o site MkDocs e executa markdownlint em push/PR.
- CI valida estrutura e propriedades objetivas; não julga verdade de evidências, qualidade de hipótese, autorização ou semântica profunda.
- AGENTS.md só é aplicado automaticamente por ferramentas que reconhecem esse padrão. Em outras interfaces, BOOTSTRAP e instruções explícitas continuam necessários.
- Se branch protection não exigir checks, uma gravação direta pode ocorrer mesmo com CI falhando; falha de CI significa que a documentação não passou no gate.

## 7. Divergências
Consultar a fonte canônica da informação divergente. Verificar logs e commits. Corrigir derivados e registrar reconciliação. Se não houver base segura, marcar BLOCKED/NEEDS_RECONCILIATION; nunca adivinhar.
