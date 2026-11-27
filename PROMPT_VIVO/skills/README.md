# Skills operacionais do Kamikaze

Skills são instruções especializadas e reutilizáveis. Elas orientam a IA quando o usuário ou o fluxo as aciona; não são agentes autônomos, não executam trabalho em segundo plano e não criam acesso a ferramentas que o ambiente não possui.

## Skills disponíveis

| Skill | Quando usar | Resultado |
|---|---|---|
| [Human Writing](human-writing/SKILL.md) | Posts, mensagens, propostas, páginas e textos que precisam soar naturais e manter a voz do autor | Texto claro, específico, com ritmo natural e sem padrões genéricos de IA |
| [Business Opportunity Intelligence](business-opportunity-intelligence/SKILL.md) | Descobrir gargalos, comparar mercados, avaliar oportunidades e decidir o que testar | Dossiê crítico com evidências, riscos, economia, adequação ao operador e experimento mínimo |

## Regras de uso

- Ler a skill antes de iniciar a tarefa correspondente.
- Não tratar score como probabilidade estatística nem como verdade objetiva.
- Não inventar experiência, depoimentos, métricas, entrevistas ou resultados.
- Separar pesquisa secundária (web) de validação primária (conversa, teste, pagamento).
- Se o ambiente não oferecer agentes paralelos, simular as perspectivas em sequência e deixar claro que são lentes analíticas da mesma IA, não opiniões independentes.
- Toda ação externa permanece sujeita às autorizações do projeto.

## Referências de origem e inspiração

As skills foram escritas para o contexto e as restrições do Kamikaze, após examinar abordagens públicas:
- [shir-danishyar/humanize](https://github.com/shir-danishyar/humanize) — escrita natural, registro, calibração de voz e auditoria de padrões.
- [gabrieldejesusrodrigues/agent-skills — startup-idea-validator](https://github.com/gabrieldejesusrodrigues/agent-skills/tree/main/skills/startup-idea-validator) — perspectivas de produto, negócio e advogado do diabo.
- [tronghieu/agent-skills — market-researcher](https://github.com/tronghieu/agent-skills/tree/main/skills/market-researcher) — pesquisa com fontes, concorrentes, demanda, triangulação e limites de pesquisa.

Não houve importação literal de código desses repositórios. As instruções foram redigidas para este projeto.
