# Acionador de implementação — Módulo de Tráfego Pago

**ID:** MAK-PAID-TRAFFIC-MODULE  
**Estado:** DORMANT / DOCUMENTED / NOT IMPLEMENTED  
**Criado:** 26/11/2026  
**Responsável pela ativação:** usuário, por intenção explícita e confirmação  
**Escopo:** preparar a futura implementação de uma capacidade completa de tráfego pago, sem autorizar campanhas, contas, gastos, publicações ou integrações agora.

## 1. Propósito do acionador

Este documento é um gatilho operacional persistente. Ele não inicia tráfego pago por conta própria. Serve para reconhecer quando o usuário decidir que chegou a hora de implementar essa capacidade, recuperar a pesquisa e o desenho preparados, apresentar o pacote de implementação e solicitar uma confirmação explícita antes de começar.

O módulo deve ser robusto, modular, ensinável e adequado ao contexto real que existir na data da ativação. Não congelar como requisito permanente a filosofia atual do Kamikaze: na ativação, reavaliar a filosofia, objetivos, orçamento, recursos, maturidade da oferta, ferramentas, políticas, legislação e plataformas disponíveis. Integrar-se ao Kamikaze somente onde isso gerar valor. O módulo deve continuar funcional como unidade independente se a arquitetura principal tiver mudado.

## 2. Linguagem de ativação e protocolo de confirmação

### Frases que indicam intenção de ativar
Exemplos:
- "Quero implementar tráfego pago."
- "Vamos começar a construir o módulo de tráfego pago."
- "Chegou a hora de montar nossa operação de anúncios pagos."
- "Ative o projeto de implementação de tráfego pago."

Menções exploratórias como "pesquise tráfego pago", "como funciona Meta Ads?", "um dia podemos anunciar?" ou "compare Google e Meta" não ativam o módulo.

### Resposta obrigatória ao detectar intenção clara
1. Informar que existe o acionador documentado `MAK-PAID-TRAFFIC-MODULE`.
2. Apresentar um resumo do pacote: objetivo, escopo, etapas, entregáveis, dependências, custos potenciais, riscos e permissões necessárias.
3. Perguntar diretamente: **"Você confirma que quer iniciar agora a implementação do Módulo de Tráfego Pago, começando pela Etapa 0 de revalidação e planejamento?"**
4. Não iniciar construção, criar contas, conectar APIs, publicar anúncios ou assumir despesas antes da confirmação.
5. Se o usuário confirmar apenas a Etapa 0, isso autoriza somente auditoria e planejamento documental. Cada ação externa ou com custo continua exigindo autorização separada.
6. Se a resposta for ambígua, continuar em modo de conversa/pesquisa, sem ativar.

A confirmação para implementar o módulo nunca é autorização para gastar dinheiro. A autorização para preparar campanhas nunca é autorização para publicá-las. A autorização para publicar uma campanha deve especificar plataforma, conta, campanha, criativos, orçamento máximo, duração, limites e evento de conversão.

## 3. O que o módulo futuro deverá entregar

Ao concluir a implementação, apresentar um pacote de handoff profissional contendo:
- visão geral e arquitetura do módulo;
- mapa de skills e suas dependências;
- guia de utilização passo a passo;
- comandos/prompts de entrada e exemplos;
- checklists pré-campanha, pré-publicação e pós-publicação;
- matriz de permissões e aprovações;
- planilhas/modelos de orçamento, unit economics e tracking;
- templates de brief, campanha, criativo, landing page e relatório;
- critérios de qualidade, bloqueios e escalonamento;
- plano de testes em modo offline/sandbox, sem gasto;
- instruções de manutenção e atualização de políticas;
- changelog e registro de fontes;
- integração com Kamikaze, se aprovada e ainda pertinente;
- apresentação final do módulo, com o que foi construído, o que não foi, como usar e quais são os próximos passos.

Não declarar "completo" se algum componente essencial estiver ausente. A entrega deve mostrar status por componente: IMPLEMENTADO, PARCIAL, BLOQUEADO, FUTURO ou NÃO APLICÁVEL.

## 4. Arquitetura proposta — independente e integrável

