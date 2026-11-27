## 2026-11-27 — playbooks compactos de design e criação web para IA

- Criado `web/AI_PROMPT_SCRIPTS.md`: regras práticas de hierarquia, composição, espaço, tipografia, cor, identidade, responsividade, acessibilidade e seis prompts reutilizáveis para delimitar, direcionar, construir, auditar, corrigir e fechar tarefas.
- Os critérios sintetizam os cursos e referências gratuitos já pesquisados (4 The Creatives, Canva Design School, HubSpot Academy, Cursa, web.dev, MDN, freeCodeCamp, CodigoZero, RNP e eMAG), convertendo fundamentos em decisões operacionais em vez de reproduzir aulas.
- Atualizado `web/README.md` para incluir os playbooks na navegação e orientar uso seletivo, sem colar todos os roteiros em cada tarefa.
- A base continua subordinada ao guia web existente; nenhuma nova ferramenta, framework, assinatura ou dependência foi adicionada.
- Persistência confirmada nos commits `028c19f` (playbooks) e `835ef29` (índice). Validação de CI ainda não consultada.

---

## 2026-11-27 — deploy do portfólio MkDocs pelo GitHub Actions

### Motivo
O GitHub Pages estava com histórico de publicação por branch/Jekyll, enquanto o projeto gera o site em `portfolio_site/site/` com MkDocs.

### Alterações
- Criado `.github/workflows/deploy-pages.yml`.
- Build executa em push para `main` quando fontes do portfólio/configuração/dependências mudam, ou manualmente.
- Instala dependências e executa `mkdocs build --strict`.
- Faz upload apenas de `portfolio_site/site/` e publica com `actions/deploy-pages`.
- Permissões mínimas e job de deploy separado do build.
- Atualizados índices de automação e README raiz.

### Pré-requisito e estado
- O usuário deve confirmar em Settings → Pages → Build and deployment → Source a opção **GitHub Actions** caso ainda esteja configurado para publicar de branch.
- O conector disponível não permite alterar a configuração administrativa do Pages.
- O workflow foi criado no commit `05f6cb7c8662d7144350c142089b53709fd40779`; execução, build e deploy ainda não foram confirmados pelo status consultado.
- Não declarar o site atualizado até verificar execução bem-sucedida e abrir a URL pública.

---

## 2026-11-27 — padrão reutilizável de desenvolvimento web

### Motivo
O usuário pediu uma base consistente para criar e modificar sites simples com qualidade visual, tema escuro, CSS/JavaScript organizados e instruções consultáveis por agentes de IA.

### Alterações
- Criada a área `web/` com índice, guia operacional para IA e template HTML inicial.
- Criado `kamikaze-base.css` com tokens visuais dark, layout responsivo, componentes reutilizáveis, foco visível e suporte a movimento reduzido.
- Criado `kamikaze.js` sem dependências, com menu mobile acessível e ano automático; aprimoramento progressivo.
- Integrados os assets ao `mkdocs.yml`; o CSS específico do portfólio permanece como camada de personalização.
- Atualizado `AGENTS.md` para exigir leitura do guia web antes de criar ou modificar sites.
- Atualizados índices e documentação do portfólio e README principal.

### Padrão de execução
HTML semântico, CSS e JavaScript separados, vanilla JS por padrão, mobile-first, acessibilidade, sem dependências pagas ou frameworks sem justificativa. O tema dark azul-marinho/grafite/cinza-claro é o padrão visual do Kamikaze.

### Limites e verificação
Os arquivos foram persistidos no GitHub. O status de checks consultado não retornou verificações; build MkDocs e revisão visual em navegador permanecem NÃO VALIDADOS. Nenhum deploy ou publicação foi realizado nesta tarefa.

---

## 2026-11-26 — Princípios operacionais para reduzir ciclos e priorizar execução

### Motivo
O usuário pediu consolidar regras persistentes para reconhecer quando pesquisar, quando parar, quando testar e quando abandonar uma linha improdutiva, evitando preparação infinita.

