# Pesquisa de agentes e produção com custo zero

**Data de consulta:** 25/11/2026  
**Escopo:** ferramentas gratuitas para pesquisar mercado, coordenar agentes e produzir entregáveis com R$ 0.  
**Status:** pesquisa documental e de fontes públicas; nenhuma ferramenta foi instalada ou executada nesta sessão.

## Resumo executivo

A melhor hipótese de stack para o Projeto Sem Nome é:

1. **Google Antigravity (desktop ou CLI `agy`) como ambiente de execução principal**, se o computador suportar. O plano Free inclui acesso ao CLI, skills, MCP e recursos do produto; a cota é semanal e variável, não ilimitada.
2. **Uma skill operacional nossa no repositório**, com instruções e estado em Markdown. Antigravity descobre skills e subagentes do workspace.
3. **Reddit Research MCP** como ferramenta complementar para pesquisa semântica no Reddit, quando conectado a um cliente MCP compatível e após OAuth.
4. **Pain Miner** como coletor batch complementar de Reddit, Hacker News e V2EX, sem chave de API no fluxo padrão; testar primeiro o diagnóstico de fontes.
5. **Google AI Studio / Gemini API Free** para tarefas pontuais e protótipos, respeitando os limites e as regras de privacidade do nível gratuito.
6. **GitHub como memória e trilha de auditoria**, não como runtime de agentes.
7. **Pesquisa manual e contato humano** para validar intenção de compra. Nenhum agente consegue provar que um comprador vai pagar sem um teste comercial.

Não recomendo começar por CrewAI, LangGraph, Dify, Flowise, OpenHands, n8n ou Ollama. São componentes úteis, mas aumentam a implantação e não resolvem o principal gargalo: encontrar compradores e validar uma oferta.

## 1. Atenção ao nome BitChat

A pesquisa encontrou dois produtos distintos com nomes muito parecidos:

### bitChat da bitbybit Studio
Site: https://bitbybit.studio/bitchat/

É um agente de atendimento e comércio para WhatsApp, Instagram, Facebook, TikTok e web, conectado a dados de loja/Shopify. A página descreve respostas baseadas em catálogo e pedidos, criação de carrinho, consulta de entrega e transferência para humanos com contexto. O produto tem um AI Studio para construir, testar e implantar agentes.

A tabela pública de preços mostra um plano Free para bitChat com 100 respostas de IA/mês, 100 tickets/mês, até 3 atendentes humanos, AI Studio, skillsets de IA e base de conhecimento com 50 documentos. O plano é gratuito, mas tem limites e é orientado a atendimento comercial; não é um ambiente geral de agentes para pesquisar mercado, navegar livremente e produzir qualquer projeto. O uso com Shopify/WhatsApp também pode envolver dependências e taxas externas.

Fonte: https://bitbybit.studio/pricing/ (seção bitChat, linhas 539–568 da página consultada); https://bitbybit.studio/bitchat/

### BitChat brasileiro — bitchat.com.br
Site: https://www.bitchat.com.br/

É uma plataforma de atendimento multicanal e automação de WhatsApp para empresas, com o produto IABit. A página consultada anuncia teste de 7 dias e planos pagos; o plano Pro é anunciado por R$ 400/mês. Portanto, não é uma plataforma geral de agentes de produção gratuita e contínua.

Fonte: https://www.bitchat.com.br/

**Conclusão:** se o usuário quis dizer bitChat da bitbybit, vale testar o plano gratuito como ferramenta para um futuro produto de atendimento a clientes, mas não como nosso cérebro central. Se quis dizer o BitChat brasileiro, não atende à restrição de custo zero contínuo.

## 2. Melhor candidato: Google Antigravity

Site e documentação:
- https://antigravity.google/
- https://antigravity.google/docs/home
- https://antigravity.google/docs/subagents
- https://antigravity.google/docs/browser
- https://antigravity.google/docs/plans
- https://antigravity.google/download