### Camada A — Strategy & Readiness
- business-and-offer-readiness: validar se existe oferta real, público, problema, diferencial, prova, capacidade de entrega e suporte.
- paid-media-goal-selection: selecionar objetivo de negócio e evento primário; não otimizar para vaidade.
- channel-fit-assessment: decidir entre Google Search, Shopping/Performance Max quando adequado, Meta, YouTube, LinkedIn, TikTok, Reddit ou outros; não presumir que todas as plataformas são necessárias.
- economics-and-break-even: margem de contribuição, ticket, comissão líquida, taxa de conversão, CAC máximo, CPA de equilíbrio, ROAS de equilíbrio, reembolsos, impostos e fluxo de caixa.
- paid-media-readiness-gate: bloquear mídia paga quando oferta, página, mensuração, atendimento, economia ou política não estiverem prontos.

### Camada B — Research & Planning
- audience-and-intent-research: segmentos, dores, linguagem, gatilhos, objeções e intenção.
- keyword-and-demand-research: palavras-chave, intenção, volume, competição e sazonalidade, com fonte e data.
- competitor-and-ad-library-research: análise ética de anúncios públicos, posicionamento e criativos; não copiar ativos ou claims.
- campaign-architecture: estrutura de campanhas, grupos/conjuntos, segmentação, exclusões e nomenclatura.
- budget-scenario-planner: cenários conservador/base/otimista, limites e sensibilidade; projeções não são garantias.
- testing-roadmap: hipóteses, variável, controle, amostra, janela e critério de decisão.

### Camada C — Creative & Conversion
- creative-strategy-and-brief: conceito, ângulo, promessa verificável, prova, CTA e formato.
- ad-copy-and-creative-studio: textos, variações, roteiro, visual e especificações por plataforma.
- landing-page-and-conversion-audit: velocidade, clareza, correspondência anúncio/página, confiança, acessibilidade e fricção.
- offer-and-funnel-design: caminho anúncio → página → conversa/checkout → venda → pós-venda.
- experiment-design: plano de testes sem confundir correlação com causalidade.

### Camada D — Tracking, Privacy & Compliance
- measurement-architecture: evento primário, eventos secundários, UTMs, GA4 e relatórios.
- conversion-tracking-qa: validar tags, pixels, APIs de conversão, deduplicação, consentimento e atribuição.
- data-quality-and-attribution: distinguir evento observado, conversão reportada pela plataforma, conversão real e receita recebida.
- privacy-and-lgpd-review: minimização, base legal, transparência, retenção, direitos e consentimento quando aplicável.
- platform-policy-review: políticas atuais de Google, Meta e demais plataformas; restrições do produto, nicho, claims e landing page.
- br-advertising-and-consumer-law: CDC, CONAR, regras de publicidade, afiliados e disclosure brasileiro; revisão jurídica especializada quando necessário.

### Camada E — Campaign Operations
- account-and-access-security: contas, Business Manager, permissões mínimas, MFA, tokens, segredos e recuperação.
- campaign-build-spec: gerar estrutura pronta para revisão, inicialmente sem executar alterações.
- preflight-and-policy-check: checklist antes de qualquer publicação.
- launch-approval-gate: resumo explícito do que será publicado, onde, por quanto, por quanto tempo e quais limites.
- pacing-and-budget-guard: acompanhar ritmo, limite diário/total, alertas e stop-loss.
- campaign-monitoring: anomalias, entrega, reprovação, frequência, leilão, custo e conversões.
- optimization-recommendations: recomendações priorizadas, explicando evidência, incerteza e efeito esperado.
- incident-and-pause-protocol: interrupção, gasto inesperado, conta comprometida, tracking quebrado ou anúncio irregular.

### Camada F — Learning & Governance
- performance-analysis: CTR, CPC, CPM, CVR, CPA, CAC, ROAS, margem e receita líquida, com definições consistentes.
- creative-fatigue-and-audience-diagnostics: fadiga, frequência, saturação, sobreposição e deterioração.
- attribution-and-incrementality: limites de atribuição; experimentos de incremento quando houver escala/dados suficientes.
- weekly-and-monthly-review: relatório de decisão, não apenas dashboard.
- knowledge-and-playbook-updater: converter resultados reais em playbooks, sem generalizar com amostras pequenas.
- skills-and-policy-version-audit: verificar atualizações de APIs, skills, termos e políticas.

