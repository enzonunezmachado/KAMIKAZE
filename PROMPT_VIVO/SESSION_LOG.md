### KAM-2026-11-27 — Validador documental orientado ao RUN_ID ativo
- **Problema:** `scripts/validate_docs.py` apontava sempre para `PV-2026-11-25-TOTALMENTE-GRATUITA`, mesmo que `operations/state.toml` passasse a indicar outra execução.
- **Correção:** o script agora lê `project.active_run`, valida o formato do ID e deriva os arquivos obrigatórios, budgets e checks do diretório ativo. A checagem de links inclui as entradas comerciais e web.
- **Validação:** workflow `45940323180` PASS: validador documental, MkDocs strict e markdownlint.

---

### KAM-2026-11-27 — Correção estrutural do container do portfólio
- **Diagnóstico:** `.km-main` e `.rst-content` aplicavam max-width e padding em camadas aninhadas, estreitando o conteúdo em relação ao eixo interno do header/footer.
- **Correção:** `.km-main` passou a ser wrapper full-width sem padding; `.rst-content` ficou como único container central; header e footer receberam largura explícita de 100%.
- **Validador:** `scripts/validate_portfolio_build.py` agora verifica os três assets, shell em todas as páginas, largura total, container compartilhado, breakpoint mobile, reduced motion e comportamento de navegação.
- **Metodologia:** `web/AI_PROMPT_SCRIPTS.md` recebeu regra reutilizável contra max-width/padding duplicados.
- **CI/deploy:** documentação `45940140564` PASS; deploy Pages `45940140491` PASS. Inspeção visual em navegador ainda pendente.

---

### KAM-2026-11-27 — Auditoria de consistência e recuperação da CI
- **Escopo:** revisão da árvore completa do repositório, governança, estado, operação comercial, pesquisa, skills, site, scripts e workflows.
- **Achados principais:** divergência de última entrega entre TOML e CURRENT_WORK; BOOTSTRAP com caminho relativo incorreto; link para demo inexistente; README do Prompt Vivo com tabela malformada; skills/brief com meta antiga; caminho `experiments/` inexistente em uma skill; CI de documentação falhando por sincronização e lint; repositório público contendo contexto pessoal/financeiro em arquivos operacionais.
- **Correções persistidas:** reconciliados state.toml/CURRENT_WORK; corrigidos caminhos de retomada, link quebrado, índice Markdown, meta vigente e referência de armazenamento; ampliada validação para links da Primeira Venda; corrigido lint nos arquivos de entrada; removidos dados financeiros pessoais de cópias atuais do módulo Company Solutions e política de orçamento.
- **Validação:** workflow `45939953007` PASS no commit `70ec82b`: validador documental, build MkDocs strict e markdownlint concluídos com sucesso. Deploy Pages `45939795049` PASS no commit `2932ad2`.
- **Limites:** não houve inspeção visual em navegador/captura. O histórico Git ainda contém versões anteriores com dados pessoais; limpeza de histórico ou separação em repositório privado exige decisão do usuário.
- **Estado comercial:** piloto Primeira Venda continua sem contatos, propostas ou receita; orçamento operacional R$0. Nenhuma ação externa foi realizada.

---

