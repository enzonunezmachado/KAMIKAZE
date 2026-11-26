## 2026-11-26 — Preocupação com excesso de pesquisa e momento de testar

**Entrada:** o usuário questionou se o Kamikaze pode estar pensando/pesquisando demais em vez de colocar uma hipótese suficientemente preparada em prática. Não quer testar ideias aleatórias sem critério, mas também não quer esperar por uma certeza impossível nem confundir pesquisa pública com prova de conversão.

**Aplicado:** QUALITY_GATE, RESEARCH_METHOD e EXECUTION_PROTOCOL ganharam um gate explícito entre pesquisa e experimento. Distinguir fatos que podem ser pesquisados de comportamento que exige teste; avaliar valor da informação; definir hipótese, comprador, oferta, canal, métrica, critério de sucesso/interrupção, custo, risco e autorização.

**Regra:** não usar "60% de chance" como número inventado. Usar níveis de evidência e prontidão; quando a próxima pesquisa não puder mudar a decisão e um experimento pequeno, ético, reversível e autorizado puder responder melhor, parar de pesquisar e recomendar o teste. Nenhuma ação externa foi autorizada nesta entrada.

## 2026-11-26 — Auditoria e melhoria da arquitetura documental e agentes

**Entrada:** o usuário pediu que a comparação com Spec Kit, BMAD, AGENTS.md, LangChain e Diátaxis fosse aplicada ao Kamikaze, com revisão de arquivos/pastas, READMEs obrigatórios, leitura progressiva, regras claras de gravação, redução de resumos extensos e validação automática de sincronização. Também pediu teste de MkDocs com portfólio escrito em Markdown, registro de Diátaxis e Obsidian no NEXUS, e pesquisa futura de agentes gratuitos mantendo controle humano.

**Interpretação:** melhorar a arquitetura existente sem migrar cegamente para framework externo; separar fonte canônica, snapshot, resumo e histórico; usar agentes somente quando a tarefa for delimitada e verificável; preservar participação humana em decisões subjetivas.

**Aplicado:** governança documental, AGENTS, README por níveis operacionais, state.toml, snapshots compactos, arquivos históricos preservados, validador Python, GitHub Actions, MkDocs e esqueleto de portfólio Markdown. Proposta Diátaxis/Obsidian registrada em NEXUS-DOCUMENTACAO.

**Limites:** CI ainda pendente; site não publicado; nenhuma integração Obsidian, código Android, agente externo, contato ou gasto realizado. O mecanismo verifica propriedades objetivas, mas não pode garantir que qualquer IA leia/obedeça arquivos sem suporte do ambiente.

# USER INPUT LOG — PV-2026-11-25-TOTALMENTE-GRATUITA

Este arquivo registra comentários, correções, preferências, decisões e autorizações do usuário que alterem a execução. Não é transcrição integral de chat; é um registro operacional resumido e rastreável.

| Data | Entrada do usuário | Impacto operacional | Status |
|---|---|---|---|
| 2026-11-25 | Pediu controlador adaptativo: ao dizer "próxima/continua", a IA deve auditar a fase e decidir se continua, aprofunda, cria subfase ou avança, sem exigir que o usuário escolha numeração. | PHASE_CONTROL.md; arquitetura adaptativa; auditoria de gate antes de cada transição. | APLICADO |
| 2026-11-25 | Pediu que o número e a estrutura das fases sejam administrados pela IA, sem limite fixo; não criar subfase por simetria ou burocracia. | EXECUTION_PROTOCOL.md e PHASE_ARCHITECTURE.md devem preservar histórico e permitir dividir, mesclar, reabrir e encerrar fases. | APLICADO |
| 2026-11-25 | Esclareceu que comentários e observações entre respostas podem influenciar o que será pesquisado e a decisão da próxima fase; depois pode simplesmente dizer "próxima". | Feedback da conversa deve ser interpretado como entrada de escopo/prioridade/critérios, comparado com decisões anteriores e registrado antes da próxima execução. | APLICADO |
| 2026-11-25 | Pediu que um novo chat consiga retomar a execução anterior com contexto completo: projeto, build/execução, pesquisa atual, fases, trabalho construído, evidências e próximo passo. | Criado BOOTSTRAP.md e RESUME_PACKET.md; MASTER_PROMPT e protocolo de handoff devem exigir reconstrução contextual e auditoria de divergências. | APLICADO |
| 2026-11-25 | Solicitou releitura do repositório e continuidade da fase em execução, sem reiniciar o trabalho. | Fazer bootstrap a partir dos arquivos atuais; continuar PHASE_03.1 se o controlador confirmar. | EM EXECUÇÃO |