### O que oferece
- Aplicativo desktop e CLI `agy`.
- Skills de projeto em Markdown.
- MCP e regras de comportamento.
- Subagentes paralelos com papéis e permissões.
- Agentes personalizados em `.agents/agents/<nome>.md`.
- Skills de workspace em diretórios de skills.
- Navegador para abrir páginas, clicar, preencher, testar interfaces e inspecionar erros, sujeito à superfície/versão/conta.
- Painel `/agents` para monitorar agentes.
- `/swarm` para coordenar agentes em um quadro compartilhado.
- Ações e execução de código no workspace, com permissões e sandbox.

### Gratuito de verdade?
O plano Free custa US$ 0 e inclui CLI, funcionalidades-base, skills, MCP e recursos de agentes. A documentação informa uma cota significativa renovada semanalmente, acesso a modelos específicos e limite semanal. A cota é baseada no trabalho executado; tarefas complexas consomem mais. Limites e modelos podem mudar. Não é uso infinito.

A documentação indica:
- `/swarm`: disponível em todos os planos, inclusive Free.
- `/teamwork` e `/boost`: planos pagos.
- Browser integrado no Antigravity App para contas pessoais Free está em rollout a partir da versão 2.30.0; disponibilidade precisa ser conferida na instalação.
- CLI `agy` pode usar Chrome local via Chrome DevTools MCP para navegação, exigindo Chrome recente e autorização de depuração.

### Como isso se encaixa no projeto
Antigravity é a melhor opção pesquisada para ser o ambiente de trabalho do agente: lê o repositório, executa comandos, edita arquivos, chama MCP e delega pesquisa/produção. O repositório vira contexto operacional versionado, e a skill define o método.

### Riscos e limites
- Cota gratuita semanal: não planejar uma operação que dependa de agentes rodando sem parar.
- Agentes paralelos consomem mais recursos e podem duplicar trabalho.
- Subagentes não herdam automaticamente o histórico inteiro da conversa principal; cada tarefa precisa receber contexto suficiente.
- Browser e acesso a contas exigem permissões; login e ações sensíveis devem continuar sob controle humano.
- A ferramenta pode mudar de versão, disponibilidade e quota.
- O uso no computador do usuário não foi testado nesta pesquisa.

### Instalação oficial no Windows
PowerShell:
```powershell
irm https://antigravity.google/cli/install.ps1 | iex
agy --version
```
App desktop: baixar em https://antigravity.google/download e instalar no Windows 10/11 64-bit.

Fonte oficial: https://antigravity.google/docs/plans/ ; https://antigravity.google/docs/subagents ; https://antigravity.google/docs/browser ; https://antigravity.google/docs/cli-getting-started

## 3. Comparação de ferramentas

| Ferramenta | O que é | Software gratuito? | Modelo/infra grátis? | Fit agora |
|---|---|---:|---:|---|
| Google Antigravity | Ambiente agente desktop/CLI com subagentes, skills, MCP e browser | Sim, plano Free | Cota semanal gratuita, limitada | **Muito alto** |
| Gemini CLI tradicional | Agente terminal anterior | Código aberto, mas acesso individual mudou | Free individual foi direcionado ao Antigravity CLI em junho/2026; verificar conta | Baixo para nova instalação |
| Google AI Studio / Gemini API | Playground e API para protótipos e chamadas | Sim | Modelos selecionados com limites Free | Alto como complemento |
| Reddit Research MCP | Servidor MCP para busca e coleta no Reddit | MIT; servidor standalone declarado gratuito | Usa serviço hospedado e OAuth; não é modelo de IA | Alto como ferramenta de pesquisa |
| Pain Miner | CLI Python + skill para mineração de dores | MIT | Coleta pública sem chave no fluxo padrão; análise depende do agente | Alto como coletor |
| smolagents | Framework Python de agentes com ferramentas | Apache 2.0 | Modelos locais ou inference API com limites; hardware/modelo à parte | Médio, para futura automação própria |
| LangGraph | Framework de workflows/estado para agentes | MIT | Modelo e execução são responsabilidade nossa | Médio, excessivo agora |
| CrewAI | Framework de equipes de agentes | Gratuito/open source no núcleo | Modelo e infraestrutura à parte | Médio, excessivo agora |
| Microsoft Agent Framework | Framework unificado de agentes e workflows | Open source | Modelo e execução à parte | Baixo agora; bom para produto técnico futuro |
| AutoGen | Framework multiagente anterior da Microsoft | Open source | Modelo e infraestrutura à parte | Não iniciar projeto novo sem avaliar migração para Agent Framework |
| OpenHands | Agente de engenharia de software | MIT core | Precisa modelo forte; local exige hardware ou API | Baixo no hardware atual |
| Dify | Plataforma visual para aplicações e workflows de IA | Community self-hosted | Hospedagem/modelo ficam conosco; licença tem condições próprias | Baixo agora |
| Flowise | Builder visual de agentes e fluxos | Open source, self-hosted | Modelo e servidor à parte | Baixo agora |
| n8n Community | Automação de workflows com nós de IA | Community Edition self-hosted gratuita | Precisa máquina/servidor e modelo; licença SUL limita certos usos como serviço | Médio mais tarde |
| Ollama | Runtime local para modelos abertos | Sim | O custo é hardware/energia/armazenamento | Baixo no computador atual |

