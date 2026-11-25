# Estado operacional

**Última atualização:** 25/11/2026  
**Fase:** pesquisa exploratória ampla — mineração de problemas em comunidades  
**Hipótese principal:** nenhuma; H1 rebaixada a hipótese provisória até nova evidência  
**Receita obtida neste projeto:** R$ 0  
**Despesas:** R$ 0  
**Experimento ativo:** nenhum iniciado. Pesquisa exploratória em andamento.

## Objetivo imediato

Buscar R$ 200 em até sete dias sem investimento inicial. Meta aspiracional, não garantia.

## Decisões vigentes

- Validar problema e disposição de pagamento antes de desenvolver.
- Começar com serviço manual e ferramentas gratuitas.
- Não construir SaaS ou aplicativo nesta fase.
- Não pagar APIs, hospedagem, anúncios ou assinaturas.
- Não usar dados reais de clientes em demonstrações.
- A hipótese H1 é provisória e pode ser descartada.

## O que foi feito

- Repositório criado e estrutura documental inicial registrada.
- Brief e princípios de trabalho definidos.
- Pesquisa inicial de casos de vibe coding e pequenos negócios registrada.
- H1 documentada como hipótese, sem validação comercial.

## O que falta

1. Mapear assistências técnicas independentes na região.
2. Conversar com pelo menos cinco responsáveis.
3. Registrar dores e processos atuais.
4. Decidir se H1 merece protótipo.
5. Fazer uma oferta real e medir resposta.

## Próxima ação recomendada

Antes de programar, preparar uma lista de cinco assistências e iniciar conversas curtas de descoberta. Atualizar este arquivo com respostas agregadas, objeções e decisões.

## Registro de decisões

| Data | Decisão | Motivo |
|---|---|---|
| 25/11/2026 | Priorizar validação comercial antes de software | Prazo curto, orçamento zero e risco de construir sem compradores |
| 25/11/2026 | Registrar H1 como hipótese, não como negócio validado | Ainda não houve entrevistas nem pagamentos |

## Nova orientação de pesquisa — 25/11/2026

O usuário autorizou pesquisa exploratória ampla, com registro contínuo diretamente neste repositório. Não limitar a pesquisa a assistência técnica, odontologia, programação ou aos exemplos citados. Explorar comunidades e nichos diversos, especialmente Reddit, procurando problemas concretos, pedidos de ajuda sem resposta satisfatória, soluções improvisadas, reclamações recorrentes e sinais de pagamento.

### Protocolo de registro
- Registrar cada achado com URL original, comunidade, data de acesso, resumo fiel, tipo de evidência e grau de confiança.
- Separar relato individual, padrão recorrente, evidência comercial (preços/compras/concorrentes) e hipótese nossa.
- Nunca inferir disposição de pagamento apenas de uma reclamação.
- Guardar fontes e observações em arquivos brutos por lote; sintetizar depois em documentos próprios.
- Explorar formatos diversos: serviço manual, produto digital, conteúdo, ferramenta, curadoria, intermediação etc.; não presumir software.
- Respeitar R$ 0, execução solo, distribuição sem anúncios e complexidade de pagamentos internacionais.
- Nenhuma oportunidade é aprovada antes de validação com compradores.

### Correção de escopo
A H1 (acompanhamento de orçamentos para assistências) não é prioridade nem hipótese principal. O usuário já havia contatado assistências anteriormente para buscar trabalho/aprendizado, não para validar uma oferta comercial. Não repetir esses contatos como se fossem entrevistas de mercado.

### Próxima etapa
Executar lotes de pesquisa diversificados, registrar evidências diretamente em research/, e só depois comparar oportunidades. A pesquisa não deve ser tratada como concluída em uma única sessão.
## Auditoria de ferramentas de pesquisa de mercado — 25/11/2026

- `research/TOOLS_AND_REPOSITORIES_AUDIT.md`: auditoria comparativa de repositórios open source, metadados de stars/commits, capacidades, dependências, custos, limitações e relatos de Reddit.
- `research/TOOLS_QUICKSTART.md`: comandos de instalação/diagnóstico/teste para Pain Miner, Reddit Research MCP e Trend Opportunity Radar.
- `.agents/skills/market-opportunity-scout/SKILL.md`: skill local original com protocolo de pesquisa amplo, sinais comerciais S0–S4, contraprovas, diversidade de formatos e regras de memória.

### Decisão técnica provisória
- Primeiro candidato a teste local: `AdvancingTitans/pain-miner` (MIT; coleta pública declarada sem chave/conta Reddit; exige Python e depende de disponibilidade das fontes). Ainda não instalado nem executado.
- Complemento potencial: `dialog-tools/reddit-research-mcp` (MIT; 268 stars/106 commits no snapshot; exige cliente MCP compatível e OAuth do serviço). Não presumir suporte direto no app ChatGPT Android.
- Referência de rigor metodológico: `datou202307-design/trend-opportunity-radar` (MIT; 44 commits; usa adaptadores/MCP de terceiros para coleta real).
- Referência de validação e concorrência posterior: `ferdinandobons/startup-skill` (MIT; alta adoção, mas alto consumo de tokens segundo README).
- Nenhum projeto é considerado validado por receita. Histórias de MRR no Reddit são autodeclaradas e não auditadas.

### Estado de execução
Os repositórios foram estudados por README, SKILL.md, changelog/metodologia, metadados e histórico recente de commits. Não foram clonados, instalados ou executados localmente. Não afirmar teste funcional.

### Próximo passo
Se houver acesso a um ambiente Python, testar Pain Miner com diagnóstico primeiro e comparar o resultado com pesquisa manual. Só depois decidir se vale instalar um MCP ou uma skill multiplataforma.