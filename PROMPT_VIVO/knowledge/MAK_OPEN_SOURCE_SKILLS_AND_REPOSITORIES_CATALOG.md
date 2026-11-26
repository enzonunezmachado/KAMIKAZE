# Catálogo de repositórios e skills — Motor de Aquisição Kamikaze

**Data da auditoria:** 26/11/2026  
**Escopo:** inventário documental dos repositórios open source estudados para o MAK.  
**Regra:** este catálogo é um índice de referência e uma resenha crítica. Não significa que código, prompts ou workflows de terceiros foram importados, instalados ou aprovados para uso.

## 1. Resumo executivo

O levantamento contém um repositório principal de skills (Affitor/affiliate-skills), um diretório de programas afiliados (OpenAffiliate), uma plataforma de publicação/analytics (Postiz), workflows de automação e alguns projetos experimentais.

**Conclusão central:** o Affitor é a melhor referência metodológica para estruturar capacidades especializadas do MAK, mas não deve ser copiado como um pacote autônomo. O MAK deve transformar os métodos úteis em instruções próprias, com evidência, linguagem, regras brasileiras, restrições de orçamento e aprovação humana.

### Snapshot Affitor

- Repositório: https://github.com/Affitor/affiliate-skills
- Licença declarada: MIT.
- Snapshot GitHub consultado: 817 stars / 222 forks; atualizado em 26/11/2026 (metadados sujeitos a mudança).
- Árvore recursiva da branch `main`: 53 arquivos `skills/*/*/SKILL.md`.
- `registry.json`: 53 entradas, distribuídas em oito estágios.
- README/QUICKSTART ainda exibem 52; 50 aparece como contagem histórica. Para o inventário deste snapshot, prevalecem os arquivos canônicos e o registry.
- O registry declara `generated_at: 2026-10-19`; por isso, revalidar o catálogo quando o repositório mudar.
- `affiliate-program-search` é um ponteiro de compatibilidade para `find-and-verify-affiliate-program`, não uma capacidade independente equivalente.

## 2. Inventário das 53 skills Affitor

Os nomes abaixo são os slugs e caminhos observados na árvore de `main`. A descrição é um resumo funcional do README/registry, não uma reprodução integral dos arquivos de skill. Cada link abre a definição original.

### S1 — Research & Discovery (11)

