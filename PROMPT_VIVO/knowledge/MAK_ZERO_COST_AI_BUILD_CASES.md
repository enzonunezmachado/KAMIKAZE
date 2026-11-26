# MAK — Casos de construção com IA e ferramentas gratuitas

**Data da pesquisa:** 26/11/2026  
**Escopo:** pessoas e projetos que construíram aplicações, ferramentas, SaaS ou automações com IA e planos gratuitos, priorizando custo inicial realmente zero, funcionamento observável, arquitetura reaproveitável e transparência sobre resultados.  
**Estado:** pesquisa documental; nenhum projeto foi instalado, clonado, executado, cadastrado ou adotado.

## 1. Definições para não confundir “grátis”

- **ZERO-CASH / CLAIMED:** criador declara não ter pago ferramentas/infra durante o período, mas a declaração não foi auditada financeiramente.
- **ZERO-CASH / CORROBORATED BUILD:** há artefato público funcional (demo/código) e uma fonte descreve explicitamente uso de plano gratuito para construir e publicar. Não significa auditoria de todos os custos indiretos.
- **FREE-TIER STACK:** combinação de planos gratuitos; limites, regras comerciais, inatividade e uso de IA podem restringir o uso.
- **BOOTSTRAPPED / COST UNKNOWN:** sem investimento externo ou equipe, mas não há prova de custo zero. Não classificar como gratuito.
- **FREE PRODUCT / NOT A FREE BUILD:** produto é gratuito para o usuário, mas isso não comprova que o criador o construiu sem pagar.

Tempo de trabalho, equipamento, internet, conhecimento, contas já pagas, custo de oportunidade e taxas transacionais não desaparecem porque a fatura mensal de hospedagem é US$0.

## 2. Casos estudados

### Caso A — Stockroom: aplicativo completo de estoque gerado e publicado por IA
- **Fonte primária do caso:** https://appjet.ai/blog/free-full-stack-inventory-app-case-study
- **Código público:** https://github.com/qoddiapps/inventory-appjet
- **Demo:** https://jrhgma9jb6.dev.ap-jt.com
- **Classificação:** ZERO-CASH / CORROBORATED BUILD, com ressalva de que o caso foi produzido/publicado pelo próprio fornecedor AppJet.
- **O que existe:** dashboard de estoque; catálogo de produtos com busca, filtros, ordenação e CRUD; categorias e fornecedores; histórico/ledger de movimentações; validação contra estoque negativo; cálculos; exportação CSV; backend e banco SQLite.
- **Stack observada no repositório:** Next.js 16, React, TypeScript strict, Tailwind CSS v4, Node 24, SQLite via better-sqlite3, Docker. API routes para produtos, fornecedores, categorias, movimentações, estatísticas e exportação.
- **Processo/custo declarado:** AppJet afirma que a IA escreveu todo o código, schema, API, UI, dados de demonstração, Dockerfile e README; o caso foi construído e implantado no plano gratuito, sem virtual disk pago. O repositório afirma que nenhum código foi escrito/editado manualmente por pessoa.
- **Limites importantes:** demonstração usa dados de amostra; não tem autenticação/login; a persistência do SQLite depende de volume configurado no host; a própria AppJet alerta para verificar persistência e backups antes de dados reais. O estudo de caso é material promocional do fornecedor, embora o código, demo e funcionalidades possam ser inspecionados.
- **Valor para o MAK:** prova concreta de que um fluxo AI-builder pode produzir um sistema operacional de negócio com frontend, lógica de backend, banco, validações e exportação sem pagar assinatura de desenvolvimento. É o caso mais forte desta rodada para “construir algo funcional por R$0”.
- **Não significa:** que qualquer sistema comercial ficará seguro, multiusuário, persistente ou escalável sem trabalho humano.