### Notas essenciais
- **Open source não significa IA gratuita.** CrewAI, LangGraph, smolagents, Dify e Flowise são ferramentas de orquestração; ainda precisam de modelo, servidor e conectores.
- **Ollama é gratuito, mas exige hardware.** A documentação indica 8 GB de RAM disponível como referência mínima para modelos 7B, 16 GB para 13B e 32 GB para 33B. Não é a rota indicada para um computador com 4 GB de RAM.
- **OpenHands** pode usar Ollama ou LM Studio, mas sua própria documentação alerta que modelos locais podem ter limitações e que fluxos de codificação exigem modelos e hardware capazes.
- **n8n** é gratuito para self-hosting e uso interno/serviço operado para clientes sob condições específicas; não pode ser tratado como base livre para revender hospedagem do editor ou dar aos clientes acesso para configurar automações sem licença comercial.
- **Dify** Community é gratuito para self-hosting, mas a licença e os termos comerciais devem ser revisados antes de embutir em produto comercial.
- **Flowise** permite construir single-agent, multi-agent e workflows visualmente, mas precisa de servidor e modelo. Não é necessário para começar.

Fontes:
- Antigravity: https://antigravity.google/docs/plans/ ; https://antigravity.google/docs/subagents
- Gemini API: https://ai.google.dev/gemini-api/docs/pricing
- smolagents: https://huggingface.co/docs/smolagents/
- Ollama: https://ollama.com/download e https://ollama.readthedocs.io/en/quickstart/
- OpenHands: https://github.com/OpenHands/docs/blob/main/openhands/usage/llms/local-llms.mdx
- Flowise: https://docs.flowiseai.com/
- Dify: https://dify.ai/pricing
- n8n: https://docs.n8n.io/hosting/ e https://support.n8n.io/article/can-i-use-your-license-for-my-use-case

## 4. O que as pessoas relatam sobre o uso de agentes

### Caso 1 — operação solo organizada em um repositório
Thread: https://www.reddit.com/r/AI_Agents/comments/1uyoahi/i_have_run_a_oneperson_company_on_ai_agents_for_6/

Um autor descreve seis meses operando marketing, CRM, conteúdo e prospecção com agentes, organizados em um único repositório. Diz ter fechado dois leads frios e afirma receita de cinco dígitos, mas nos comentários esclarece que vende um sistema de marketing para pequenas agências/startups e que ainda depende principalmente de indicações. O stack citado inclui Claude Code, Neon/Postgres, ferramentas próprias de navegador/CLI, Google Workspace CLI, Apify e Cloudflare Workers — portanto não é um exemplo de operação integralmente gratuita.

