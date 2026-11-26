### KAM-2026-11-26-008 — Gate de pesquisa para experimento

- **Motivo:** preocupação do usuário de que a operação possa pesquisar e planejar excessivamente, adiando o momento em que o comportamento real do comprador precisa ser observado.
- **Aplicado:** QUALITY_GATE, RESEARCH_METHOD e EXECUTION_PROTOCOL agora diferenciam fatos pesquisáveis de variáveis que exigem experimento (disposição a pagar, conversão, retenção, recompra). Criados estados de decisão RESEARCH_MORE, READY_TO_TEST, NOT_WORTH_TESTING e BLOCKED.
- **Regra:** interromper pesquisas de baixo valor informacional; se um experimento mínimo for ético, reversível, barato e autorizado, recomendá-lo. Não fabricar percentuais de chance sem dados calibrados.
- **Controle humano:** contatos, publicações, cadastros, despesas e compromissos continuam exigindo autorização explícita.
- **Persistência:** confirmar gravações e CI antes de declarar validação completa.

### KAM-2026-11-26-007 — Arquitetura documental, validação e MkDocs

- **Data:** 2026-11-26
- **Pedido:** comparar a arquitetura Markdown com Spec Kit/BMAD/AGENTS.md/LangChain/Diátaxis; melhorar continuidade, granularidade, leitura obrigatória por pastas, sincronização verificável e criar teste MkDocs/portfólio Markdown.
- **Diagnóstico:** resumos e snapshots acumulavam histórico; CURRENT_WORK, STATE, RUN_STATE, PHASE_CONTROL e RESUME_PACKET não tinham autoridade suficientemente explícita; estado de fase em STATE/RESUME estava desatualizado em relação ao controlador e RUN_STATE.
- **Aplicado:** AGENTS.md raiz e Prompt Vivo; ARCHITECTURE_GOVERNANCE; READMEs de navegação; state.toml; snapshots compactos; histórico anterior preservado em STATE_HISTORY e RUN_HISTORY; BOOTSTRAP/CONTINUITY/NEXT_CHAT/CURRENT_WORK/RESUME_PACKET atualizados; PHASE_CONTROL marcado com snapshot vigente.
- **Validação:** criado scripts/validate_docs.py para verificar arquivos obrigatórios, budgets, links selecionados e sincronização TOML/Markdown; GitHub Actions executa validação, build MkDocs e markdownlint.
- **MkDocs:** criado site demonstrativo com fonte Markdown em portfolio_site/docs; ainda não publicado. Cases e dados fictícios estão explicitamente rotulados.
- **NEXUS:** criada proposta estratégica Diátaxis + Obsidian em repositório separado NEXUS-DOCUMENTACAO; não houve alteração de código Android, banco, backup ou artefatos do AI Studio.
- **Limites:** CI ainda precisa rodar e ser inspecionada; AGENTS.md depende do suporte do agente; scripts não validam verdade semântica nem obrigam qualquer IA a obedecer.
- **Não realizado:** nenhum agente externo instalado, nenhum dado real exportado, nenhuma publicação, contato, venda, gasto ou deploy.
- **Persistência:** confirmar commits individuais e workflow antes de declarar validação concluída.

# SESSION LOG — Histórico global do Kamikaze

Este log registra checkpoints e mudanças relevantes do projeto. É append-only: correções e reconciliações entram como novos eventos, sem apagar o histórico anterior.

## Eventos

### KAM-2026-11-26-001 — Implantação do sistema de continuidade
- **Data:** 2026-11-26
- **Tipo:** governança / continuidade entre chats
- **Motivo:** pedido do usuário para documentar atualizações do Kamikaze e permitir retomada automática da pesquisa após o limite de uma conversa.
- **Executado:** auditoria dos arquivos existentes de bootstrap, estado, handoff, protocolo e resume packet; identificada estrutura prévia semelhante à do NEXUS, mas com estado e documentação parcialmente divergentes.
- **Criados:** `PROMPT_VIVO/CONTINUITY_SYSTEM.md`, `PROMPT_VIVO/NEXT_CHAT_PROMPT.md`, `PROMPT_VIVO/SESSION_LOG.md` e log específico da execução ativa.
- **Alterados:** BOOTSTRAP, MASTER_PROMPT, EXECUTION_PROTOCOL, MEMORY_AND_HANDOFF, CHANGELOG, operations/STATE e arquivos de estado da execução.
- **Resultado:** checkpoint obrigatório, log cronológico, prompt de novo chat e regra de sincronização do estado.
- **Limitação:** continuidade não é execução em segundo plano; requer checkpoint enquanto há sessão e ferramenta de persistência disponível.
- **Persistência:** CONFIRMAR após concluir as gravações GitHub deste evento.


### KAM-2026-11-26-001A — Confirmação de persistência
- **Data:** 2026-11-26
- **Resultado:** arquivos do sistema de continuidade e documentos dependentes gravados com sucesso no GitHub.
- **Commit de confirmação mais recente:** 0d87d4f1adf88e7e2fd661a8f1dddda5b5e5f9b1.
- **Status:** CONFIRMADO.


