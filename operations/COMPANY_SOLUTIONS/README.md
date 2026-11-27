# Motor de Diagnóstico e Soluções Empresariais (MDSE)

**Projeto:** NEGÓCIO DIGITAL KAMIKAZE  
**Estado:** DOCUMENTADO / PLANEJAMENTO OPERACIONAL — NÃO ATIVADO  
**Versão:** 1.0  
**Data:** 26/11/2026

## Objetivo
Operar ciclos de descoberta de **20 empresas únicas**, analisar e ranquear as oportunidades, selecionar as melhores, decidir quais merecem contato ou prototipagem, registrar cada decisão e impedir que empresas já processadas reapareçam como novas oportunidades sem uma justificativa explícita de reavaliação.

A operação pode atender empresas de diferentes setores e regiões. Não existe vertical obrigatório.

## Comece por aqui
1. [CONTROL_TOWER.md](CONTROL_TOWER.md) — estado e painel central.
2. [REGISTERS/COMPANY_MASTER_REGISTER.md](REGISTERS/COMPANY_MASTER_REGISTER.md) — registro único de empresas e deduplicação.
3. [REGISTERS/CONTACT_AND_SUPPRESSION_REGISTER.md](REGISTERS/CONTACT_AND_SUPPRESSION_REGISTER.md) — histórico de contato, recusas e bloqueios.
4. [REGISTERS/REVENUE_AND_COST_REGISTER.md](REGISTERS/REVENUE_AND_COST_REGISTER.md) — receitas, custos e recorrência.
5. [BATCHES/README.md](BATCHES/README.md) — rodadas de 20 empresas.
6. [COMPANIES/README.md](COMPANIES/README.md) — dossiês individuais.
7. [PROJECTS/README.md](PROJECTS/README.md) — projetos vendidos e entregas.
8. [RECURRING/README.md](RECURRING/README.md) — contratos e mensalidades.
9. [PLAYBOOKS/RANKING_AND_DECISION_RULES.md](PLAYBOOKS/RANKING_AND_DECISION_RULES.md) — ranking, gates e seleção.
10. [PLAYBOOKS/STATUS_TAXONOMY.md](PLAYBOOKS/STATUS_TAXONOMY.md) — estados separados.
11. [PLAYBOOKS/RESEARCH_AND_CONTACT_GOVERNANCE.md](PLAYBOOKS/RESEARCH_AND_CONTACT_GOVERNANCE.md) — pesquisa, privacidade e contato.

## Princípios não negociáveis
- Um registro canônico por empresa. Um novo lote não cria uma segunda identidade para o mesmo negócio.
- Cada lote contém exatamente 20 empresas únicas qualificadas para triagem; candidatos incompletos ficam em uma fila de pesquisa, não contam como empresas analisadas.
- A classificação é comparativa e baseada em evidências; score não é probabilidade estatística calibrada.
- Registrar as 20 empresas e explicar por que cada uma foi ou não priorizada.
- Não contatar automaticamente as 20. Seleção para contato é decisão separada.
- Empresa não contatada por baixa prioridade pode voltar à fila em reavaliação justificada. Recusa explícita, opt-out e pedido para não contatar geram supressão.
- Não confundir ausência de resposta com recusa, nem proposta com venda.
- Protótipo demonstrativo não é implantação nem prova de resultado.
- Cada projeto, contrato recorrente, receita e despesa tem registro próprio e vínculo por ID.
- Nenhum contato, publicação, cadastro, integração, deploy, compra ou gasto externo ocorre sem autorização aplicável.
- Orçamento operacional autorizado: R$0. Não armazenar saldo, dívida ou compromissos financeiros pessoais neste módulo.

## Limite desta estrutura
Este é um sistema documental-operacional. Não é CRM automatizado, não consulta empresas em segundo plano, não envia mensagens e não atualiza sozinho. Os registros devem ser atualizados durante a execução e verificados após cada rodada.
