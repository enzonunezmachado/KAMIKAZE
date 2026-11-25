# Estado operacional

**Última atualização:** 25/11/2026  
**Fase:** pesquisa de stack gratuita de agentes e desenho da operação  
**Hipótese principal:** nenhuma oportunidade validada  
**Receita obtida neste projeto:** R$ 0  
**Despesas:** R$ 0  
**Experimento ativo:** nenhum iniciado.

## Objetivo imediato

Buscar R$ 200 em faturamento sem investimento inicial. Meta aspiracional, não garantia.

## Decisões vigentes

- Validar problema e disposição de pagamento antes de desenvolver.
- Começar com serviço manual ou entrega simples e ferramentas gratuitas.
- Não pagar APIs, hospedagem, anúncios ou assinaturas antes de receita e aprovação explícita.
- Não construir SaaS ou aplicativo antes de sinais comerciais.
- Não usar dados reais de clientes em demonstrações públicas.
- Explorar mercados diversos; não restringir a tecnologia, assistência técnica ou experiências anteriores.
- Pesquisar até cinco oportunidades, mas produzir no máximo uma ou duas ofertas por ciclo.
- Agentes podem pesquisar e preparar rascunhos; contato, publicação, compra, deploy e ações irreversíveis exigem aprovação humana.

## O que foi feito

- Repositório e estrutura documental inicial criados.
- Brief e princípios de validação registrados.
- Pesquisa de repositórios de mineração de dores e skills documentada.
- Skill original `market-opportunity-scout` criada para pesquisa ampla.
- Auditoria de ferramentas e quickstart anteriores registrados.
- Pesquisa adicional de agentes gratuitos concluída documentalmente.
- Antigravity identificado como principal candidato de ambiente de execução: plano Free inclui CLI, skills, MCP e /swarm, com quota semanal variável.
- bitChat da bitbybit identificado como produto de atendimento/comércio, com plano gratuito limitado; não é um orquestrador geral de pesquisa.
- BitChat brasileiro identificado como ferramenta de atendimento WhatsApp com trial e planos pagos; não atende a custo zero contínuo.
- Reddit Research MCP e Pain Miner mantidos como ferramentas de coleta complementares.
- Nova skill `.agents/skills/zero-cost-opportunity-ops/SKILL.md` criada para coordenar descoberta, crítica, oferta, produção e auditoria.
- Pesquisa registrada em `research/FREE_AGENT_STACK_RESEARCH.md`.
- Guia de setup em `operations/ZERO_COST_STACK_QUICKSTART.md`.

## Decisões técnicas provisórias

1. **Primeira opção para testar:** Google Antigravity App/CLI `agy`, com conta Google pessoal Free. Tem subagentes, skills, MCP, navegador e /swarm; a quota é semanal e variável, não ilimitada.
2. **Memória operacional:** GitHub e arquivos Markdown do Projeto Sem Nome.
3. **Pesquisa Reddit:** Reddit Research MCP, se a conexão MCP e OAuth forem aprovados e funcionarem na versão instalada.
4. **Coleta batch:** Pain Miner, começando por `diagnose`; não rodar se as fontes estiverem bloqueadas.
5. **Complemento:** Google AI Studio/Gemini API Free para experimentos pontuais, respeitando modelos e limites do plano gratuito.
6. **Não instalar agora:** Ollama, OpenHands, Dify, Flowise, n8n, CrewAI ou LangGraph. Podem ser úteis depois, mas aumentam complexidade e dependências sem resolver a validação comercial inicial.
7. **Não usar AutoGen como base de novo projeto** sem avaliar o Microsoft Agent Framework, seu sucessor atual.
8. **Não presumir que BitChat/bitChat seja a plataforma desejada:** dois produtos distintos foram encontrados; nenhum substitui Antigravity como ambiente geral de agentes.

## O que ainda não foi feito

- Nenhuma ferramenta foi instalada, autenticada, clonada ou executada nesta sessão.
- Não testamos a quota do Antigravity na conta do usuário.
- Não confirmamos que o computador disponível executará o Antigravity confortavelmente.
- Não conectamos Reddit Research MCP.
- Não executamos Pain Miner.
- As oportunidades preliminares da pesquisa são pistas, não ofertas validadas nem evidência de vendas.

## Oportunidades preliminares para investigação

- Serviço de limpeza/padronização de CSV e planilhas para pequenos negócios/profissionais contábeis.
- Planilha de controle de inventário de bundles para vendedores Etsy.
- Curadoria e preparação original de materiais pedagógicos.
- Organização administrativa para profissionais autônomos.

Cada pista tem fonte e contraprova inicial em `research/FREE_AGENT_STACK_RESEARCH.md`. Nenhuma foi aprovada como negócio.

## Próxima ação recomendada

1. No computador Windows, instalar Antigravity CLI/desktop e confirmar versão, quota e memória disponível.
2. Abrir o repositório como workspace.
3. Carregar a skill `zero-cost-opportunity-ops`.
4. Testar uma tarefa curta com dois ou três agentes, sem enviar mensagens externas.
5. Conectar Reddit Research MCP somente depois de verificar OAuth e permissões.
6. Executar diagnóstico Pain Miner em ambiente Python.
7. Rodar um primeiro lote em três a cinco nichos e escolher no máximo uma oferta para validação.

## Registro de decisões

| Data | Decisão | Motivo |
|---|---|---|
| 25/11/2026 | Priorizar validação comercial antes de software | Prazo curto, orçamento zero e risco de construir sem compradores |
| 25/11/2026 | Registrar H1 de acompanhamento de orçamentos como hipótese, não como negócio validado | Não houve entrevistas nem pagamentos |
| 25/11/2026 | Testar Antigravity Free antes de montar framework próprio | Oferece ambiente de agentes, skills, MCP e /swarm sem assinatura, embora com quota |
| 25/11/2026 | Usar o GitHub como memória operacional | Persistência e continuidade entre ferramentas/sessões |
| 25/11/2026 | Pesquisar cinco hipóteses, produzir uma ou duas no máximo | Evitar dispersão e excesso de trabalho não vendido |
| 25/11/2026 | Não instalar stack local de modelos no primeiro ciclo | Hardware e setup podem custar mais tempo que o benefício |