Aprendizados úteis:
- Um agente generalista + playbooks bem escritos pode superar vários bots especializados em tarefas comuns.
- Subagentes só devem ser usados quando a tarefa realmente precisa de paralelismo; o autor estima consumo de tokens muitas vezes maior.
- O repositório pode funcionar como memória legível e gravável.
- Ações externas devem passar por fila de aprovação humana.
- Leads e engajamento não são compradores: o autor relata que seu pipeline de engajamento trouxe quase nenhum comprador real.
- Automação pode falhar silenciosamente; cada fila precisa de um consumidor e monitoramento.
- O gargalo pode ser decidir e publicar, não gerar mais coisas.

Confiabilidade: relato detalhado e autocrítico, mas autodeclarado, stack não gratuito e faturamento não auditado. Útil como estudo de arquitetura, não como prova financeira.

### Caso 2 — experiência de uma agência de automação sem primeiro cliente
Thread: https://www.reddit.com/r/AiAutomations/comments/1osg4ml/started_my_ai_automation_agency_7_days_ago_built/

O autor diz ter construído 15–20 projetos e criado portfólio/site, mas ainda não tinha cliente após sete dias de prospecção em Fiverr, Upwork, LinkedIn e cold outreach. Comentários divergem: alguns relatam dificuldade de vender automação genérica; outros defendem visitar empresas, entender o problema e vender resultado em vez de vender “IA”.

Aprendizado: criar automações e portfólio não prova demanda; distribuição e conversa com compradores são parte central do produto.

Confiabilidade: relato pessoal com opiniões conflitantes; sem receita comprovada.

### Caso 3 — experiência com Antigravity Swarm
Thread: https://www.reddit.com/r/google_antigravity/comments/1xstsji/whats_your_experience_with_swarm/

Um usuário relata que uma tarefa complexa, com 14 arquivos editados, consumiu cerca de 3% da cota em um plano Pro usando modelo Flash. Outros comentam que a execução paralela acelera tarefas, mas pode consumir a cota rapidamente; um relato diz ter esgotado uma cota de cinco horas em aproximadamente 1,5 hora com 31 agentes em um plano Ultra.

Aprendizado: o Swarm existe e é utilizado, mas os números são anedóticos e de planos pagos. Não projetar consumo Free a partir desses relatos. Começar com 2–3 agentes e uma tarefa delimitada.

Confiabilidade: discussão recente de usuários, sem telemetria auditada.

## 5. Fontes de pesquisa de mercado gratuitas

| Fonte | O que extrair | Acesso/custo | Limitações |
|---|---|---|---|
| Reddit | Dor, improvisos, comparação, compra, comentários | Pesquisa pública/manual; MCP e Pain Miner complementam | Bloqueios, API/termos, regras de comunidade; não fazer spam |
| Hacker News | Ferramentas, problemas de devs, feedback técnico, Show HN | Algolia Search API pública, documentação indica até 10.000 requests/h/IP | Público enviesado para tecnologia e startups |
| GitHub Issues/Discussions | Bugs, pedidos de feature, workarounds e integrações | Busca pública e API com limites | Dor de dev não é automaticamente mercado pagante |
| Fóruns de nicho | Necessidades específicas de profissões/hobbies | Muitos são públicos | Busca fragmentada e regras próprias |
| Reviews de apps/marketplaces | Fricção, lacunas, preço, expectativas | Leitura pública | Review não comprova mercado ou vendas |
| Comunidades de suporte de software | Problemas recorrentes, falhas e limitações | Público em muitos produtos | Usuários podem ser poucos ou não ser compradores |
| YouTube comentários | Dúvidas e reclamações após tutorial/review | Público/manual | Ruído e dificuldade de quantificar |
| Reclame Aqui e avaliações públicas | Falhas de serviço e lacunas de atendimento | Parte pública | Não usar dados pessoais; uma reclamação isolada não é mercado |

Fontes:
- HN Algolia API: https://hn.algolia.com/api
- Reddit MCP: https://github.com/dialog-tools/reddit-research-mcp
- Pain Miner: https://github.com/AdvancingTitans/pain-miner