| 2026-11-25 | Autorizou continuidade após a criação do protocolo de retomada, sem acrescentar nova restrição temática. | Continuar PHASE_03.1 conforme PHASE_CONTROL; comentários futuros continuam podendo alterar escopo e método. | APLICADO |
| 2026-11-25 | Pediu pesquisas mais profundas e autorizou dedicar mais tempo, sem priorizar velocidade; ressaltou que é iniciante, não tem experiência profissional e que reuniões/ambientes de mercado podem exigir credibilidade e postura que ainda precisa desenvolver. | Adotar padrão de pesquisa aprofundada e adaptativa; incluir adequação ao operador, curva de aprendizagem, prova de capacidade, credibilidade honesta, preparação para reuniões, risco, requisitos legais/idade e progressão de baixo risco em toda avaliação de oportunidade. Não presumir experiência nem recomendar fingir autoridade. | APLICADO |

| 2026-11-25 | Autorizou continuar PHASE_03.1 após confirmar as alterações documentais. | Continuar conforme PHASE_CONTROL; executar pesquisa aprofundada e registrar evidências/contraprovas em S076+; não avançar mecanicamente. | APLICADO |
\n| 2026-11-25 | Corrigiu a idade: tem 18 anos, não 16. Também esclareceu que tem capacidade/disposição para aprender e desempenhar o que for necessário; não quer que ausência de experiência profissional seja interpretada como incapacidade. | Corrigir documentação; invalidar restrições pessoais baseadas em menoridade; reavaliar plataformas que exigem 18 anos. Avaliar capacidade por tarefa e demonstração prática, sem descartar automaticamente por falta de histórico. | APLICADO |\n

| 2026-11-25 | Autorizou continuar a pesquisa após corrigir idade e capacidade. | Executar nova rodada de pesquisa em trabalho de bastidores, oportunidades de entrada e pagamento; registrar S087–S100 e manter controlador adaptativo. | APLICADO |

| 2026-11-25 | Pediu continuidade da execução (“Pode continuar”). | O controlador manteve PHASE_03.1 e abriu investigação adicional de oportunidades de tarefas remotas e validação de pagamento/privacidade; rodadas 8–12, fontes S105–S129. | APLICADO |

## 2026-11-25 — retomada em novo chat e preferência de entrega consolidada
- **Entrada:** usuário solicitou executar obrigatoriamente BOOTSTRAP.md, reconstruir contexto e continuar exatamente do ponto correto; mantém-se a preferência expressa nesta conversa de receber a pesquisa completa de uma vez, sem pequenas atualizações por subpesquisa.
- **Classificação:** instrução de continuidade + preferência de comunicação.
- **Impacto:** bootstrap integral executado; pesquisa continuada em fluxo único; nenhuma mudança na meta, orçamento ou autorizações externas.
- **Arquivos afetados:** RESUME_PACKET.md, RUN_STATE.md, MEMORY_HANDOFF.md, PHASE_CONTROL.md, SOURCE_LEDGER.md, FINDINGS.md, OPEN_QUESTIONS.md.
- **Status:** APLICADO.