### Caso B — MyClaw Tools: 249 ferramentas de IA com custo mensal declarado de US$0
- **Fonte:** https://medium.com/@ahmadyarkhan.2/the-0-tech-stack-behind-249-free-ai-tools-11b5f5f57a3a
- **Produto:** https://myclaw-tools.vercel.app
- **Classificação:** ZERO-CASH / CLAIMED; autorrelato técnico detalhado, sem auditoria financeira independente.
- **Stack declarada:** Next.js 16 + Vercel Hobby; Gemini 2.5 Flash free tier via Google AI Studio; Upstash Redis free tier; NextAuth v5/Google OAuth; Razorpay; Tailwind CSS; shadcn/ui; sem domínio próprio (subdomínio vercel.app).
- **Escopo:** 249 ferramentas em 20 categorias, com páginas estáticas/SEO, API routes, prompts estruturados, autenticação opcional, limites de uso, geração de documentos e pagamento Pro. O autor diz ter criado as ferramentas em cerca de duas semanas.
- **Arquitetura interessante:** 3 gerações gratuitas/dia; rate limiting no Redis; falha do Redis bloqueia a geração (fail-closed); login opcional para uso básico; OAuth para contas; HMAC/replay protection em webhooks; sete rodadas de auditoria de segurança relatadas.
- **Métricas declaradas na primeira semana:** 200+ visitantes únicos, 42 gerações, 22 ferramentas efetivamente usadas, 0 clientes pagantes; 47 visitas à página de preços; 137 impressões no Search Console e cerca de quatro páginas indexadas. Reddit teria enviado 48 dos primeiros 112 visitantes.
- **Lição comercial:** 249 ferramentas não geraram automaticamente compradores. O próprio autor relata conversão de 0% entre visitas à página de preços e compras naquele momento. Ferramentas úteis, fricção baixa e SEO não substituem intenção de compra e oferta.
- **Ressalva crítica de termos:** Vercel Hobby é oficialmente destinado a uso pessoal/não comercial. O artigo declara plano Pro e monetização, portanto essa combinação não deve ser copiada para uma operação comercial sem resolver a incompatibilidade de termos (plano/host adequado). Razorpay cobra taxa por transação; “US$0/mês” não quer dizer custo zero quando há receita. O Gemini free tier também tem condições de uso de dados diferentes do plano pago.
- **Valor para o MAK:** blueprint de arquitetura de ferramentas pequenas, geração estruturada, rate limiting, uso anônimo e páginas SEO. Não copiar o número 249 como objetivo nem assumir que a stack inteira é elegível para uso comercial.

### Caso C — Somnia: PWA local-first para diário de sonhos
- **Fonte:** https://www.reddit.com/r/ClaudeAI/comments/1rq28iw/built_a_full_pwa_with_localfirst_architecture/
- **Classificação:** FREE-TIER / CLAIMED; custo total de desenvolvimento não informado.
- **Stack declarada:** Claude + Copilot para desenvolvimento; PWA; IndexedDB no dispositivo para dados privados; Supabase guarda apenas perfil/plano; Vercel free tier.
- **Resultado declarado:** versão funcional construída em aproximadamente uma semana; 50+ deployments; arquitetura que evita armazenar entradas pessoais no servidor.
- **Lição técnica:** local-first reduz custo de armazenamento/sincronização e diminui exposição de dados sensíveis. PWA evita depender de publicação em lojas para testar a primeira versão.
- **Ressalvas:** o post não comprova custo zero das ferramentas de IA, nem escalabilidade infinita. Backups, sincronização, suporte, armazenamento e limites de hospedagem continuam sendo problemas a resolver. O plano Hobby da Vercel tem restrição não comercial.

### Caso D — Toolkiya: utilitários de PDF, imagem e OCR processados no cliente
- **Fonte:** https://www.reddit.com/r/nextjs/comments/1shsfw1/weekly_showoff_thread_share_what_youve_created/
- **Classificação:** FREE-TIER / CLAIMED; sem auditoria de custos.
- **Stack declarada:** Next.js 16, TypeScript, Tailwind, shadcn/ui, Vercel Hobby, Supabase Free; pdf-lib, pdfjs-dist, Canvas e Tesseract.js para processamento local; cascata de modelos gratuitos via OpenRouter, com fallback Gemini e Groq.
- **Arquitetura:** PDF/imagem/OCR executados no navegador quando possível; três camadas de rate limiting (local, IP e orçamento global); carregamento lazy e foco em performance.
- **Lição técnica:** processamento client-side pode eliminar upload de arquivos, custos de servidor e exposição desnecessária de dados. Modelos gratuitos podem servir como camada auxiliar, mas disponibilidade, termos, limites e privacidade variam por provedor.
- **Ressalva:** Vercel Hobby não deve ser tratado como hospedagem comercial gratuita; o relato não comprova volume de uso, segurança ou estabilidade.

