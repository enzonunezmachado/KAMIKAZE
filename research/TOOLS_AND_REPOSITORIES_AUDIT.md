# Auditoria de ferramentas open source para pesquisa de oportunidades

**Data da auditoria:** 25/11/2026
**Objetivo:** encontrar repositórios e Agent Skills que ajudem uma IA a investigar comunidades, minerar dores reais, analisar alternativas comerciais e priorizar oportunidades executáveis por uma pessoa com orçamento inicial de R$ 0.

## Conclusão executiva

Não existe um repositório comprovado que, sozinho, encontre oportunidades lucrativas de forma confiável e gratuita. O melhor caminho é combinar:

1. **Pain Miner** para coletar e estruturar evidências de comunidades com barreiras de entrada relativamente baixas.
2. **Reddit Research MCP** para ampliar a descoberta semântica de comunidades e consultar posts/comentários com links.
3. **Trend Opportunity Radar** como referência de processo: amostragem delimitada, abertura das fontes originais, contraprovas, distinção entre fato e inferência e relatórios locais.
4. **Startup Skill** para aprofundar concorrência, estratégia e validação depois que um problema específico já foi encontrado.

A recomendação é não instalar uma plataforma grande agora. Primeiro usar a skill local market-opportunity-scout criada neste repositório e, quando houver ambiente Python/agente compatível, testar Pain Miner. Os scripts aceleram coleta e organização, não substituem validação comercial.

## 1. Repositórios analisados

### A. AdvancingTitans/pain-miner
Link: https://github.com/AdvancingTitans/pain-miner
Licença: MIT
Snapshot público consultado: 18 stars, 6 forks, 5 commits; último lote de commits consultado em 11/07/2026.
Fit com nosso método: muito alto.

**O que faz:** CLI Python + Agent Skill; pesquisa Reddit, Hacker News e V2EX; descobre e perfila comunidades; busca posts e comentários; classifica intenção, sinais comerciais, relevância e riscos; compara temas entre comunidades; gera JSON e relatório Markdown de nove seções, com fontes, contraprovas e plano de validação.

**Custo e dependências:** README declara fluxo padrão sem login, sem conta Reddit e sem API key. Requer Python 3.10+ e conectividade às fontes públicas; depende de Reddit/Arctic Shift, HN e V2EX e pode sofrer bloqueios/limites. A análise com IA depende do agente/modelo usado; não presumir que qualquer API será grátis.

**Por que é relevante:** é o repositório mais próximo do trabalho de mineração de problemas. O ponto forte não é gerar ideia, mas preservar fonte, risco, intenção, contraprova e suficiência de evidência.

**Limitações:** cobertura centrada em Reddit/HN/V2EX; projeto pequeno (18 stars e 5 commits no snapshot); o próprio projeto documenta bloqueios e indisponibilidade; foco em produto/indie SaaS, enquanto nossa skill local amplia para serviço manual, conteúdo, curadoria, intermediação e outros formatos.

Arquivos a estudar: SKILL.md, CHANGELOG.md, scripts/pain_miner.py, references/ e exemplos de saída.
**Veredito:** melhor primeiro script a testar quando houver ambiente de execução. Não é uma máquina de descobrir negócios prontos.

### B. dialog-tools/reddit-research-mcp
Link: https://github.com/dialog-tools/reddit-research-mcp
Licença: MIT
Snapshot público consultado: 268 stars, 30 forks, 106 commits; commits recentes até 20/10/2026.
Fit: alto como infraestrutura de pesquisa no Reddit.

**O que faz:** servidor MCP que conecta agentes a pesquisa semântica do Reddit; descoberta de subreddits por significado (README declara índice de 20.000+ comunidades); busca de posts, coleta de múltiplos subreddits, leitura de comentários e gerenciamento de feeds; resultados com citações e links.

**Custo/complexidade:** servidor hospedado apresentado como gratuito, mas requer conexão/autenticação MCP; autenticação usa Descope OAuth2. Não é agente completo nem cobre automaticamente outras plataformas. O uso depende de cliente compatível; não presumir instalação direta no app ChatGPT móvel.

**Veredito:** repositório mais popular e com histórico mais substancial entre os focados em pesquisa Reddit desta lista. Melhor ferramenta complementar se o ambiente MCP for compatível.