## 2026-11-25 — rejeição Hub Data e nova orientação de pesquisa
- **Entrada:** usuário rejeitou a Hub Data por não querer filmar/registrar tarefas domésticas para produzir dados de IA. Disse que aceita criar/gravar conteúdo voluntariamente, mas expressou dúvidas sobre leitura de manhua por duração, inglês e voz/IA. Pediu continuidade da pesquisa focada online, reflexão honesta sobre competitividade e relatório intermediário sem conclusão definitiva.
- **Classificação:** preferência/limite pessoal + nova hipótese + orientação estratégica.
- **Impacto:** Hub Data = REJECTED_BY_USER; não insistir. Manhua reading = hipótese investigada e não priorizada por copyright/reused content. Aumentar investigação de serviços online específicos, operação/WhatsApp, pesquisa comercial e conteúdo original. Preparar relatório de situação.
- **Comunicação:** entregar consolidação em bloco, sem interrupções por subpesquisa.
- **Status:** APLICADO.


## 25/11/2026 — ampliação de segmentação de compradores (APLICADO)
**Entrada:** o usuário quer investigar todos os públicos com os quais possa aprender a lidar: pessoas físicas, profissionais independentes, pequenos negócios e empresas. Observou que empresas podem pagar mais, mas exigem autoridade, confiança e prova; negócios pequenos podem ter problemas digitais/operacionais e comprar implantação + manutenção; isso é hipótese, não garantia de aquisição. O usuário não quer assumir que consegue converter automaticamente um comércio local nem que empresas aceitam qualquer fornecedor.

**Impacto:** ampliar a pesquisa além da lista de serviços e avaliar quem compra, por que compra, como descobre fornecedores, que prova exige, quanto paga, quão acessível é a aquisição e se existe recorrência verdadeira. Todos os segmentos serão pesquisados; a seleção final será por evidência e capacidade de execução, não por preferência prévia. Exemplos de site, manutenção mensal e pesquisa recorrente permanecem hipóteses.

**Arquivos:** PHASE_ARCHITECTURE, PHASE_CONTROL, RUN_STATE, RESEARCH_PLAN, FINDINGS, OPEN_QUESTIONS, VALIDATION_MATRIX, SOURCE_LEDGER, novo PHASE_03_2_BUYER_SEGMENTATION_AND_ACCESS, checkpoint 03.2, RESUME_PACKET, MEMORY_HANDOFF e operations/STATE.


## 2026-11-26 — crítica à amostra de evidência e retomada em novo chat
**Entrada:** “só uma pessoa??” e solicitação para iniciar novo chat, executar BOOTSTRAP, reconstruir todo o contexto e continuar sem repetir pesquisa concluída.
**Classificação:** CORREÇÃO DE PADRÃO DE EVIDÊNCIA + CONTINUIDADE.
**Impacto:** não tratar um caso isolado como evidência suficiente de comportamento de compra; ampliar a amostra com fontes independentes, separar compra/uso/renovação/reembolso/satisfação e buscar sinais de retenção. Executar auditoria de estado antes de continuar.
**Status:** APLICADO na Rodada 21 (S227–S244); documentação sincronizada.
**Arquivos afetados:** PHASE_03_3, SOURCE_LEDGER, FINDINGS, OPEN_QUESTIONS, VALIDATION_MATRIX, PHASE_CONTROL, RUN_STATE, RESUME_PACKET, MEMORY_HANDOFF, RESEARCH_PLAN, PHASE_ARCHITECTURE, operations/STATE.


## 2026-11-26 — restrições reais de construção e pedido de portfolio de ideias
**Entrada:** usuário reforçou que devemos pesquisar amplamente e depois filtrar; recursos principais são ChatGPT, Google AI Studio e construtores gratuitos; está desenvolvendo NEXUS no mesmo ecossistema; não possui capital disponível; citou compromissos de R$200 no cartão e R$140 com a mãe, datas de fechamento/vencimento no ciclo, e corrigiu que os R$60 não devem ser tratados como verba livre. Pediu várias ideias diferentes, não uma solução escolhida antecipadamente.
**Impacto:** manter exploração ampla dentro do mercado freelancer; apresentar portfolio de hipóteses e filtrar somente depois da pesquisa. Orçamento operacional R$0, limite do cartão não é capital, R$60 não é verba autorizada. Proteger transporte/compromissos e não gastar sem aprovação. Não assumir disponibilidade de slot no Google AI Studio por uso concomitante com NEXUS; verificar quotas/slots antes de deploy. Priorizar ferramentas estáticas/local-first e evitar API/backend até necessário.
**Status:** APLICADO na Rodada 22 (S245–S285); documentação sincronizada.