### Caso E — HookMafia / HookLayer: duas ferramentas construídas por uma pessoa com IA
- **Fonte:** https://www.indiehackers.com/post/no-cs-degree-no-network-from-bangladesh-full-time-job-uber-i-built-2-ai-products-solo-and-just-got-into-the-chatgpt-app-directory-7fb47c3eec
- **Classificação:** BOOTSTRAPPED / COST UNKNOWN. Não é evidência de construção inteiramente gratuita.
- **Criador:** Ashifur Khan, sem formação em computação; relata trabalhar em emprego integral e dirigir Uber.
- **Produtos:** HookMafia (web app de hooks/roteiros e análise TikTok) e HookLayer (servidor MCP para Claude/ChatGPT).
- **IA/processo:** protótipo inicial com ChatGPT e Gemini; depois Claude Code; o autor também fez análise de produto, SEO, growth, analytics e suporte.
- **Métricas declaradas em agosto de 2026:** 1.227 usuários, 578 nos últimos 30 dias, 12 clientes pagantes, 6 assinaturas ativas, MRR de US$38 em junho, US$115 em julho e US$174 em agosto. Aprovação no diretório de apps do ChatGPT teria aumentado cadastros de ~7/dia para 50+/dia.
- **Lições:** IA amplia capacidade individual para além do código; instrumentação e correção do onboarding aumentaram ativação declarada de 10% para 39%; distribuição via diretório/ecossistema pode ser decisiva.
- **Limite:** autorrelato; não comprova custo zero, e Claude Code/API/infra podem ter custos.

### Caso F — RenderArchi: SaaS criado por arquiteta sem experiência em programação
- **Fonte:** https://www.indiehackers.com/post/from-architect-to-indie-hacker-how-i-built-my-first-saas-with-zero-code-and-hit-7-1-conversion-i7Rnlu1YqvZBTzhRdIEv
- **Classificação:** BOOTSTRAPPED / COST UNKNOWN.
- **Stack declarada:** templates open source do GitHub, Cursor e ferramentas de IA para produto de renderização arquitetônica.
- **Métricas declaradas:** cerca de 3 meses para MVP; 100 usuários orgânicos na primeira semana após publicação em Xiaohongshu; primeira venda 20 dias depois; 2,5 mil usuários registrados após quatro meses; conversão declarada de 7,1%; receita total declarada de ~US$1.500.
- **Lições:** começar de problema vivido pela pessoa; testar com profissionais conhecidos; remover cadastro antes do primeiro valor; preço e free tier precisam cobrir custos reais.
- **Limite:** o custo de Cursor, APIs e infraestrutura não está detalhado. Não classificar como R$0.

### Caso G — AssetShark: SaaS de depreciação construído com Replit AI
- **Fonte:** https://www.indiehackers.com/post/i-vibe-coded-an-entire-saas-in-a-few-months-with-replit-heres-what-i-learned-e49fd68dcb
- **Classificação:** BOOTSTRAPPED / COST UNKNOWN; ainda em validação.
- **Stack declarada:** Replit AI Agent, React frontend e Node backend; criador diz que todo o código foi produzido por prompts.
- **Produto:** rastreamento de ativos e cálculo de depreciação para pequenas empresas australianas, usando taxas oficiais ATO.
- **Estado declarado:** produto publicado e funcional, calculadora gratuita, 24 páginas SEO; quatro beta users no momento do post.
- **Lição:** IA acelera a construção, mas o próprio criador diz que adquirir usuários é muito mais difícil que construir.
- **Limite:** custos do Replit e infraestrutura não foram esclarecidos; não é caso confirmado de custo zero.

### Caso H — HypeDesk: plataforma de promoção de startups
- **Fonte:** https://www.indiehackers.com/post/after-6-months-of-work-and-1200-in-revenue-i-made-my-saas-free-for-everyone-466e4ae94f
- **Classificação:** BOOTSTRAPPED / COST UNKNOWN.
- **Produto:** diretório/gestão de locais para divulgar startups, geração de materiais com IA, extensão Chrome para preencher formulários e colaboração.
- **Métricas declaradas:** aproximadamente 60 vendas e US$1.200 nos primeiros seis meses; após liberar tudo, ~20 cadastros/dia.
- **Lição:** construir uma plataforma não é o mesmo que distribuir; o autor mudou o modelo para tentar ampliar uso e monetizar recursos avançados.
- **Limite:** custos de construção e operação não informados; não é evidência de R$0.