### C. datou202307-design/trend-opportunity-radar
Link: https://github.com/datou202307-design/trend-opportunity-radar
Licença: MIT
Snapshot público consultado: 19 stars, 3 forks, 44 commits; versão v0.14.1 candidate, commits recentes até 26/08/2026.
Fit: muito alto como referência de rigor de pesquisa.

**O que faz:** Agent Skill para social listening, concorrentes, conteúdo e validação de demanda; trabalha com um tópico e uma plataforma por estudo; define amostragem, abre fontes originais, revisa sinais e procura contraprovas; separa fatos observados, extração da máquina e julgamento do modelo; gera HTML, Markdown e JSON com manifesto e trilha de evidências.

**Plataformas e custo:** Reddit requer MCP de terceiros conectado pelo usuário; árvore de comentários desabilitada na rota descrita. X, YouTube e outras plataformas dependem de capacidades de leitura/autorização específicas; algumas rotas são beta ou exigem navegador autenticado. A skill é MIT e instala via npx skills add datou202307-design/trend-opportunity-radar -g, mas a coleta real pode depender de ferramentas externas.

O release declara que não prevê viralidade, tráfego, demanda ou receita e que algumas capacidades de monitoramento ainda são candidatas.
**Veredito:** excelente referência de processo e auditoria. Mais complexo do que precisamos para o primeiro teste; aproveitar a metodologia.

### D. ferdinandobons/startup-skill
Link: https://github.com/ferdinandobons/startup-skill
Licença: MIT
Snapshot público consultado: aproximadamente 1,3 mil stars, 167 forks, 67 commits; release v1.10.0 e commits recentes em 01/07/2026.
Fit: alto para a fase posterior à descoberta.

**O que faz:** skills para estratégia, pesquisa de mercado, descoberta de clientes, concorrência, posicionamento, projeções e experimentos. startup-design tem oito fases, pre-flight, gate de entrevistas e mais de 30 entregáveis. startup-competitors cria battle cards, análise de preços e matriz de recursos.

**Custo/complexidade:** MIT; instalação via plugin ou npx skills add. README alerta que usa múltiplos agentes de pesquisa e pode consumir muitos tokens; recomenda Claude Max 5x. Não combina com nossa restrição de custo zero como rotina principal. Mais útil quando já existe ideia/segmento concreto.
**Veredito:** maior adoção visível desta seleção, mas não é a primeira ferramenta para nossa fase atual. Guardar para análises profundas e usar com parcimônia.

### E. theomarsoliman/business-ideas-dataset
Link: https://github.com/theomarsoliman/business-ideas-dataset
Licença: MIT
Snapshot público consultado: 41 stars, 3 forks, 3 commits; dataset declarado com 42 ideias no último export descrito no README.
Fit: médio como referência de filtros e consulta, baixo como fonte primária.

**O que contém:** dataset JSON/CSV com ideias extraídas de reclamações do Reddit e avaliações da App Store; seis skills para validar ideias, encontrar oportunidades em nichos, montar MVP, mapear concorrentes, pesquisar Reddit e verificar demanda de palavras-chave. Metodologia declara 170 padrões de busca, sinais da App Store e enriquecimento com DataForSEO; scoring por modelo (Grok 3 mini).

**Limitações:** viés para SaaS/apps/ferramentas; subamostra mercados internacionais e não ingleses; volume de busca é dos EUA; dados completos de threads e concorrentes ficam no site; serviços pagos no pipeline (DataForSEO); score de IA é direcional. “Validated” é o rótulo do mantenedor, não auditoria independente de vendas.
**Veredito:** estudar padrões de consulta e checklist, não tratar scores como verdade nem copiar ideias cegamente.

### F. mkhanna-stack/venturemind-ai
Link: https://github.com/mkhanna-stack/venturemind-ai
Licença: verificar antes de reutilizar código (README consultado não deixou licença clara).
Snapshot público consultado: 3 stars, 0 forks, 1 commit.
Fit: médio como arquitetura demonstrativa.