### Alterações
- Criado OPERATING_PRINCIPLES.md como referência normativa para pesquisa, construção, timebox, evidência, prioridade e critérios CONTINUE/TEST/HOLD/KILL/ESCALATE.
- Integradas as regras em AGENTS.md, PROMPT_VIVO/AGENTS.md e BOOTSTRAP.md.
- Adicionado o documento ao índice do Prompt Vivo.
- Atualizado CURRENT_WORK.md para apontar a entrega e orientar retomada prática.

### Regra central
Não pesquisar quando a próxima informação dificilmente muda a decisão e um teste barato, reversível e autorizado pode responder melhor. Não construir infraestrutura para hipóteses sem evidência comercial mínima. A IA deve dizer explicitamente quando estamos dando voltas e recomendar a próxima ação principal.

### Limites
Nenhum contato, publicação, gasto, deploy ou compromisso externo foi realizado. A CI das alterações atuais precisa ser consultada antes de declarar validação verde.

---

## 2026-11-26 — Regra de parada da pesquisa e prontidão para experimento

- Ampliado `QUALITY_GATE.md` para distinguir RESEARCH_MORE, READY_TO_TEST, NOT_WORTH_TESTING e BLOCKED.
- Ampliado `RESEARCH_METHOD.md` com valor da informação, separação entre pesquisa, prototipagem e experimento, e tratamento de resultados negativos.
- Ampliado `EXECUTION_PROTOCOL.md` com decisão explícita entre continuar pesquisando e testar.
- Regra central: não continuar pesquisa quando a próxima informação dificilmente muda a decisão e um experimento mínimo, ético, reversível, barato e autorizado pode responder melhor.
- Não inventar percentuais de sucesso sem dados calibrados; scores de prontidão são heurísticos, não probabilidades.
- Ações externas continuam sujeitas à autorização humana.

---

## 2026-11-26 — Governança documental, estado canônico e validação

### Motivação
A auditoria comparativa com Spec Kit, BMAD, AGENTS.md, LangChain Deep Agents e Diátaxis identificou risco de duplicação de estado, resumos extensos, dependência de disciplina manual e falta de verificação executável.

### Mudanças
- Adicionados `AGENTS.md` na raiz e em `PROMPT_VIVO/` com instruções de leitura e escrita para agentes compatíveis.
- Criado `ARCHITECTURE_GOVERNANCE.md` com função dos arquivos, fontes canônicas, navegação por READMEs, granularidade e classificação inspirada em Diátaxis.
- Criados/atualizados READMEs para operations, runs e a execução ativa.
- Criado `operations/state.toml` como snapshot estruturado verificável.
- Reduzidos `operations/STATE.md`, `RUN_STATE.md` e `RESUME_PACKET.md`; conteúdo anterior preservado em `STATE_HISTORY.md` e `RUN_HISTORY.md`.
- Atualizados BOOTSTRAP, CONTINUITY_SYSTEM, NEXT_CHAT_PROMPT, CURRENT_WORK e índices.
- Criado `scripts/validate_docs.py` para verificar arquivos obrigatórios, budgets de linhas, links selecionados e sincronização TOML/Markdown.
- Criado workflow GitHub Actions para validar documentação, construir site MkDocs e executar markdownlint.
- Adicionado MkDocs com fonte do portfólio em Markdown; site ainda não publicado.
- Capturada a preferência por agentes sob governança humana: tarefas delimitadas podem ser delegadas; pesquisa subjetiva e decisões de prioridade permanecem supervisionadas.

### Limites
- CI ainda precisa executar e ter seu resultado inspecionado.
- O validador verifica propriedades objetivas; não substitui auditoria semântica.
- AGENTS.md não é universalmente reconhecido por todas as IAs.
- Não foram instalados agentes externos, ferramentas locais ou extensões.
- Nenhuma publicação, contato, despesa ou ação comercial ocorreu.

---