## 5. Etapas de implementação após ativação

A implementação deverá ser adaptativa. Esta é uma sequência inicial, não uma promessa de que todas as etapas serão necessárias.

| Etapa | Nome | Resultado verificável | Gate |
|---|---|---|---|
| 0 | Revalidação e diagnóstico | Contexto, negócio, orçamento, competências, oferta, filosofia atual e objetivos atualizados | Usuário aprova brief de implementação |
| 1 | Pesquisa técnica e de mercado | Plataformas, políticas, documentação oficial, repositórios, ferramentas e custos atuais | Evidências e arquitetura aprovadas |
| 2 | Blueprint e skills | Mapa modular, interfaces, entradas/saídas, regras e dependências | Blueprint aprovado |
| 3 | Núcleo de estratégia/economia | Readiness, unit economics, planejamento e critérios de bloqueio | Testes de cenários aprovados |
| 4 | Núcleo criativo/conversão | Briefs, anúncios, criativos, landing pages e testes | Revisão de qualidade aprovada |
| 5 | Mensuração e compliance | UTMs, eventos, tracking QA, LGPD, disclosure e políticas | Testes de rastreamento e compliance aprovados |
| 6 | Operação e simulação | Campanhas fictícias/sandbox, preflight, orçamento e incidentes | Simulação sem ações reais aprovada |
| 7 | Integrações opcionais | APIs, MCP, n8n, relatórios ou conectores necessários | Aprovação técnica e de custo por integração |
| 8 | Handoff e treinamento | Manual, apresentação, exemplos, checklist e demonstração | Usuário entende e aceita o módulo |

A publicação real é um gate separado, posterior à implementação. A campanha só pode ser criada/alterada/publicada mediante autorização específica.

## 6. Regras de segurança financeira e de execução

- O módulo não presume verba disponível. Solicitar orçamento total, orçamento diário, duração, perda máxima aceitável e fonte do dinheiro.
- Não recomendar empréstimo, rotativo ou cartão como se fossem capital livre.
- Não iniciar anúncios se o valor puder comprometer contas essenciais ou obrigações financeiras.
- Começar por simulação e pesquisa. Se não houver orçamento suficiente para testar com aprendizado estatisticamente minimamente útil, dizer isso e recomendar não anunciar ainda.
- Definir limite de gasto total e procedimento de pausa antes de ativar qualquer campanha.
- Nunca prometer vendas, CPA, ROAS, lucro ou prazo.
- Não escalar por resultado isolado; considerar volume, janela, margem, qualidade do lead e receita recebida.
- Não alterar orçamento, lance, público, criativo, pixel, evento ou status de campanha automaticamente.
- Nenhuma automação pode publicar, ativar, aumentar orçamento ou criar gasto sem autorização humana específica.
- Separar recomendações de execução: leitura/análise pode ser automatizada com acesso autorizado; mutações exigem proposta e confirmação.
- Nunca inserir tokens, chaves ou dados pessoais em GitHub, prompts públicos ou arquivos sem proteção.

## 7. Portfólio de repositórios para auditoria futura

Todos são referências para estudar, não componentes já aprovados para adoção. Na ativação, conferir estado, licença, atividade, dependências, segurança, termos, custos e compatibilidade novamente.