### Método de coleta recomendado
1. Descobrir 5–8 comunidades em áreas distintas.
2. Usar buscas com frases de dor e improviso, não só palavras de produto.
3. Abrir os posts originais e ler comentários/respostas.
4. Agrupar por tarefa/problema e contar autores independentes.
5. Procurar contraprovas e alternativas pagas.
6. Registrar URL, data, contexto, força de sinal e limites da amostra.
7. Nunca perguntar de forma genérica em comunidades que proíbem pesquisa de mercado. Observar discussões públicas e cumprir as regras locais.

## 6. Avaliação dos repositórios anteriores

| Repositório | Papel recomendado | Decisão |
|---|---|---|
| AdvancingTitans/pain-miner | Coletor batch de dores | Testar diagnóstico primeiro |
| dialog-tools/reddit-research-mcp | Pesquisa semântica e comentários no Reddit | Conectar ao Antigravity via MCP após verificar OAuth |
| datou202307-design/trend-opportunity-radar | Método de amostragem, contraprovas e trilha de evidências | Aproveitar processo; não instalar inicialmente |
| ferdinandobons/startup-skill | Pesquisa profunda de concorrência e estratégia | Guardar para depois; consumo de tokens elevado |
| theomarsoliman/business-ideas-dataset | Dataset e checklist | Usar só como referência; viés SaaS/US e rótulo “validated” não auditado |
| mkhanna-stack/venturemind-ai | Arquitetura local de embeddings/clustering | Não instalar; baixa adoção e licença a verificar |
| lignertys/reddit-research-skills | Playbooks de Reddit | Não adotar serviço pago/credencial como base |
| lefttree/reddit-pain-points | Dashboard de mineração | Não priorizar; modo demo usa dados fictícios e modo real exige chave LLM |
| huxm-git/reddit-idea-scout | PRAW + Claude API | Não atende R$ 0 |

## 7. Arquitetura recomendada: Projeto Sem Nome Opportunity OS

### Camada A — Interface e orquestração
**Antigravity** é o agente principal, responsável por interpretar a tarefa, escolher skill, delegar quando necessário e atualizar o repositório.

### Camada B — Agentes de função
Começar com três papéis, não nove agentes permanentes:

1. **Scout (descoberta):** encontra comunidades, posts e comentários. Não pontua ideias ainda.
2. **Analista crítico (evidência e contraprova):** agrupa dores, identifica autores independentes, concorrentes, preço, sinais S0–S4 e razões para não avançar.
3. **Builder/Comercial (oferta e teste):** só recebe oportunidades aprovadas; define uma oferta manual, protótipo mínimo, preço de teste, canal e roteiro de venda.

O agente principal atua como coordenador e auditor. Produção pode ser uma etapa separada do mesmo agente principal até haver necessidade real de delegar código/design.

### Camada C — Ferramentas
- Reddit Research MCP: descoberta e leitura profunda do Reddit.
- Pain Miner: coleta batch de Reddit/HN/V2EX.
- Navegador Antigravity: fontes adicionais, concorrentes, preços e validação visual.
- GitHub: arquivos, decisões, evidências e entregáveis.
- Google AI Studio: chamadas/experimentos de IA pontuais, não como memória central.
- Planilhas e documentos: primeira forma de entrega, sem servidor próprio.

### Camada D — Memória
O GitHub é a fonte da verdade:
- `research/`: evidências e auditorias.
- `opportunities/`: hipóteses e status.
- `experiments/`: ofertas e testes comerciais.
- `operations/STATE.md`: situação atual e próximo passo.
- `.agents/skills/`: instruções reutilizáveis.
- `.agents/agents/`: papéis de subagentes quando o setup Antigravity estiver disponível.

Não despejar todo o histórico em cada prompt. O agente deve ler README + STATE e abrir apenas os arquivos relevantes.

### Camada E — Aprovação humana
Agentes podem pesquisar, rascunhar e preparar. O usuário aprova:
- contato com prospect;
- publicação em rede/comunidade;
- envio de mensagem;
- alteração destrutiva;
- gasto, contratação ou assinatura;
- qualquer ação com dados pessoais ou compromisso comercial.