## 2026-11-26 — visão ampliada de aquisição, interesse e afiliados
**Entrada:** usuário esclareceu que visualizações podem sinalizar interesse mesmo sem compra; seguidores iniciais são um indicador intermediário relevante, desde que avaliados em relação ao período e à qualidade do público. Pediu reconstruir o mecanismo real que leva descoberta → interesse → confiança → clique/conversa → compra, sem descartar relatos apenas por falta de comprovação independente. Quer desenhar uma operação multicanal: perfis em redes, conteúdo adaptado, stories/publicações frequentes, participação legítima em grupos, distribuição ativa e facilitação/automação com modelos e IA. Também pediu priorizar a investigação de afiliação a produtos existentes com comissão interessante, em vez de exigir produto próprio.
**Classificação:** correção de modelo mental + expansão de escopo de aquisição + prioridade de hipótese afiliados.
**Impacto:** adotar funil de aquisição e métricas intermediárias; analisar views, visitas ao perfil, seguidores, salvamentos, comentários, cliques, conversas, leads e vendas em conjunto, com janela temporal e origem. Não tratar views como venda nem como sinal vazio. Investigar afiliados como rota de baixo custo com atenção a qualidade do produto, comissão líquida, aprovação, atribuição/cookies, reembolso, payout, materiais permitidos e canais reais de distribuição. Desenhar uma operação multicanal com rotina sustentável e facilitação, sem automação abusiva, spam, perfis falsos ou autopromoção proibida.
**Arquivos afetados:** PHASE_03.4, nova PHASE_03.5_ACQUISITION_ENGINE_AND_AFFILIATE_VALIDATION, SOURCE_LEDGER, FINDINGS, OPEN_QUESTIONS, VALIDATION_MATRIX, RUN_STATE, PHASE_CONTROL, RESUME_PACKET, MEMORY_HANDOFF e operations/STATE.
**Status:** APLICADO PARCIALMENTE; rodada de pesquisa afiliados e mecanismos de aquisição continua.


## 2026-11-26 — mecanismo de indicação por relacionamento e pesquisa GitHub
**Entrada:** usuário propôs abordar profissionais que atuam no público relacionado ao produto, apresentar a solução com contexto honesto do projeto e ouvir sua opinião. Se a pessoa não tiver interesse/necessidade, explorar se conhece alguém que possa se beneficiar e pedir uma introdução voluntária; o objetivo é criar oportunidades por confiança e reciprocidade, não parecer uma venda insistente. Também pediu pesquisar projetos públicos no GitHub por affiliate/afiliado, marketing digital e automação com IA para reutilizar componentes úteis na operação.
**Classificação:** hipótese de aquisição por relacionamento/indicação + solicitação de pesquisa técnica open source.
**Impacto:** criar mecanismo de referral-by-introduction com disclosure de comissão, consentimento, pedido sem pressão e sem coletar contatos de terceiros sem autorização. Oferecer uma mensagem encaminhável para a pessoa compartilhar; não condicionar ajuda a compra/indicação nem explorar culpa/obrigação. Auditar repositórios por licença, atividade, código real, dependências, APIs, custos, segurança, manutenção e aderência ao MAK; não instalar, executar ou importar sem auditoria e aprovação.
**Fontes:** S394–S398.
**Status:** APLICADO NA DOCUMENTAÇÃO; pesquisa de repositórios continua.



## 2026-11-26 — estudo aprofundado do Affitor/affiliate-skills e expansão do MAK
**Entrada:** usuário autorizou estudar profundamente o primeiro repositório recomendado (Affitor/affiliate-skills), examinar seus arquivos e adaptar ao projeto Kamikaze os elementos que realmente agreguem valor; também aprovou incorporar a estratégia de relacionamento e memória de marca descrita na conversa.
**Classificação:** autorização de pesquisa documental e atualização do repositório Kamikaze; expansão conceitual do MAK.
**Impacto:** criar estudo técnico/estratégico próprio, mapear padrões úteis, registrar limitações/contraprovas, adaptar a arquitetura modular e o flywheel, e acrescentar o ciclo de relacionamento/memória de marca. Não instalar, clonar, executar, importar código, criar contas, publicar ou contatar terceiros.
**Status:** APLICADO NA DOCUMENTAÇÃO; implementação operacional e validação comercial continuam pendentes.