### Referências centrais de skills e workflows
1. [Affitor/affiliate-skills](https://github.com/Affitor/affiliate-skills) — 53 skills catalogadas em MAK; referência para pesquisa, conteúdo, distribuição, analytics, automação e compliance. Adaptar as partes de mídia paga e funil.
2. [irinabuht12-oss/marketing-skills](https://github.com/irinabuht12-oss/marketing-skills) — 49 skills em Markdown, com Google Ads, Meta Ads, diagnóstico, orçamento, criativos, tracking, análise e SEO. O README promove integração Ryze MCP; separar skills abertas do serviço hospedado e validar licença/termos no momento da ativação.
3. [SankeerthBoddu/n8n-marketing-workflows](https://github.com/SankeerthBoddu/n8n-marketing-workflows) — padrão IA prepara → planilha de revisão → aprovação humana → publicação → logging. Workflows descritos como referência/teste, não produção comprovada.
4. [mccannac/ai-marketing-reporting-workflow](https://github.com/mccannac/ai-marketing-reporting-workflow) — pipeline de dados, validação, cálculos determinísticos, detecção de mudanças, interpretação IA e aprovação humana. Design spec, não implantação.

### APIs e integração oficial
5. [googleads/google-ads-mcp](https://github.com/googleads/google-ads-mcp) — servidor MCP oficial do Google Ads; consultas/relatórios e mutações limitadas com fluxo Propose & Confirm; requer Google Cloud/API e credenciais; não é gestor de campanhas autônomo.
6. [googleads/google-ads-python](https://github.com/googleads/google-ads-python) — biblioteca cliente oficial Python para Google Ads API; requer developer token, OAuth e configuração.
7. [meta/facebook-python-business-sdk](https://github.com/facebook/facebook-python-business-sdk) — Business SDK oficial Meta para Python; acesso à Marketing API depende de app, tokens e permissões.
8. [meta/facebook-nodejs-business-sdk](https://github.com/facebook/facebook-nodejs-business-sdk) — Business SDK oficial Meta para Node.js; mesmas exigências de autenticação e permissões.
9. [irinabuht12-oss/google-ads-meta-ads-mcp](https://github.com/irinabuht12-oss/google-ads-meta-ads-mcp) — MCP hospedado por Ryze que declara 250+ ferramentas Google/Meta/GA4/GSC; inclui trial e planos pagos, não deve ser presumido gratuito ou necessário. Requer auditoria de privacidade, fornecedor, acesso e custo.
10. [irinabuht12-oss/n8n-google-meta-ads](https://github.com/irinabuht12-oss/n8n-google-meta-ads) — workflows que usam Ryze MCP, Gemini, Gamma, Gmail e Firecrawl; dependem de serviços externos e credenciais.

### Reporting e analytics
11. [konkomaji/AdsOnSheets](https://github.com/konkomaji/AdsOnSheets) — dashboard Meta Ads em Google Sheets/Apps Script com alertas e relatórios; depende de Meta token, permissões e revisão de segurança. Frequência e regras anunciadas no README não são validação independente.
12. [eduard0-g0mes/meta-ads-n8n-supabase](https://github.com/eduard0-g0mes/meta-ads-n8n-supabase) — extração Meta → n8n → Supabase/Sheets; requer token ads_read, infra e secrets. Útil como referência de ingestão, não necessário para MVP.
13. [nawazxz/clientreport](https://github.com/nawazxz/clientreport) — relatórios self-hosted em Python para GA4, Google Ads, Meta Ads e outras fontes; MIT declarado, runtime dependencies zero segundo README. Avaliar conectores e credenciais antes de usar.
14. [google/meridian](https://github.com/google/meridian) — Marketing Mix Modeling para análise agregada de canais e planejamento de orçamento; requer histórico e volume de dados, Python 3.11–3.13 e compute relevante. Fase avançada, não ferramenta de primeira campanha.
15. [Postiz](https://github.com/gitroomhq/postiz-app) — agendamento e analytics orgânicos multirrede; complementar para conteúdo, não substitui gestão de mídia paga.

### Regra de priorização
- Começar por skills documentais, fontes oficiais, cálculos transparentes e planilhas simples.
- APIs oficiais apenas quando houver necessidade real, conta, credenciais e aprovação.
- Evitar conectar contas de anúncios a SaaS de terceiros sem avaliação de dados, permissões, retenção, suboperadores e custo.
- Não adotar scraping de bibliotecas de anúncios nem automações que violem termos.
- Não importar nenhum repositório diretamente para produção. Fazer leitura de código, licença, dependências, secrets, rede, permissões e comportamento antes de qualquer teste isolado.

## 8. Inventário inicial de 49 skills — marketing-skills

Inventário do snapshot da árvore recursiva consultada em 26/11/2026. Os nomes podem mudar; verificar novamente na ativação. A listagem não significa adoção.

### Auditoria e estratégia de conta
1. `account-structure-review`
2. `google-ads-audit`
3. `meta-ads-audit`
4. `linkedin-ads-audit`
5. `reddit-ads-audit`
6. `ad-extension-audit`
7. `quality-score-breakdown`
8. `search-term-mining`
9. `wasted-spend-finder`
10. `performance-benchmarking`
11. `competitor-creative-analysis`
12. `competitor-teardown`

### Orçamento, lances e eficiência
13. `ad-spend-allocator`
14. `budget-scenario-planner`
15. `bid-strategy-recommendations`
16. `channel-mix-optimizer`
17. `pacing-monitor`
18. `cpa-diagnostics`
19. `roas-forecasting`
20. `day-hour-performance-breakdown`
21. `device-performance-split`
22. `geo-performance-analysis`

### Público, frequência e criativos
23. `audience-overlap-analysis`
24. `creative-fatigue-detection`
25. `frequency-cap-recommendations`
26. `retargeting-window-analysis`
27. `ad-copy-variant-generator`
28. `icp-research-assistant`

### Conversão, tracking e experimentos
29. `ab-test-analyzer`
30. `ab-test-setup-and-analysis`
31. `attribution-model-comparison`
32. `conversion-path-analysis`
33. `utm-tracking-generator`
34. `landing-page-audit`
35. `landing-page-audit-39`
36. `anomaly-detection`

### Naming, reporting e planejamento
37. `campaign-naming-convention-builder`
38. `client-report-narratives`
39. `weekly-account-summary`

### Capacidades adjacentes de SEO e visibilidade
40. `e2e-seo-assistant`
41. `programmatic-seo-builder`
42. `programmatic-seo-playbook`
43. `keyword-cannibalization-check`
44. `ai-visibility-audit`
45. `brand-answer-monitoring`
46. `citation-source-gap-finder`
47. `content-aeo-optimizer`
48. `content-repurposer`
49. `email-sequence-writer`

### Observação de contagem
A árvore recursiva retornou 49 arquivos `SKILL.md`, e a enumeração acima agora contém os 49 slugs únicos. A lista é um inventário nominal; descrições e critérios de adoção devem ser aprofundados na ativação. **Status: 49/49 listados; nenhum código importado.**

## 9. Lacunas a pesquisar quando ativado

- Estado atual das políticas Google Ads, Meta Ads e plataformas selecionadas.
- Regras brasileiras atuais para publicidade, afiliados, saúde/finanças e categorias reguladas.
- Regras e APIs para contas brasileiras, verificação de anunciante e faturamento.
- Limites, aprovação e tempo de obtenção de Google Ads developer token e Meta App Review.
- Custos reais de domínio, landing page, hospedagem, analytics, CRM, APIs e ferramentas.
- Como instrumentar conversões com consentimento e LGPD sem coletar mais dados que o necessário.
- Estratégias de campanha adequadas ao tipo de negócio e à economia real; não assumir afiliados.
- Modelos de orçamento mínimo de teste por plataforma e como estimar amostra/tempo sem inventar benchmarks.
- Procedimentos de contestação de reprovação, suspensão e bloqueio de conta.
- Acesso a dados, retenção e exportabilidade de fornecedores de MCP/automação.
- Adequação das skills Affitor/marketing-skills a ChatGPT e ao ambiente de trabalho real; não presumir compatibilidade plug-and-play.

## 10. Checklist de prontidão para autorizar uma campanha real

Uma campanha não está pronta só porque o módulo foi implementado. Antes de cada lançamento, apresentar e obter aprovação separada para:
- negócio/oferta e página final;
- plataforma e conta de anúncios exatas;
- objetivo, evento de otimização e definição de conversão;
- público, geografia e exclusões;
- criativos, textos, claims e disclosure;
- landing page, checkout e atendimento;
- tracking testado e qualidade dos dados;
- orçamento diário, teto total, datas e perda máxima aceitável;
- regras de pausa e pessoa responsável;
- riscos e incertezas;
- confirmação final inequívoca para publicar.

## 11. Estado e manutenção

- Estado atual: DORMANT / DOCUMENTED / NOT IMPLEMENTED.
- Não existe autorização de gasto, conta, integração, campanha ou publicação.
- A implementação só começa após intenção clara + confirmação do pacote/Etapa 0.
- O plano deve ser revalidado na data de ativação; snapshots e políticas envelhecem.
- Quando a filosofia do Kamikaze mudar, revisar integração e dependências sem apagar a autonomia deste módulo.
- Alterações deste documento devem ser registradas em changelog e logs do Prompt Vivo.