### Caso I — MyClaw/Toolkiya/Stockroom: padrão comum de custo
Os três exemplos sugerem um padrão técnico mais útil que a quantidade de funcionalidades:
1. interface estática ou leve;
2. lógica determinística no navegador sempre que possível;
3. banco apenas para estado que precisa persistir ou sincronizar;
4. IA só na parte em que linguagem/geração agrega valor;
5. limites explícitos de uso;
6. exportação em formatos abertos;
7. deploy com plano gratuito cujos termos permitem o uso pretendido;
8. autenticação, backup, proteção de segredos e validação antes de dados reais.

## 3. Stack gratuita — mapa de candidatos e restrições oficiais

| Camada | Candidato | O que oferece | Limites / atenção |
|---|---|---|---|
| Desenvolvimento assistido | AppJet Free | AI coding, GitHub, checks, Supabase e deploy Cloudflare anunciados no plano gratuito | Limite semanal; fornecedor recente; revisar termos, privacidade e capacidade antes de uso real |
| Desenvolvimento assistido | GitHub Copilot Free | 2.000 completions/mês e modelos incluídos no plano Free | Limite mensal; não equivale a agente ilimitado |
| IA via API | Gemini API Free | acesso gratuito limitado a determinados modelos e tokens | limites variam por modelo; no Free, dados enviados podem ser usados para melhoria dos produtos; não enviar segredos/dados sensíveis |
| Hospedagem edge | Cloudflare Workers Free | até 100.000 requests/dia, 10 ms CPU por request e 128 MB memória conforme docs consultadas | CPU curta; limites por conta/recurso; confirmar termos do produto específico |
| Banco/auth | Supabase Free | Postgres, API, Auth e Storage com quotas | 2 projetos gratuitos; projetos pausam após 1 semana de inatividade; quotas e ausência de backups automáticos no Free |
| Hospedagem | Vercel Hobby | deploy e CDN gratuitos para projetos pessoais | **uso pessoal/não comercial**; não utilizar como base gratuita de operação comercial sem plano/termos compatíveis |
| UI | Tailwind / shadcn/ui | componentes e estilos open source | exigem revisão de acessibilidade, licença e implementação |
| Dados locais | IndexedDB / SQLite | persistência local/embedded sem serviço de banco pago | backups, concorrência, sincronização e durabilidade dependem da arquitetura |
| Processamento local | pdf-lib, pdfjs-dist, Canvas, Tesseract.js | PDF, imagem e OCR no navegador | desempenho depende do dispositivo; IA local não é a mesma coisa que API de modelo |
| Cache/limite | Upstash Redis Free | rate limiting e contadores no caso MyClaw | quota gratuita e termos precisam ser conferidos na ativação |

**Fontes oficiais e snapshots de preços:** Gemini API https://ai.google.dev/gemini-api/docs/pricing ; Supabase https://supabase.com/pricing e https://supabase.com/docs/guides/platform/billing-on-supabase ; Cloudflare Workers https://developers.cloudflare.com/workers/platform/limits/ ; Vercel Hobby https://vercel.com/docs/plans/hobby e termos https://vercel.com/legal/terms ; GitHub Copilot https://github.com/features/copilot/plans ; AppJet https://appjet.ai/.

Os limites são snapshots consultados em 26/11/2026 e podem mudar. Antes de cada implementação, revalidar preços, elegibilidade regional, limites, termos comerciais, privacidade e política de dados.

## 4. Arquitetura Kamikaze candidata: construir sem pagar por operação desnecessária

**Princípio:** não escolher uma stack por ser popular; escolher o menor conjunto que atende o problema e os termos do uso.

### Perfil 1 — ferramenta simples sem login
- HTML/CSS/JS ou Next.js estático.
- Processamento local no browser.
- Deploy Cloudflare Pages/Workers ou AppJet Free após validação de termos.
- Sem banco, sem autenticação, sem API paga.
- Ideal para calculadoras, conversores, validadores, geradores determinísticos e utilitários de arquivo.

### Perfil 2 — aplicação com estado individual
- Frontend web/PWA.
- IndexedDB ou SQLite local quando o dado pertence ao usuário/dispositivo.
- Supabase apenas quando login, sincronização ou dados compartilhados forem essenciais e os limites forem suficientes.
- Exportação CSV/JSON/PDF para portabilidade e backup.
- Separar dados pessoais do processamento de IA sempre que possível.