# Histórico de evolução — Prompt Vivo

## 2026-11-25 — Criação da arquitetura inicial

### Motivo
O usuário definiu a necessidade de um sistema de prompts e arquivos Markdown interligados, capaz de conduzir pesquisas em várias etapas, registrar resultados, criar novas instruções especializadas, melhorar seus próprios métodos e permitir continuidade entre chats sem reconstruir o processo manualmente.

### Estrutura criada
- README e arquitetura da pasta.
- CORE com princípios e hierarquia.
- MASTER_PROMPT para inicialização e retomada.
- Protocolo de execução e checkpoints.
- Método de pesquisa profunda.
- Padrão de evidências.
- Quality Gate.
- Protocolo de autoaperfeiçoamento.
- Memória e transferência entre chats.
- Template de execução.
- Seis fases reutilizáveis: escopo, cenário, demanda, validação, viabilidade e síntese.

### Decisões de arquitetura
- Cada pesquisa concreta terá uma pasta própria em `runs/`.
- O conhecimento reutilizável ficará separado dos dados específicos de cada execução.
- A IA poderá melhorar instruções e criar módulos, com níveis de mudança e aprovação para alterações centrais.
- A documentação será a memória persistente; o chat é uma sessão temporária.
- A estrutura deve ser adaptável a diferentes temas, sem pré-selecionar um modelo de negócio.

### Limitações reconhecidas
O Prompt Vivo não cria memória automática fora dos arquivos, não garante que todo chat tenha acesso ao GitHub e não executa trabalho entre sessões sem uma ferramenta que permita isso. A retomada depende de a IA conseguir ler os arquivos e salvar as alterações.

## Regra para novas entradas
Adicionar novas mudanças no topo, com data, motivo, arquivos afetados, impacto e forma de verificar se a melhoria funcionou.


## 2026-11-25 — Primeiro teste real: TOTALMENTE GRATUITA

- Criada execução PV-2026-11-25-TOTALMENTE-GRATUITA.
- Registrados plano, fontes, achados, questões abertas, handoff e síntese em elaboração.
- Criada política de cotas com reserva explícita e fallback permitido; percentual de 90% definido como meta de confiabilidade a medir, não promessa.
- O primeiro lote identificou hipóteses em serviços operacionais de dados/documentos/conteúdo, riscos de automação genérica, custos de dropshipping e taxas de marketplaces.
- Próxima iteração: aprofundar procura brasileira e verificar caminhos de aquisição/pagamento.

## 2026-11-25 — Governança adaptativa de fases

### Motivo
O usuário esclareceu que o Prompt Vivo precisa administrar dinamicamente a quantidade e a estrutura das fases: concluir uma fase sem inventar novas quando desnecessárias, mas também criar, modificar, dividir, mesclar, reordenar, pular ou reabrir fases quando a pesquisa exigir.

### Diagnóstico
O protocolo anterior permitia aprofundar, encerrar linhas e pesquisar em paralelo, mas não definia explicitamente o ciclo de vida completo das fases nem a obrigação de sincronizar o plano e o estado quando a arquitetura mudasse.

### Alterações
- Adicionada seção obrigatória de arquitetura adaptativa ao EXECUTION_PROTOCOL.md.
- Atualizado README para deixar claro que PHASE_00–PHASE_05 são modelos, não limite fixo.
- Toda run deverá manter PHASE_ARCHITECTURE.md para registrar decisões e versões da sequência.

### Governança
Ajustes locais na execução são permitidos dentro do escopo aprovado; mudanças no protocolo/CORE seguem aprovação humana. Esta alteração central foi autorizada pelo pedido explícito do usuário.

### Teste
Aplicar imediatamente na execução PV-2026-11-25-TOTALMENTE-GRATUITA ao iniciar PHASE_02_DEMAND.


## 2026-11-26 — Sistema de continuidade e histórico entre chats