**O que faz:** MVP com coleta de Reddit e Hacker News, limpeza/deduplicação, embeddings locais via sentence-transformers, ChromaDB, clustering KMeans, busca de concorrentes no DuckDuckGo e score de oportunidade. README declara que coleta, embeddings e clustering podem funcionar sem API paga; geração Claude é opcional.

**Limitações:** um commit e baixa adoção observável; pontuação e detecção de market gap são heurísticas do autor; frequência/concorrência não comprovam intenção de compra.
**Veredito:** não instalar agora. Estudar arquitetura local se quisermos construir pipeline próprio.

### G. lignertys/reddit-research-skills
Link: https://github.com/lignertys/reddit-research-skills
Licença: MIT
Snapshot público consultado: 15 stars, 1 fork, 22 commits.
Fit: alto para pesquisa Reddit, baixo para custo zero.

**O que faz:** skills de pesquisa de mercado, usuários, validação de produto, tendências e descoberta de comunidades; integra reddapi.dev, que declara busca semântica em dezenas de milhares de subreddits; inclui reddit-leads para intenção de compra.
**Limitações:** serviço terceiro com API key e limites por plano; reddit-leads exige plano pago.
**Veredito:** boa referência de playbooks, não adotar como infraestrutura principal.

### H. lefttree/reddit-pain-points
Link: https://github.com/lefttree/reddit-pain-points
Licença: MIT
Snapshot público consultado: 8 stars, 1 fork, 6 commits.
Fit: médio.

**O que faz:** coleta em 12+ subreddits, classifica linguagem de dor e usa Gemini/Claude para extrair público, problema, alternativas e score; dashboard e exportação CSV/JSON.
**Limitações:** modo real requer chave de API LLM; demo usa dados de exemplo; coleta pública pode falhar; score mistura engajamento, severidade e tamanho estimado de mercado.
**Veredito:** demonstração didática, não primeira escolha.

### I. huxm-git/reddit-idea-scout
Link: https://github.com/huxm-git/reddit-idea-scout
**O que faz:** PRAW com OAuth Reddit, filtros de dor, análise Claude e exportação CSV.
**Limitação:** exige credenciais Reddit e ANTHROPIC_API_KEY; não atende custo zero.

## 2. O que a pesquisa no Reddit mostra

Os relatos encontrados são úteis como pistas, mas quase todos os posts sobre ferramentas próprias são autopromoção. Resultados de receita são autodeclarados e não auditados.

1. **Claude e validação de ideia, alegação de US$ 2,3k MRR:** autor diz ter usado pesquisa do Claude para ler reclamações em Reddit, Quora e G2 sobre personalização de cold email; relata primeiro cliente pago na segunda semana e depois US$ 2,3k MRR com outreach. História individual, sem auditoria independente: https://www.reddit.com/r/SaaS/comments/1lwlk57/how_i_used_claude_to_validate_my_idea_in_10/
2. **ChatGPT e alegação de US$ 19k MRR:** autor descreve mudar de construir primeiro para pesquisar demanda antes; relato promocional/autodeclarado, sem verificação independente: https://www.reddit.com/r/SideProject/comments/1mfnzdg/
3. **IdeaPicker e 25 mil ideias:** criador declarou ter escaneado 250+ subreddits. Em comentário, admitiu que estimativas de receita foram geradas por IA e algumas eram irreais. Advertência contra volume de ideias e receita inventada: https://www.reddit.com/r/SideProject/comments/1c6ch2w/
4. **SaaStrike, 247 oportunidades:** criador relatou 100+ usuários, 247 ideias, 15 pessoas construindo e 3 MVPs lançados; métricas autodeclaradas de alguém promovendo a ferramenta, sem prova de vendas: https://www.reddit.com/r/SaaS/comments/1njnjb4/30_days_later_my_reddittosaas_tool_found_247_real/
5. **Como avaliar ideias com IA:** discussão pergunta como evitar falsos positivos e recomenda IA para agrupar dores e mapear concorrentes, mantendo entrevistas e validação humana: https://www.reddit.com/r/SaaS/comments/1s0de6i/how_do_you_systematically_evaluate_startup_ideas/
6. **40 horas pesquisando Reddit:** autor relata 12 discussões com “I’d pay” e dores, mas reconhece limitações de amostragem e esforço. Também é relato próprio: https://www.reddit.com/r/Entrepreneurs/comments/1qp8edh/spent_40_hours_analyzing_reddit_for_business/

