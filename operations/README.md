# Operations — Índice operacional do Kamikaze

Esta pasta contém controles de execução e registros estruturados da operação.

## Prioridade operacional atual

1. [Operação Primeira Venda](FIRST_SALE/README.md) — piloto comercial ativo, com oferta e lote inicial de candidatos. A demonstração ainda não foi produzida; nenhum contato realizado.
2. [Estado estruturado canônico do projeto](state.toml) — prioridade, frentes, próxima ação, execução, restrições e métricas.
3. [Estado humano](STATE.md) — explicação compacta do estado estruturado.
4. [Histórico preservado](STATE_HISTORY.md) — snapshots antigos.
5. [Recursos disponíveis](AVAILABLE_RESOURCES.md) — inventário de ferramentas e capacidades.
6. [Company Solutions](COMPANY_SOLUTIONS/README.md) — sistema de ranking empresarial documentado; usar apenas se necessário.

## Relação entre os módulos

- FIRST_SALE guarda a oferta e o experimento comercial específico. O lote de candidatos é uma fila de descoberta, não um lote de 20 empresas já qualificadas.
- COMPANY_SOLUTIONS é o registro mestre para deduplicação, qualificação, ranking, histórico de contato, projetos e recorrência quando for ativado.
- Só promover um candidato ao registro mestre depois de confirmar identidade, atividade, presença digital e oportunidade observável. Usar um Company ID único; não manter dossiês duplicados.
- A estrutura Company Solutions permanece DOCUMENTADA / NÃO ATIVADA; esta regra não autoriza pesquisa adicional, contato ou publicação.

## Regras

- state.toml é a fonte estruturada do estado do projeto: prioridade entre frentes, próxima ação, execução ativa, fase/gate, limites e métricas. Não existe ponteiro manual de última entrega.
- A operação de primeira venda é um piloto paralelo; sua situação comercial está em FIRST_SALE.
- Registros históricos ficam em STATE_HISTORY.md e logs.
- Não inserir senhas, tokens ou dados pessoais desnecessários.
- Não iniciar contatos, propostas, contratos, despesas ou deploys sem autorização explícita.