| 2026-11-26 | Pediu pesquisar e construir dados para as ressalvas identificadas no estudo Affitor: divergência de contagem e skills canônicas, métricas/proxies, heurísticas de plataforma, evidência dos casos numéricos, disclosure brasileiro e claims de urgência/bônus/garantia. | Criada auditoria documental aprofundada em knowledge/MAK_AFFITOR_EVIDENCE_AND_GOVERNANCE.md; fontes S403–S413; regras incorporadas à PHASE_03.5 e à governança do MAK. | APLICADO |

| 2026-11-26 | Pediu criar mecanismo para documentar as atualizações do Kamikaze e recuperar o contexto após o limite do chat, permitindo abrir outra conversa, colar um prompt e continuar a pesquisa automaticamente, como no mecanismo de continuidade do NEXUS. | Criados CONTINUITY_SYSTEM.md, NEXT_CHAT_PROMPT.md e SESSION_LOGs global/da execução; reescrito BOOTSTRAP; atualizados MASTER_PROMPT, EXECUTION_PROTOCOL, MEMORY_AND_HANDOFF, README, CHANGELOG, operations/STATE, RUN_STATE, RESUME_PACKET e PHASE_CONTROL. Checkpoint obrigatório após lotes e antes de transferência; novo chat deve auditar e continuar sem reiniciar. | APLICADO |


## 2026-11-26 — pedido para executar NEXT_CHAT e catalogar skills/repositórios
**Entrada:** usuário confirmou que basta pedir para ler o repositório do Kamikaze para localizar e executar NEXT_CHAT_PROMPT; pediu executar retomada, preparar a adição/listagem das skills Affitor e dos outros repositórios estudados, permitindo uma resenha.
**Classificação:** instrução de continuidade + pedido de inventário técnico e resenha crítica.
**Impacto:** executar NEXT_CHAT/BOOTSTRAP, conferir estado ativo e criar catálogo centralizado com as 53 skills Affitor e os outros repositórios estudados. Distinguir referência, adaptação proposta e código efetivamente adotado. Não importar/instalar/executar sem autorização.
**Status:** APLICADO NA DOCUMENTAÇÃO; nenhuma skill de terceiros foi importada ou executada.


## 2026-11-26 — pedido para criar acionador futuro de implementação de tráfego pago
**Entrada:** usuário pediu um mecanismo persistente que reconheça quando decidir implementar tráfego pago; antes de iniciar, apresentar o que será criado, organização, etapas, skills, repositórios e manual/handoff final. Quer módulo completo e bem estruturado, com integração à filosofia Kamikaze somente se fizer sentido; filosofia e arquitetura devem ser reavaliadas no futuro.
**Interpretação:** "assinador" foi entendido como **acionador** (gatilho de ativação). Menções exploratórias não devem ativá-lo.
**Decisão:** criar `MAK-PAID-TRAFFIC-MODULE` em estado DORMANT / DOCUMENTED / NOT IMPLEMENTED. Quando houver intenção clara, apresentar o pacote e pedir confirmação explícita para começar Etapa 0. Etapa 0 é planejamento, não autorização de gasto ou ação externa. Cada campanha, conexão, publicação e gasto exigirá autorização própria.
**Escopo registrado:** arquitetura modular, etapas e gates, checklist de prontidão, skills, repositórios, compliance/privacidade, segurança financeira, simulação e handoff final.
**Status:** blueprint e acionador persistidos. Nenhum módulo implementado, código de terceiros importado, conta criada/conectada, anúncio publicado ou gasto realizado.