**Aprendizado:** IA acelera leitura, extração e síntese; não encontrei evidência independente robusta de que instalar um desses repositórios e rodá-lo gratuitamente tenha gerado receita a um usuário comum. Medir qualidade de evidência e conversões, não quantidade de ideias ou scores.

## 3. Comparação resumida

| Projeto | Função | Stars | Commits | Obstáculo | Decisão |
|---|---|---:|---:|---|---|
| Pain Miner | Coletar dores, intenção e contraprovas | 18 | 5 | Python; fontes públicas podem falhar | Testar primeiro |
| Reddit Research MCP | Descobrir comunidades e ler Reddit com citações | 268 | 106 | MCP + OAuth | Complemento prioritário |
| Trend Opportunity Radar | Processo rigoroso por plataforma | 19 | 44 | Adaptadores/MCP | Referência metodológica |
| Startup Skill | Estratégia, concorrência e validação | ~1.3k | 67 | Alto consumo de tokens | Usar depois |
| Business Ideas Dataset | Dataset e padrões de consulta | 41 | 3 | Viés SaaS/US; DataForSEO | Consultar com cautela |
| VentureMind AI | Pipeline NLP local demonstrativo | 3 | 1 | Setup técnico; score heurístico | Não instalar agora |
| Reddit Research Skills | Busca semântica e leads | 15 | 22 | API terceira; lead feature paga | Não usar como base grátis |
| Reddit Pain Points | Dashboard de mineração Reddit | 8 | 6 | API LLM para análise | Apenas referência |
| Reddit Idea Scout | Scraper PRAW + Claude | — | — | OAuth Reddit + API Claude | Não usar |

*Stars e commits são snapshots de 25/11/2026 e podem mudar. Popularidade mede adoção do código, não qualidade das oportunidades ou receita produzida.*

## 4. Arquitetura recomendada

- **Descoberta:** pesquisa web/Reddit ampla, Pain Miner e, se disponível, Reddit Research MCP.
- **Leitura:** abrir threads originais e comentários; registrar contexto, tentativas e contrapontos.
- **Mercado:** pesquisar ferramentas, serviços, preços, avaliações, reclamações e sinais de compra fora do Reddit.
- **Julgamento:** usar a skill local market-opportunity-scout, que exige evidência de compradores e permite concluir “sem oportunidade”.
- **Memória:** salvar fontes, resultados, decisões e próximos passos no GitHub.
- **Validação:** contato com potenciais compradores, pré-venda, orçamento ou piloto antes de construir.

Pesquisar negócios de qualquer formato. Não assumir SaaS.

## 5. Próximos passos técnicos

1. Usar a skill local como instrução padrão de pesquisa.
2. Em ambiente Python, testar Pain Miner com um alvo amplo e amostra controlada; verificar disponibilidade das fontes.
3. Se houver cliente MCP compatível, testar Reddit Research MCP como camada de descoberta e leitura.
4. Não instalar Trend Opportunity Radar inteiro até existir necessidade de pesquisa multiplataforma com rastreabilidade.
5. Comparar pesquisa manual assistida vs Pain Miner em dois conjuntos de comunidades: diversidade, fontes válidas, duplicatas, falsos positivos e evidência comercial.
6. Não importar pontuações como verdade; decidir com evidência primária, alternativas pagas e validação direta.

## 6. Fontes principais

- https://github.com/AdvancingTitans/pain-miner
- https://github.com/dialog-tools/reddit-research-mcp
- https://github.com/datou202307-design/trend-opportunity-radar
- https://github.com/ferdinandobons/startup-skill
- https://github.com/theomarsoliman/business-ideas-dataset
- https://github.com/mkhanna-stack/venturemind-ai
- https://github.com/lignertys/reddit-research-skills
- https://github.com/lefttree/reddit-pain-points
- https://github.com/huxm-git/reddit-idea-scout

**Status:** revisão em nível de README, SKILL.md, metodologia, changelog, metadados e commits recentes. Ainda não instalamos nem executamos os projetos localmente; não afirmar que passaram em teste funcional.