### Motivo
O usuário pediu um mecanismo permanente para documentar atualizações do Kamikaze e recuperar contexto quando o limite de uma conversa acabar, permitindo abrir outro chat e continuar a pesquisa sem recontar o histórico.

### Diagnóstico
Já existiam BOOTSTRAP, RESUME_PACKET, RUN_STATE e MEMORY_HANDOFF, inspirados no mecanismo do NEXUS. Porém, faltava um log cronológico padronizado de sessões, um prompt de retomada pronto para copiar e um protocolo explícito de sincronização e confirmação de escrita. Também foram encontrados trechos com referências malformadas no BOOTSTRAP.

### Alterações
- Criado `CONTINUITY_SYSTEM.md` com camadas de estado, memória, histórico e retomada; protocolo de checkpoint; reconciliação de divergências; checklist de integridade.
- Criado `NEXT_CHAT_PROMPT.md` para copiar e colar em novo chat.
- Criados logs append-only global e por execução: `SESSION_LOG.md`.
- Reescrito `BOOTSTRAP.md` para corrigir referências, carregar o sistema, auditar estado e continuar.
- Atualizados MASTER_PROMPT, EXECUTION_PROTOCOL, MEMORY_AND_HANDOFF e README.
- Sincronizados operations/STATE e arquivos da execução ativa; registrada a entrada do usuário.

### Limites
O mecanismo não trabalha em segundo plano nem salva após a conversa terminar. Checkpoints devem ser feitos enquanto a sessão está ativa e dependem de acesso confirmado ao GitHub. O novo chat precisa ter acesso ao repositório.

### Verificação
Confirmar a existência dos arquivos e a leitura das atualizações no GitHub. A retomada futura deve testar o texto de NEXT_CHAT_PROMPT e verificar que não repete pesquisas concluídas.


## 2026-11-26 — acionador persistente de tráfego pago
- Criado `knowledge/PAID_TRAFFIC_MODULE_ACTIVATION.md` com protocolo de ativação por intenção explícita + confirmação, arquitetura modular, etapas/gates, skills, repositórios, compliance, segurança financeira e handoff esperado.
- Ampliado catálogo open source com 49 skills de marketing-skills e repositórios oficiais/auxiliares Google Ads, Meta Ads, MCP, n8n, reporting e Meridian.
- Atualizados `knowledge/README.md`, `BOOTSTRAP.md`, `NEXT_CHAT_PROMPT.md` e `CONTINUITY_SYSTEM.md` para descoberta de acionadores dormentes em novos chats.
- Nenhuma integração, instalação, campanha ou gasto autorizado/executado.


## 2026-11-26 — pesquisa de construção com IA e ferramentas gratuitas
- Criado `knowledge/MAK_ZERO_COST_AI_BUILD_CASES.md` com casos, arquitetura, custos declarados e restrições dos planos gratuitos.
- Criado suplemento de fontes S436–S450: `runs/PV-2026-11-25-TOTALMENTE-GRATUITA/SOURCE_LEDGER_SUPPLEMENT_S436_S453.md`.
- Atualizados PHASE_03.5, FINDINGS, RUN_STATE, RESUME_PACKET, USER_INPUT_LOG, logs e operations/STATE.
- Nenhuma ferramenta foi instalada ou executada; nenhum app, conta, deploy ou gasto foi realizado.


## 2026-11-26 — serviços tecnológicos locais e prospecção
- Criado `knowledge/MAK_LOCAL_AI_SOLUTIONS_AND_LEAD_ENGINE.md` com diagnóstico por maturidade, ofertas por vertical, modelo implantação/manutenção, lead engine, LGPD/WhatsApp, pilotos e portfólio.
- Criado `runs/PV-2026-11-25-TOTALMENTE-GRATUITA/SOURCE_LEDGER_SUPPLEMENT_S454_S466.md`.
- Atualizados PHASE_03.5, FINDINGS, RUN_STATE, RESUME_PACKET, USER_INPUT_LOG e logs.
- Nenhum contato ou gasto realizado.