1. [affiliate-program-search](https://github.com/Affitor/affiliate-skills/blob/main/skills/research/affiliate-program-search/SKILL.md) — ponte de compatibilidade; direciona ao fluxo canônico de descoberta e verificação.
2. [commission-calculator](https://github.com/Affitor/affiliate-skills/blob/main/skills/research/commission-calculator/SKILL.md) — calcula cenários de comissão e receita afiliada.
3. [competitor-spy](https://github.com/Affitor/affiliate-skills/blob/main/skills/research/competitor-spy/SKILL.md) — analisa estratégias públicas de afiliados concorrentes.
4. [content-angle-ranker](https://github.com/Affitor/affiliate-skills/blob/main/skills/research/content-angle-ranker/SKILL.md) — prioriza ângulos por competição, dados de engajamento e adequação de plataforma; score é heurístico.
5. [find-and-verify-affiliate-program](https://github.com/Affitor/affiliate-skills/blob/main/skills/research/find-and-verify-affiliate-program/SKILL.md) — descobre programas e confirma termos na fonte oficial do anunciante.
6. [monopoly-niche-finder](https://github.com/Affitor/affiliate-skills/blob/main/skills/research/monopoly-niche-finder/SKILL.md) — explora interseções de nicho e posicionamento diferenciado.
7. [niche-opportunity-finder](https://github.com/Affitor/affiliate-skills/blob/main/skills/research/niche-opportunity-finder/SKILL.md) — identifica e avalia oportunidades de nicho.
8. [purple-cow-audit](https://github.com/Affitor/affiliate-skills/blob/main/skills/research/purple-cow-audit/SKILL.md) — avalia diferenciação e capacidade de recomendação de um produto.
9. [submit-program](https://github.com/Affitor/affiliate-skills/blob/main/skills/research/submit-program/SKILL.md) — prepara submissão documentada de programas ao diretório OpenAffiliate.
10. [traffic-analyzer](https://github.com/Affitor/affiliate-skills/blob/main/skills/research/traffic-analyzer/SKILL.md) — examina tráfego e fontes de audiência de domínios.
11. [trending-content-scout](https://github.com/Affitor/affiliate-skills/blob/main/skills/research/trending-content-scout/SKILL.md) — pesquisa conteúdos populares e padrões em redes sociais.

### S2 — Content Creation (7)

1. [content-pillar-atomizer](https://github.com/Affitor/affiliate-skills/blob/main/skills/content/content-pillar-atomizer/SKILL.md) — desdobra uma peça central em conteúdos nativos para diferentes canais.
2. [content-research-brief](https://github.com/Affitor/affiliate-skills/blob/main/skills/content/content-research-brief/SKILL.md) — coleta fontes e monta brief de conteúdo baseado em pesquisa.
3. [infographic-generator](https://github.com/Affitor/affiliate-skills/blob/main/skills/content/infographic-generator/SKILL.md) — especifica infográficos e visuais com dados.
4. [reddit-post-writer](https://github.com/Affitor/affiliate-skills/blob/main/skills/content/reddit-post-writer/SKILL.md) — estrutura posts e comentários adequados ao contexto do Reddit; regras de cada comunidade prevalecem.
5. [tiktok-script-writer](https://github.com/Affitor/affiliate-skills/blob/main/skills/content/tiktok-script-writer/SKILL.md) — cria roteiros curtos para TikTok, Reels e Shorts.
6. [twitter-thread-writer](https://github.com/Affitor/affiliate-skills/blob/main/skills/content/twitter-thread-writer/SKILL.md) — estrutura threads para X.
7. [viral-post-writer](https://github.com/Affitor/affiliate-skills/blob/main/skills/content/viral-post-writer/SKILL.md) — prepara posts para redes sociais; “viral” é aspiração, não garantia.

### S3 — Blog & SEO (7)

1. [affiliate-blog-builder](https://github.com/Affitor/affiliate-skills/blob/main/skills/blog/affiliate-blog-builder/SKILL.md) — estrutura artigos de review, tutorial e afiliados.
2. [comparison-post-writer](https://github.com/Affitor/affiliate-skills/blob/main/skills/blog/comparison-post-writer/SKILL.md) — comparativos entre produtos.
3. [content-decay-detector](https://github.com/Affitor/affiliate-skills/blob/main/skills/blog/content-decay-detector/SKILL.md) — identifica conteúdo que perdeu desempenho e precisa de atualização.
4. [content-moat-calculator](https://github.com/Affitor/affiliate-skills/blob/main/skills/blog/content-moat-calculator/SKILL.md) — estima esforço de conteúdo para construir autoridade temática.
5. [how-to-tutorial-writer](https://github.com/Affitor/affiliate-skills/blob/main/skills/blog/how-to-tutorial-writer/SKILL.md) — escreve tutoriais com integração contextual de produtos.
6. [keyword-cluster-architect](https://github.com/Affitor/affiliate-skills/blob/main/skills/blog/keyword-cluster-architect/SKILL.md) — organiza palavras-chave em clusters e arquitetura temática.
7. [listicle-generator](https://github.com/Affitor/affiliate-skills/blob/main/skills/blog/listicle-generator/SKILL.md) — cria listas comparativas “top N”.

### S4 — Offers & Landing Pages (8)

1. [bonus-stack-builder](https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/bonus-stack-builder/SKILL.md) — organiza bônus associados à oferta; só usar bônus reais e entregáveis.
2. [grand-slam-offer](https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/grand-slam-offer/SKILL.md) — estrutura proposta de valor e oferta.
3. [guarantee-generator](https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/guarantee-generator/SKILL.md) — formula garantias; não prometer o que o afiliado não controla.
4. [landing-page-creator](https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/landing-page-creator/SKILL.md) — cria landing pages autocontidas.
5. [product-showcase-page](https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/product-showcase-page/SKILL.md) — cria página de apresentação aprofundada de produto.
6. [squeeze-page-builder](https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/squeeze-page-builder/SKILL.md) — cria páginas de captura.
7. [value-ladder-architect](https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/value-ladder-architect/SKILL.md) — desenha jornada de valor gratuito a ofertas pagas.
8. [webinar-registration-page](https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/webinar-registration-page/SKILL.md) — cria página de inscrição para eventos/webinars.

### S5 — Distribution & Deployment (4)

1. [bio-link-deployer](https://github.com/Affitor/affiliate-skills/blob/main/skills/distribution/bio-link-deployer/SKILL.md) — cria hub de links para bio.
2. [email-drip-sequence](https://github.com/Affitor/affiliate-skills/blob/main/skills/distribution/email-drip-sequence/SKILL.md) — estrutura sequência de nutrição por e-mail.
3. [github-pages-deployer](https://github.com/Affitor/affiliate-skills/blob/main/skills/distribution/github-pages-deployer/SKILL.md) — orienta deploy em GitHub Pages; deploy real continua sujeito à autorização do usuário.
4. [social-media-scheduler](https://github.com/Affitor/affiliate-skills/blob/main/skills/distribution/social-media-scheduler/SKILL.md) — organiza calendário de publicação.

### S6 — Analytics & Optimization (5)

1. [ab-test-generator](https://github.com/Affitor/affiliate-skills/blob/main/skills/analytics/ab-test-generator/SKILL.md) — propõe variantes de testes A/B.
2. [conversion-tracker](https://github.com/Affitor/affiliate-skills/blob/main/skills/analytics/conversion-tracker/SKILL.md) — estrutura UTMs e acompanhamento de cliques/conversões.
3. [internal-linking-optimizer](https://github.com/Affitor/affiliate-skills/blob/main/skills/analytics/internal-linking-optimizer/SKILL.md) — otimiza links internos de sites.
4. [performance-report](https://github.com/Affitor/affiliate-skills/blob/main/skills/analytics/performance-report/SKILL.md) — consolida KPIs e relatórios.
5. [seo-audit](https://github.com/Affitor/affiliate-skills/blob/main/skills/analytics/seo-audit/SKILL.md) — audita páginas e artigos para SEO.

### S7 — Automation & Scale (5)

1. [content-repurposer](https://github.com/Affitor/affiliate-skills/blob/main/skills/automation/content-repurposer/SKILL.md) — adapta conteúdo para formatos diferentes.
2. [email-automation-builder](https://github.com/Affitor/affiliate-skills/blob/main/skills/automation/email-automation-builder/SKILL.md) — desenha fluxos de e-mail condicionais.
3. [multi-program-manager](https://github.com/Affitor/affiliate-skills/blob/main/skills/automation/multi-program-manager/SKILL.md) — organiza portfólio de programas afiliados.
4. [paid-ad-copy-writer](https://github.com/Affitor/affiliate-skills/blob/main/skills/automation/paid-ad-copy-writer/SKILL.md) — prepara textos para anúncios pagos; fora do orçamento atual de R$0.
5. [proprietary-data-generator](https://github.com/Affitor/affiliate-skills/blob/main/skills/automation/proprietary-data-generator/SKILL.md) — estrutura pesquisas e dados originais.

### S8 — Meta (6)

1. [category-designer](https://github.com/Affitor/affiliate-skills/blob/main/skills/meta/category-designer/SKILL.md) — trabalha posicionamento e definição de categoria.
2. [compliance-checker](https://github.com/Affitor/affiliate-skills/blob/main/skills/meta/compliance-checker/SKILL.md) — revisa disclosure e regras; a referência FTC precisa adaptação brasileira.
3. [create-skill](https://github.com/Affitor/affiliate-skills/blob/main/skills/meta/create-skill/SKILL.md) — transforma processos repetíveis em skills estruturadas.
4. [funnel-planner](https://github.com/Affitor/affiliate-skills/blob/main/skills/meta/funnel-planner/SKILL.md) — planeja funil de pesquisa até receita.
5. [self-improver](https://github.com/Affitor/affiliate-skills/blob/main/skills/meta/self-improver/SKILL.md) — conduz retrospectiva e melhoria de campanhas.
6. [skill-finder](https://github.com/Affitor/affiliate-skills/blob/main/skills/meta/skill-finder/SKILL.md) — seleciona skills relevantes para uma tarefa.

## 3. Resenha crítica do Affitor

### O que vale muito a pena aproveitar

- **Modularidade:** cada capacidade tem propósito, entradas, saídas e próximos passos. Isso facilita dividir trabalho entre pesquisa, produção, distribuição e análise.
- **Pesquisa antes da produção:** o brief com fontes reduz conteúdo inventado ou genérico.
- **Verificação de oferta:** encontrar um programa não basta; comissão, cookie, payout, aprovação, restrições e termos devem ser confirmados no site oficial.
- **Pesquisa de conteúdo e ângulos:** observar o que o público pergunta e consome antes de produzir.
- **Adaptação por canal:** uma ideia central pode virar versões diferentes, desde que cada peça tenha valor próprio e respeite a cultura/regras do canal.
- **Mensuração em circuito fechado:** acompanhar cada etapa e devolver o aprendizado à pesquisa inicial.
- **Feedback e retrospectiva:** registrar o que funcionou, falhou, ficou sem dado e precisa ser testado de outra maneira.

### O que exige cautela ou não deve ser copiado

- Métricas de engajamento podem misturar observações, snippets, estimativas e proxies. Shares estimados e scores heurísticos não podem ser apresentados como dados medidos nem como previsão de conversão.
- Recomendações de algoritmo e regras de comunidade são mutáveis; confirmar políticas oficiais e regras locais antes de qualquer ação.
- Casos numéricos de receita e crescimento não possuem corroboração independente suficiente no repositório. Não são benchmarks para projetar nossa renda.
- Percentuais de aumento de conversão, bônus de múltiplos e garantias descritos em frameworks não devem ser usados como fatos sem estudos rastreáveis.
- FTC é referência dos EUA. Para operação brasileira, aplicar CDC, Decreto 7.962/2013, CONAR, LGPD e políticas atuais das plataformas.
- O CLI e algumas skills dependem de APIs/provedores externos, Bun, dados de terceiros ou serviços que podem ter custo/quota. Não são necessários para começar.
- “Viral” é linguagem aspiracional. O objetivo do MAK é utilidade, distribuição qualificada, confiança e resultado observável, não volume vazio.

### Resenha final

O Affitor é forte como **biblioteca de workflows e arquitetura de raciocínio para marketing de afiliados**. Não é prova de que um afiliado iniciante conseguirá vendas, não é um canal de aquisição por si só e não substitui a validação de público, produto, confiança e payout. Seu maior valor para o Kamikaze é ensinar a organizar uma operação completa e mensurável — desde a pesquisa de oferta até o aprendizado pós-campanha.

## 4. Outros repositórios estudados

### 4.1 [Affitor/OpenAffiliate](https://github.com/Affitor/open-affiliate)

- **Tipo:** diretório estruturado de programas afiliados; licença MIT.
- **Recursos anunciados:** catálogo de programas, dados de comissão/cookie/payout/aprovação/restrições, filtros, comparações, API REST, CLI, SDK e servidor MCP.
- **Valor para o MAK:** ponto de partida para descobrir candidatos e padronizar fichas de programas.
- **Limite decisivo:** registro comunitário não é fonte final dos termos. Confirmar cada dado na página oficial do anunciante, guardar URL, data e trecho comprobatório. O score do diretório mede critérios definidos pelo projeto; não equivale a qualidade comercial garantida.
- **Decisão:** referência de descoberta; não instalar CLI/MCP nem automatizar integração agora.

### 4.2 [GitroomHQ/Postiz](https://github.com/gitroomhq/postiz-app)

- **Tipo:** plataforma de gestão, agendamento e analytics de redes sociais; licença AGPL-3.0.
- **Recursos:** calendário, publicação em múltiplas redes, API e integrações; README lista Instagram, YouTube, LinkedIn, Reddit, TikTok, Facebook, Pinterest, Threads, X, Discord e outras.
- **Snapshot GitHub:** 42.451 stars / 8.119 forks no momento consultado.
- **Valor:** possível camada operacional futura para calendário e distribuição multicanal.
- **Limites:** self-host exige infraestrutura, manutenção, credenciais e integração oficial com cada rede; licença AGPL requer análise antes de incorporar/redistribuir código.
- **Decisão:** guardar como candidato futuro; não é prioridade de uma operação R$0 e não substitui estratégia de aquisição.

### 4.3 [MDanieechi14/tiktok-affiliate-promo-generator-n8n](https://github.com/MDanieechi14/tiktok-affiliate-promo-generator-n8n)

- **Tipo:** workflow n8n de geração de scripts, legendas e hashtags.
- **Fluxo declarado:** Google Sheets → seleção de produtos (limite de teste em 3) → Groq → estruturação da saída → planilha de resultados → notificação Telegram.
- **Valor:** exemplo simples de pipeline de produção e armazenamento de rascunhos.
- **Limites:** README descreve conteúdo Taglish; teste limitado; não prova conversões, vendas ou adequação ao público brasileiro. Depende de serviços externos e credenciais.
- **Decisão:** aproveitar o desenho conceitual de entrada estruturada/saída organizada; não importar sem adaptação e auditoria.

### 4.4 [eduubrz/affiliate-platform](https://github.com/eduubrz/affiliate-platform)

- **Tipo:** plataforma brasileira de campanhas afiliadas, IA, WhatsApp e analytics; licença MIT declarada.
- **Stack:** Node/Express/TypeScript, Prisma, PostgreSQL, Redis/BullMQ, Next.js, Docker, MinIO, Evolution API, OpenAI/Groq.
- **Valor:** referência de funcionalidades que uma plataforma mais completa poderia ter.
- **Limites:** README declara que o desenvolvimento ativo foi interrompido; arquitetura pesada, dependências e APIs oficiais pendentes; não é adequada ao orçamento/tempo atual.
- **Decisão:** não adotar como base.

### 4.5 [SankeerthBoddu/n8n-marketing-workflows](https://github.com/SankeerthBoddu/n8n-marketing-workflows)

- **Tipo:** exemplos de workflows n8n para geração, revisão, publicação e logging.
- **Padrão útil:** IA prepara conteúdo por rede → Google Sheets funciona como buffer de revisão → publicação é disparada após aprovação → IDs e resultados são registrados.
- **Valor:** referência mais alinhada à governança do MAK do que automação totalmente autônoma.
- **Limites:** o próprio autor define os fluxos como referências/rascunhos para teste, não como sistema de produção comprovado; requer credenciais e APIs de redes.
- **Decisão:** adotar o padrão de aprovação humana e registro, não assumir que os JSONs funcionam sem adaptação.

### 4.6 [signalreason/affiliate-content-automation](https://github.com/signalreason/affiliate-content-automation)

- **Tipo:** pipeline de SEO e conteúdo afiliado com clusters, landing pages, distribuição e testes A/B.
- **Stack declarada:** Go, Python, Next.js, Redis, PostgreSQL e serviços separados.
- **Valor:** referência conceitual para organizar clusters, links internos, páginas e analytics.
- **Limites:** proposta de geração em escala muito alta (até 1.000 artigos/semana) favorece volume e infraestrutura, não qualidade editorial; custo operacional e risco de conteúdo massivo sem utilidade.
- **Decisão:** não adotar como arquitetura inicial.

### 4.7 [AshmithaRajadurai/agentic-ai-social-media-manager](https://github.com/AshmithaRajadurai/agentic-ai-social-media-manager)

- **Tipo:** automação n8n para gerar conteúdo/imagens com Gemini, usar Cloudinary e publicar no Instagram; inclui Puppeteer.
- **Valor:** exemplo de encadeamento de geração e mídia.
- **Limites:** publicação automatizada e uso de navegador exigem revisão de políticas, segurança de credenciais e confiabilidade; README é curto e não apresenta evidência de resultados.
- **Decisão:** não adotar por enquanto; evitar automação por navegador e publicação sem aprovação humana.

### 4.8 [sonpiaz/hidrix-tools](https://github.com/sonpiaz/hidrix-tools)

- **Tipo:** servidor MCP de busca, leitura e análise de conteúdo; licença MIT.
- **Recursos declarados:** busca web, X, Reddit, YouTube e TikTok; leitura de páginas/threads; ferramentas de análise; armazenamento SQLite; algumas integrações usam provedores externos como RapidAPI/Apify/GetXAPI.
- **Valor:** pode ampliar pesquisa de tendências e comunidades com dados mais estruturados.
- **Limites:** nem todas as fontes são gratuitas; scraping pode conflitar com termos, privacidade ou políticas; métricas de provedores terceiros exigem validação e não devem ser confundidas com analytics oficiais.
- **Decisão:** referência técnica para pesquisa futura; não instalar nem usar scraping em comunidades.

## 5. Mapa de incorporação ao MAK

| Capacidade do MAK | Referências mais úteis | Adaptação própria |
|---|---|---|
| Pesquisa e segmentação de público | Affitor: niche-opportunity-finder, competitor-spy, trending-content-scout; hidrix-tools | Mapa de público, problema, gatilho, objeção, canal e qualidade da evidência |
| Inteligência de ofertas afiliadas | find-and-verify-affiliate-program; commission-calculator; OpenAffiliate | Ficha de oferta com termos oficiais, comissão líquida, atribuição, reembolso, payout e restrições |
| Brief e pauta | content-research-brief; content-angle-ranker | Brief com fontes, afirmações verificáveis, ângulos alternativos e hipótese de CTA |
| Conteúdo multicanal | writers por plataforma; atomizer; n8n TikTok workflow | Uma peça-mãe e adaptações realmente nativas, revisadas por humano |
| Páginas e apresentação | landing-page-creator; product-showcase-page; Postiz como distribuição futura | Página simples, clara, leve, sem claims falsos e sem depender de API paga |
| Relacionamento | MAK Relationship Network (módulo próprio) | Valor antes da oferta, permissão, conexão consentida, memória de marca e introdução voluntária |
| Distribuição | Postiz (futuro); n8n marketing workflows (padrão de aprovação) | Fila de rascunhos, checagem de regras, autorização humana e registro do post |
| Métricas e aprendizado | conversion-tracker; performance-report; self-improver | Funil com exposição, atenção, interesse, intenção, conversão, payout e relacionamento separados |
| Compliance | compliance-checker como referência | Gate brasileiro: CDC, CONAR, LGPD, Decreto 7.962/2013 e política atual do canal |

## 6. Prioridade sugerida de estudo/adaptação

**Prioridade 1 — transformar em capacidades nativas do MAK**
- Descobrir e verificar programas afiliados.
- Avaliar adequação/qualidade da oferta.
- Pesquisar público, problema, concorrentes e conteúdo já consumido.
- Produzir brief de conteúdo com fontes e claims rastreáveis.
- Adaptar conteúdo por plataforma.
- Registrar métricas por etapa e conduzir retrospectiva.
- Compliance/disclosure brasileiro.
- Relacionamento e indicação consentida, módulo próprio do MAK.

**Prioridade 2 — padrões operacionais**
- Buffer de revisão humana inspirado no n8n-marketing-workflows.
- Registro de campanhas e programas afiliados inspirado no OpenAffiliate.
- Calendário e distribuição multicanal, mantendo Postiz apenas como opção futura.

**Prioridade 3 — não construir agora**
- Plataforma afiliada completa.
- Automação autônoma de publicação/DM.
- Scrapers de redes/grupos.
- Geração massiva de artigos.
- Stack com banco, filas, Redis, APIs pagas e infraestrutura contínua.

## 7. Regras para incorporar skills ao repositório Kamikaze

1. Não copiar integralmente os arquivos de terceiros como se fossem nossos. Respeitar licença, atribuição e obrigações aplicáveis.
2. Criar skills próprias em português, orientadas ao MAK e com entradas, saídas, evidências, limites e handoffs claros.
3. Uma skill só entra como **ADOTADA** após revisão de utilidade, duplicidade, custo, segurança, compliance e adequação ao orçamento.
4. Manter status: `REFERÊNCIA`, `EM ANÁLISE`, `ADAPTADA`, `TESTADA`, `APROVADA` ou `REJEITADA`.
5. Nenhum teste comercial ou ação externa é inferido da existência de uma skill.
6. Toda recomendação automatizada deve preservar o fluxo: IA prepara → humano revisa → humano autoriza → execução permitida → métricas → aprendizado.
7. Não adicionar como capacidade ativa integração que exija conta, API, quota ou infraestrutura não aprovada.

## 8. Limites desta auditoria

- O inventário Affitor foi contado pela árvore recursiva e comparado com o registry; não significa que todas as 53 skills foram testadas individualmente.
- A leitura aprofundada anterior concentrou-se nas skills e referências ligadas diretamente ao MAK; este catálogo amplia o índice, não substitui auditoria linha a linha.
- Os dados de stars/forks são snapshots mutáveis do GitHub.
- A disponibilidade, licença e manutenção dos outros repositórios devem ser verificadas novamente antes de qualquer reutilização.
- Nenhum repositório foi clonado, instalado, executado ou importado nesta rodada.
- Nenhuma conta, publicação, mensagem, candidatura, deploy, compra ou gasto foi realizado.

## 9. Fontes principais

- Affitor skills: https://github.com/Affitor/affiliate-skills
- Affitor registry: https://github.com/Affitor/affiliate-skills/blob/main/registry.json
- OpenAffiliate: https://github.com/Affitor/open-affiliate
- Postiz: https://github.com/gitroomhq/postiz-app
- TikTok affiliate n8n: https://github.com/MDanieechi14/tiktok-affiliate-promo-generator-n8n
- AffiliateOS: https://github.com/eduubrz/affiliate-platform
- n8n marketing workflows: https://github.com/SankeerthBoddu/n8n-marketing-workflows
- Affiliate content automation: https://github.com/signalreason/affiliate-content-automation
- Agentic AI social media manager: https://github.com/AshmithaRajadurai/agentic-ai-social-media-manager
- hidrix-tools: https://github.com/sonpiaz/hidrix-tools



## 4. Extensão de pesquisa — futuro módulo de tráfego pago (26/11/2026)

O acionador e blueprint completos estão em [PAID_TRAFFIC_MODULE_ACTIVATION.md](PAID_TRAFFIC_MODULE_ACTIVATION.md). O estado é DORMANT / DOCUMENTED / NOT IMPLEMENTED: não autoriza gasto, criação de contas, conexão, alteração ou publicação de anúncios.

### Nova biblioteca de skills: marketing-skills
- Repositório: https://github.com/irinabuht12-oss/marketing-skills
- Snapshot da árvore recursiva: 49 arquivos `SKILL.md`; inventário nominal completo no documento do acionador.
- Capacidades relevantes: auditoria Google/Meta/LinkedIn/Reddit Ads; estrutura de contas; pesquisa de termos; desperdício; orçamento e pacing; lances; CPA/ROAS; fadiga criativa; sobreposição de públicos; tracking/UTM; landing page; atribuição; experimentos; relatórios.
- Resenha: referência de processos e checklists, não evidência de eficácia dos thresholds ou benchmarks. Algumas skills são genéricas e algumas dependem de Ryze MCP. Verificar a licença, a origem, as instruções e a dependência externa antes de adaptar. Não instalar pacote como está.

### Repositórios adicionais investigados
| Repositório | Papel potencial | Decisão preliminar |
|---|---|---|
| [googleads/google-ads-mcp](https://github.com/googleads/google-ads-mcp) | MCP oficial Google Ads, leitura/relatórios e mutações protegidas por Propose & Confirm | Referência técnica forte; exige projeto Google Cloud, OAuth e developer token; considerar mais tarde |
| [googleads/google-ads-python](https://github.com/googleads/google-ads-python) | SDK oficial Python para Google Ads API | Referência oficial; não necessário para primeira versão documental |
| [meta/facebook-python-business-sdk](https://github.com/meta/facebook-python-business-sdk) | SDK oficial Meta em Python | Referência oficial; requer app, token e permissões |
| [meta/facebook-nodejs-business-sdk](https://github.com/meta/facebook-nodejs-business-sdk) | SDK oficial Meta em Node.js | Referência oficial; mesmas exigências de autenticação |
| [irinabuht12-oss/google-ads-meta-ads-mcp](https://github.com/irinabuht12-oss/google-ads-meta-ads-mcp) | MCP hospedado com ferramentas de Ads e Analytics | Cautela: fornecedor Ryze, trial/planos pagos e acesso sensível a contas |
| [irinabuht12-oss/n8n-google-meta-ads](https://github.com/irinabuht12-oss/n8n-google-meta-ads) | Workflows n8n apoiados em MCP e serviços externos | Inspiração; dependências externas, não plug-and-play |
| [konkomaji/AdsOnSheets](https://github.com/konkomaji/AdsOnSheets) | Dashboard/alertas Meta Ads em Sheets + Apps Script | Útil como referência de monitoramento; exige token e permissões |
| [eduard0-g0mes/meta-ads-n8n-supabase](https://github.com/eduard0-g0mes/meta-ads-n8n-supabase) | Extração de insights Meta para Supabase/Sheets | Padrão de ingestão; requer infra e secrets |
| [nawazxz/clientreport](https://github.com/nawazxz/clientreport) | Relatórios GA4/Google Ads/Meta self-hosted | Referência de reporting; revisar conectores e segurança |
| [google/meridian](https://github.com/google/meridian) | Marketing Mix Modeling e planejamento agregado | Avançado; dados históricos e compute tornam-no inadequado ao começo |
| [mccannac/ai-marketing-reporting-workflow](https://github.com/mccannac/ai-marketing-reporting-workflow) | Relatório de Ads com validação, cálculos determinísticos e aprovação humana | Boa arquitetura de governança; autor declara design spec, não produto implantado |

**Princípio de arquitetura que emerge:** começar com planejamento, análise de dados exportados, cálculo determinístico, skills documentais e revisão humana. Conectar APIs apenas se houver necessidade comprovada e aprovação. Ações de escrita em contas devem usar proposta + confirmação específica. A publicação e o orçamento exigem autorização própria.