### KAM-2026-11-26-002 — Catálogo de skills e repositórios open source
- **Data:** 2026-11-26
- **Executado:** retomada pelo NEXT_CHAT_PROMPT/BOOTSTRAP; inventário da árvore e registry Affitor (53 skills/8 categorias); resenha crítica e comparação de OpenAffiliate, Postiz, workflows n8n, AffiliateOS, Affiliate Content Automation, Agentic Social Manager e hidrix-tools.
- **Artefato criado:** `PROMPT_VIVO/knowledge/MAK_OPEN_SOURCE_SKILLS_AND_REPOSITORIES_CATALOG.md`.
- **Arquivos sincronizados:** knowledge README, Source Ledger S414–S423, Findings, PHASE_03.5, USER_INPUT_LOG, RUN_STATE, RESUME_PACKET e log da execução.
- **Decisão:** adaptar workflows em skills próprias, sem importar código de terceiros; preservar revisão/aprovação humana, evidência e compliance brasileiro.
- **Persistência:** CONFIRMADO nos commits individuais desta rodada.


### KAM-2026-11-26-003 — Acionador persistente de tráfego pago
- **Data:** 2026-11-26
- **Executado:** criada documentação do acionador `MAK-PAID-TRAFFIC-MODULE`, com protocolo de confirmação, arquitetura, etapas/gates, skills, segurança financeira, compliance e handoff.
- **Pesquisa:** inventário de 49 skills marketing-skills (49/49 slugs únicos conferidos); repositórios Google Ads MCP/SDK, Meta SDKs, Ryze MCP, n8n, AdsOnSheets, clientreport, Meridian e reporting workflow.
- **Artefato principal:** `PROMPT_VIVO/knowledge/PAID_TRAFFIC_MODULE_ACTIVATION.md`.
- **Continuidade:** BOOTSTRAP, NEXT_CHAT_PROMPT e CONTINUITY_SYSTEM agora descobrem acionadores dormentes.
- **Estado:** DORMANT / DOCUMENTED / NOT IMPLEMENTED. Nenhuma implementação, integração, conta, campanha, publicação ou gasto.
- **Persistência:** commits individuais confirmados.


### KAM-2026-11-26-004 — Casos de construção com IA e ferramentas gratuitas
- **Data:** 2026-11-26
- **Executado:** pesquisa consolidada de aplicações criadas com IA e planos gratuitos; Stockroom/AppJet (demo + código público), MyClaw Tools (249 ferramentas, 0 pagantes no snapshot), Somnia, Toolkiya, HookLayer, RenderArchi, AssetShark e HypeDesk. Auditoria de limites oficiais Gemini, Supabase, Cloudflare, Vercel e GitHub Copilot.
- **Artefatos:** `knowledge/MAK_ZERO_COST_AI_BUILD_CASES.md` e `SOURCE_LEDGER_SUPPLEMENT_S436_S453.md`; fases/estado atualizados.
- **Conclusão:** $0 pode produzir um full-stack demonstrável, mas planos gratuitos podem proibir uso comercial, pausar projetos ou limitar IA/CPU; build, produção, distribuição e receita são gates distintos.
- **Ações externas/gastos:** nenhum.
- **Persistência:** confirmar commits individuais.


### KAM-2026-11-26-004A — Auditoria estática Stockroom/AppJet
- Inspecionados schema, repositório, transações, rotas, parsing, testes, headers, CSV e Dockerfile; leitura de termos e privacidade AppJet.
- Encontradas boas práticas de integridade/validação, mas demo sem login e sem auth/tenant authorization visível nas rotas analisadas. Não usar dados reais. Testes não foram executados; sem pentest.
- AppJet declara processamento EUA/Canadá, não treino/retenção de código após coding, mas processa credenciais/env vars e não garante disponibilidade. S451–S453.
- Nenhuma conta conectada ou app criado.


### KAM-2026-11-26-005 — Serviços tecnológicos locais assistidos por IA
- Documentada linha de serviços locais com diagnóstico de maturidade, implantação competitiva e manutenção recorrente; lista exploratória de pizzarias em Taboão e política de prospecção responsável.
- Fontes S454–S466; documento `knowledge/MAK_LOCAL_AI_SOLUTIONS_AND_LEAD_ENGINE.md`.
- Nenhum contato, mensagem, instalação, publicação, venda ou gasto ocorreu.



## 2026-11-26 — estrutura documental de empresas e projetos
- Criado `operations/COMPANY_SOLUTIONS/` para lotes de 20 empresas únicas, ranking, deduplicação, dossiês, status de contato/venda/entrega, projetos, contratos recorrentes e financeiro.
- Estado DOCUMENTADO / NÃO ATIVADO; sem empresas inseridas, lote, contato, projeto, venda ou gasto.


### KAM-2026-11-26-006 — Ponteiro canônico de trabalho atual
- **Pedido:** fazer o sistema apontar automaticamente para a última linha/entrega desenvolvida ou atualizada.
- **Executado:** criado `PROMPT_VIVO/CURRENT_WORK.md` como ponteiro único; atualizado BOOTSTRAP, CONTINUITY_SYSTEM, NEXT_CHAT_PROMPT e operations/STATE; adicionado apontamento no RESUME_PACKET e registro da entrada do usuário.
- **Regra:** em cada checkpoint substantivo, atualizar o ponteiro e sincronizar atalhos; distinguir última entrega de linha de pesquisa ainda ativa; não inferir foco pela data/nome de arquivo.
- **Limite:** checkpoint exige sessão/ferramenta ativa; não existe execução em segundo plano após o chat terminar.
- **Persistência:** commits confirmados para os arquivos listados neste evento.