### KAM-2026-11-27 — Workflow de deploy MkDocs para GitHub Pages
- **Autorização:** usuário aprovou corrigir a automação e publicar o portfólio.
- **Diagnóstico:** fonte do site MkDocs é `portfolio_site/docs`, saída `portfolio_site/site`; workflow anterior `docs-quality.yml` apenas validava e construía, não publicava. Histórico anterior indicava Pages por branch/Jekyll.
- **Implementado:** `.github/workflows/deploy-pages.yml` com build `mkdocs build --strict`, artefato somente da saída MkDocs e deploy via `actions/deploy-pages`.
- **Commit do workflow:** `05f6cb7c8662d7144350c142089b53709fd40779`.
- **Pré-requisito:** Settings → Pages → Build and deployment → Source = GitHub Actions. O conector não oferece escrita para essa configuração administrativa; usuário precisa selecioná-la se ainda estiver em modo branch.
- **Verificação:** consulta de status do commit retornou lista vazia; não foi possível confirmar execução, sucesso do build ou deploy. Não declarar publicação concluída até checar Actions e abrir o site.
- **Referência técnica:** documentação oficial do GitHub sobre [workflows personalizados](https://docs.github.com/pt/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) e [fonte de publicação](https://docs.github.com/pt/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
- **Próximo passo:** usuário seleciona GitHub Actions em Settings → Pages; depois verificar o workflow e a página publicada.

### KAM-2026-11-27 — Base reutilizável de desenvolvimento web
- **Pedido:** criar padrão para sites do Kamikaze com tema escuro, CSS/JavaScript organizados e instruções consultáveis pela IA.
- **Entregue:** `web/README.md`, `web/AI_WEB_DEVELOPMENT_GUIDE.md`, `web/templates/starter.html`, `web/templates/README.md`, `portfolio_site/docs/assets/kamikaze-base.css` e `portfolio_site/docs/assets/kamikaze.js`.
- **Integração:** `mkdocs.yml`, `AGENTS.md`, README raiz e documentação do portfólio atualizados.
- **Padrão:** dark azul-marinho/grafite, texto cinza-claro, responsivo, HTML semântico, CSS modular e JavaScript vanilla progressivo.
- **Referências:** MDN (semântica e acessibilidade, CSS/JS acessíveis, responsive design), web.dev Learn Responsive Design e Chrome for Developers (design tokens).
- **Limites:** assets e documentação persistidos; status de checks não retornou verificações. Build MkDocs e revisão visual não foram confirmados. Nenhum deploy/publicação realizado.
- **Prioridade comercial:** preservada; esta melhoria estrutural não altera a meta então vigente de R$140 até 08/12 nem constitui validação de receita.

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


### KAM-2026-11-27 — Reorientação da pesquisa e triagem de mercado
- Criada branch de segurança `archive/pre-autonomous-review-2026-11-27` a partir da main anterior às alterações desta sessão.
- Pesquisa de tendências sintetizada em `research/2026-11-27-opportunity-signals.md`: sinais brasileiros do Sebrae, tendências de marketplace e padrões de Spec Kit, Superpowers e Deep Agents.
- Decisão: pesquisa exploratória e afiliados em HOLD; prioridade operacional FIRST_SALE_PILOT — TEST. Nenhum framework, agente ou módulo novo foi instalado/criado.
- Meta operacional alinhada a R$150 recebidos até 08/12/2026; preço hipotético da oferta alinhado em R$150. Orçamento segue R$0.
- Triagem pública preliminar confirmou pistas de identidade para 17 dos 20 candidatos, mas não confirmou lacuna ou intenção. Plataformas como Booksy/Fresha já exibem serviços/preços de alguns negócios da região; lote continua não qualificado.
- Nenhum contato, proposta, publicação comercial ou gasto foi realizado. A validação documental ainda precisa ser executada após a sincronização final.

### KAM-2026-11-27 — Fechamento da sessão de reorientação
- Triagem final: 17/20 candidatos com presença pública identificável; três sem confirmação suficiente após três consultas. Nenhum qualificado ou contatado.
- Comparação Git confirmou branch histórica e 31 commits de avanço na main, com 15 arquivos alterados.
- O status de checks do último commit não retornou resultados; clone local indisponível por falha de resolução de rede. Validação automatizada desta rodada permanece NÃO CONFIRMADA.


### KAM-2026-11-27 — Evidência de concorrência em serviços de planilha
- Pesquisa adicional: pedidos reais de organização de planilhas/documentos em Workana e 99Freelas. Projeto genérico da 99Freelas exibia 710 propostas e 929 interessados; anúncios Workana semelhantes exibiam dezenas de propostas.
- CFA/MEMP 2026: gestão financeira/acesso a capital ~38% das dificuldades; precificação/vendas ~19%; falta de orçamento é barreira à capacitação. Dados orientam hipóteses, não validam oferta nem autorizam consultoria financeira.
- Decisão: não lançar serviço genérico de digitação/limpeza de planilhas. Manter apenas hipótese de tarefa operacional específica, condicionada a problema observável e capacidade de entrega.
- Corrigida inconsistência na contagem do lote: 17/20 identificáveis = três sem confirmação suficiente.