## 8. Fluxo operacional

```text
Pergunta de mercado
      ↓
Scout: mapa de comunidades e coleta
      ↓
Analista: dores + autores independentes + evidências
      ↓
Crítico: concorrentes + contraprovas + sinais comerciais
      ↓
Gate humano: vale testar?
      ↓
Builder: oferta manual / amostra / protótipo
      ↓
Comercial: contato individual e contextual
      ↓
Gate humano: preço e proposta aprovados
      ↓
Pagamento ou compromisso verificável?
      ↓
Entrega simples → feedback → registro → próxima iteração
```

## 9. Número de projetos simultâneos

| Estratégia | Vantagem | Risco | Decisão |
|---|---|---|---|
| 1 oportunidade | Foco e entrega mais rápida | Menos diversificação | Melhor para o primeiro ciclo |
| 2 oportunidades | Comparação e alguma diversificação | Troca de contexto | Aceitável após dois testes de oferta |
| 5 produtos construídos | Mais apostas em tese | Dispersão, manutenção, nenhum lançamento | Não recomendado |
| 5 oportunidades pesquisadas, 1–2 ofertas testadas | Amplitude na descoberta e foco na execução | Exige disciplina de gate | **Recomendado** |

Pesquisa pode cobrir cinco hipóteses; construção deve ser sequencial. Não produzir cinco coisas antes de conversar com compradores.

## 10. Oportunidades preliminares encontradas — não validadas

Os exemplos abaixo são pistas de pesquisa, não recomendações aprovadas.

### A. Limpeza e preparação de CSV/planilhas para pequenos negócios e profissionais contábeis
- **Público:** pequenos negócios, bookkeepers e profissionais que importam dados bancários ou operacionais.
- **Dor observada:** usuários relatam gastar horas limpando extratos, datas, descrições e CSVs antes de usar Excel/contabilidade.
- **Fontes:** https://www.reddit.com/r/smallbusiness/comments/1swxpjc/i_spend_hours_every_month_cleaning_bank/ ; https://www.reddit.com/r/smallbusiness/comments/1noa6lt/anyone_else_lose_their_mind_doing_bookkeeping/ ; https://www.reddit.com/r/QuickBooks/comments/1clti3u/unable_to_import_csv_due_to_numbers_in_the/
- **Sinal:** S2 (tempo gasto e improviso) e existência de ferramentas/alternativas. Não há compra comprovada nos relatos citados.
- **Oferta testável:** serviço manual de limpeza, padronização e validação de uma planilha/CSV, com amostra anonimizada e checklist. Evitar fazer escrituração ou aconselhamento contábil.
- **Custo inicial:** R$ 0 se arquivos forem tratados localmente com ferramentas gratuitas e sem armazenar dados sensíveis.
- **Validação:** conversar com profissionais, pedir arquivo fictício ou anonimizado, cotar um piloto pago pequeno. Não usar extratos reais sem acordo e proteção apropriada.
- **Contraprova:** soluções contábeis e importadores já existem; problema pode ser raro ou depender de integração específica.
- **Confiança:** baixa a média; relatos individuais, não estudo de frequência.

### B. Gestão de inventário de bundles para vendedores Etsy
- **Público:** artesãos/vendedores que vendem bundles com múltiplas variantes.
- **Dor observada:** vendedor com mais de 200 listings relata dificuldade de manter estoque correto quando compradores montam bundles; resposta sugere planilha manual ou centralização em Shopify.
- **Fonte:** https://www.reddit.com/r/EtsySellers/comments/15y1vcq
- **Sinal:** S2 (problema operacional e workaround) e alternativa paga citada (LitCommerce), sem prova de compra específica do produto.
- **Oferta testável:** planilha customizada de estoque por componentes/combinações, com regras e atualização manual; não construir integração antes de validar.
- **Custo inicial:** R$ 0 com planilha.
- **Validação:** localizar outros vendedores com catálogo complexo, descobrir frequência de erro e custo de ruptura, oferecer setup pago.
- **Contraprova:** marketplace tem regras e ferramentas de sincronização; solução pode ser coberta por Shopify/apps.
- **Confiança:** baixa; um caso específico e antigo.