## 2026-11-26 — pedido para continuar pesquisa de construtores com IA e ferramentas gratuitas
**Entrada:** usuário perguntou se há histórico de pessoas que construíram totalmente gratuitamente com IA e ferramentas poderosas; após primeira amostra, pediu continuidade.
**Interpretação:** aprofundar casos com artefatos funcionais, stacks, ferramentas, custo real/alegado, evidência de uso/receita e restrições de planos gratuitos; não apenas listar AI builders.
**Aplicado:** estudo de Stockroom/AppJet, MyClaw Tools, Somnia, Toolkiya, HookLayer, RenderArchi, AssetShark e HypeDesk; revalidação de planos Gemini, Supabase, Cloudflare, Vercel e GitHub Copilot. Criados documentos de casos e suplemento de fontes S436–S450.
**Limites:** não instalar, clonar, executar, conectar contas, criar/deployar apps, publicar ou gastar; preservar NEXUS e quota do AI Studio.
**Status:** pesquisa documental persistida; nenhuma implementação ou experimento comercial autorizado.


## 2026-11-26 — hipótese de serviços tecnológicos personalizados para negócios locais
**Entrada:** usuário sugeriu pesquisar a obtenção de telefones de negócios regionais (Maps/diretórios), diagnosticar maturidade digital e oferecer soluções de IA/tecnologia proporcionais (ex.: site/cardápio simples para pizzaria), com implantação competitiva e manutenção fixa. Quer fechar primeiro cliente e criar projetos de portfólio.
**Interpretação:** investigar motor de leads, diagnóstico por maturidade, ofertas verticais, modelo recorrente, LGPD/WhatsApp/Google Maps e primeiros candidatos regionais; não executar contato.
**Aplicado:** documentada hipótese e processo; lista exploratória de pizzarias de Taboão; restrições de scraping/WhatsApp; arquitetura de demos e preços como hipóteses.
**Limites:** sem mensagens, ligações, visitas, cadastro, publicação, instalação, deploy ou gastos.



## 2026-11-26 — estrutura de lotes de 20 empresas, ranking e CRM documental
**Entrada:** usuário propôs pesquisar grupos de 20 empresas, ranquear as oportunidades, registrar quais foram contatadas, não contatadas e por quê; impedir que empresas já documentadas reapareçam como novas em rodadas futuras; permitir reavaliação futura de empresas sem recusa definitiva; manter status de contato/venda/implantação e arquivos separados por empresa/projeto, com custos, receita pontual e mensalidades.
**Interpretação:** criar uma estrutura documental própria, com registro mestre e IDs únicos, snapshots imutáveis por lote, dossiês individuais, taxonomia de status multidimensional, histórico de contato/permissão/supressão, projetos, contratos recorrentes e ledger financeiro.
**Aplicado:** criada a estrutura `operations/COMPANY_SOLUTIONS/`, com templates e playbooks. Dois rankings separados (Conversion Fit e Business Value Fit), score heurístico com confidence/coverage e gates de elegibilidade. Regras de deduplicação, reavaliação, opt-out, protótipos e aceites.
**Limites:** documentação criada, mas módulo não ativado; nenhuma empresa inserida, pesquisa de lote, contato, protótipo específico, proposta, venda, contrato, deploy ou gasto realizado. Orçamento operacional permanece R$0.


## 2026-11-26 — atualização automática do ponteiro de trabalho
**Entrada:** o usuário pediu que a atualização do projeto aponte automaticamente para a última linha/entrega desenvolvida ou atualizada.
**Interpretação:** instituir um ponteiro canônico único, atualizado em cada checkpoint substantivo, e fazer bootstrap, prompt de novo chat e estado operacional consultarem esse ponteiro em vez de manterem focos independentes.
**Aplicado:** criado `PROMPT_VIVO/CURRENT_WORK.md`; atualizados BOOTSTRAP, CONTINUITY_SYSTEM, NEXT_CHAT_PROMPT e operations/STATE. O ponteiro distingue última entrega substantiva da fase principal de pesquisa.
**Limite técnico:** a atualização é automática como regra obrigatória do fluxo de checkpoint durante uma sessão ativa; não há execução em segundo plano depois que o chat termina. A gravação só é considerada concluída após confirmação do GitHub.