### Perfil 3 — aplicação com IA
- Determinar primeiro se a IA é realmente necessária.
- Usar código determinístico para cálculos, regras, validações e transformações.
- IA em uma etapa limitada, com quotas, rate limit e fallback.
- Nunca expor API keys no frontend.
- Não enviar dados confidenciais a planos gratuitos sem avaliar termos de uso e treinamento.
- Registrar custo potencial por operação antes de abrir para público.

### Perfil 4 — sistema interno de microempresa
- Um fluxo principal, poucas telas, permissões mínimas e exportação.
- Banco/backup só quando o processo realmente exigir.
- Demonstrar com dados fictícios.
- Antes de dados reais: autenticação, autorização, logs, backups, restauração, validação de entradas e teste de segurança.

## 5. O que realmente aprendemos

1. **É possível construir um aplicativo full-stack funcional por R$0**, pelo menos em escopo de demonstração e limites de plano gratuito. Stockroom é a prova mais tangível desta rodada: código, demo e funcionalidades inspecionáveis.
2. **A maior alavanca não é gerar mais código; é desenhar para não precisar de infraestrutura paga.** Client-side, local-first, estático, SQLite e ausência de login podem eliminar serviços desnecessários.
3. **IA pode assumir parte substancial da implementação**, mas não elimina a necessidade de especificar regras, revisar código, testar fluxos, segurança e persistência.
4. **“US$0/mês” pode esconder incompatibilidade comercial.** Vercel Hobby é não comercial; uma stack gratuita não é automaticamente elegível para monetização.
5. **IA via API gratuita pode ter custo de privacidade.** Gemini Free declara que o conteúdo pode ser usado para melhorar produtos; não usar com dados sensíveis/confidenciais.
6. **Ferramentas grátis podem produzir tráfego sem compradores.** MyClaw: 200+ visitantes, 42 gerações, 0 pagantes no snapshot. Construir não resolve distribuição.
7. **Escopo pequeno e verticalizado é mais valioso que centenas de ferramentas genéricas.** 22 de 249 ferramentas foram usadas no MyClaw na primeira semana; o criador aponta o gerador de faturas como mais usado que as ferramentas de conteúdo.
8. **O melhor ativo pode ser uma capacidade reutilizável.** Um fluxo de especificação → geração → revisão → teste → deploy → feedback pode produzir diferentes soluções conforme a oportunidade validada.

## 6. Aplicação ao Kamikaze — sem aprovar implementação ainda

- O caso Stockroom deve ser estudado como referência de produto full-stack gerado por IA, incluindo schema, API, lógica transacional, validações, exportação e estrutura de repositório.
- MyClaw deve ser estudado como referência de biblioteca de ferramentas pequenas, prompts estruturados, quotas e SEO, mas não como prova de monetização.
- Somnia e Toolkiya devem ser referências para arquitetura local-first/client-side.
- HookLayer e RenderArchi devem ser referências de capacidade individual ampliada por IA e iteração com usuários, não de custo zero.
- Não instalar AppJet, Copilot, n8n, banco, SDK ou qualquer ferramenta agora; não conectar contas, criar apps, publicar, fazer deploy ou gastar.
- Não mexer no Google AI Studio/NEXUS nem presumir quota livre.
- A arquitetura final depende da oportunidade escolhida e da revalidação de termos no momento de uso.
- Esta pesquisa não muda o orçamento operacional de R$0 nem aprova PHASE_04.

## 7. Lacunas para próxima rodada
- Auditar a implementação Stockroom por arquivos-chave: schema, transações de movimentação, validação, export, testes e Docker/persistência.
- Confirmar termos de uso, privacidade e limites do AppJet, especialmente uso comercial e retenção de código/dados.
- Encontrar mais casos brasileiros e relatos independentes de construção com R$0 real, não apenas sem investimento externo.
- Separar “IA usada para programar” de “IA incorporada no produto”; comparar custos e limites de cada modalidade.
- Investigar ferramentas open source que rodam localmente no notebook 8 GB, sem API paga, e fluxos que funcionam no celular/tablet.
- Não transformar a pesquisa em catálogo infinito: selecionar casos com artefatos inspecionáveis e valor técnico/comercial demonstrável.