### C. Curadoria e preparação de materiais pedagógicos
- **Público:** professores que compram recursos para poupar tempo de pesquisa/formatação.
- **Dor observada:** discussão mostra professores defendendo pagar pequenos valores por materiais organizados para não perder tempo pesquisando e formatando.
- **Fonte:** https://www.reddit.com/r/Teachers/comments/ywgyos
- **Sinal:** S3 fraco: usuários relatam compra de recursos de baixo valor em marketplace; não há números de vendas verificados.
- **Oferta testável:** pacote original de material, organização temática ou adaptação/formatação para um público específico. Respeitar direitos autorais, licenças e adequação pedagógica.
- **Custo inicial:** R$ 0 com ferramentas gratuitas; o custo principal é tempo.
- **Validação:** escolher uma disciplina/série e testar uma amostra com professores; só produzir lote maior após pedido ou pagamento.
- **Contraprova:** concorrência forte e recursos gratuitos abundantes.
- **Confiança:** baixa a média; discussão qualitativa com sinais explícitos de compra.

### D. Organização administrativa de autônomos
- **Público:** consultores e prestadores de serviço solo.
- **Dor observada:** relato de consultor lista horas diárias gastas em e-mail, preparação de reuniões, cobrança, organização documental e perguntas repetidas.
- **Fonte:** https://www.reddit.com/r/smallbusiness/comments/1r307db/
- **Sinal:** S2; custo de tempo declarado, sem compra observada.
- **Oferta testável:** serviço de organização de pastas, modelos de proposta, ata de reunião e checklist de follow-up usando dados fictícios ou fornecidos com autorização.
- **Custo inicial:** R$ 0; execução manual com Docs/Sheets.
- **Validação:** vender um pacote fechado de organização a um autônomo; não construir software.
- **Contraprova:** ferramentas genéricas e assistentes virtuais já fazem parte do mercado; cliente pode preferir resolver sozinho.
- **Confiança:** baixa; relato isolado e autodeclarado.

**Regra:** não aprovar nenhuma dessas oportunidades ainda. Fazer uma rodada independente para medir repetição, preço, compradores acessíveis e contraprovas.

## 11. Próximos passos prioritários

1. Confirmar que o computador disponível pode executar Antigravity (Windows 10/11 64-bit). O aplicativo não exige GPU dedicada na página de instalação, mas RAM disponível, navegador e sistema afetam a experiência.
2. Instalar Antigravity CLI ou desktop com conta Google pessoal gratuita; conferir cota e modelos no painel.
3. Abrir o repositório como workspace confiável.
4. Adicionar a skill operacional deste projeto.
5. Configurar o Reddit Research MCP via URL hospedada e OAuth, caso o cliente ofereça suporte.
6. Rodar o diagnóstico do Pain Miner e um lote pequeno; não fazer scraping agressivo nem contornar bloqueios.
7. Fazer o primeiro lote de pesquisa em cinco áreas distintas.
8. Escolher no máximo duas ofertas para validação; não desenvolver produto completo.
9. Registrar os resultados em STATE e nos experimentos.

## 12. Critério de sucesso do sistema

O sistema não será avaliado por quantidade de agentes, ideias, posts coletados ou arquivos gerados.

Será avaliado por:
- problemas documentados com fontes primárias;
- autores independentes e repetição entre comunidades;
- concorrentes/preços e contraprovas;
- conversas com potenciais compradores;
- pedidos de proposta;
- pilotos pagos;
- receita e margem por hora de trabalho.

**Conclusão:** a stack mais coerente é Antigravity Free + skill própria + GitHub + Reddit Research MCP + Pain Miner. É uma hipótese de arquitetura muito promissora, mas ainda precisa ser instalada e testada no computador. O primeiro dinheiro provavelmente virá de uma oferta manual simples, não de um agente autônomo nem de um SaaS construído antes de validar.
