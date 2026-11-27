# NEGÓCIO DIGITAL KAMIKAZE

Operação independente para descobrir, validar, produzir e comercializar oportunidades digitais usando pesquisa, IA, ferramentas acessíveis e execução enxuta.

## Missão e limites atuais
- Pesquisar diferentes modelos digitais sem escolher antecipadamente nicho ou formato.
- Distinguir atenção, interesse, intenção, contratação, pagamento e recompra.
- Usar IA para ampliar pesquisa, análise e produção; não tratar IA como proposta de valor por si só.
- Orçamento operacional autorizado: R$0. Nenhuma ferramenta paga, API, hospedagem, anúncio ou assinatura sem autorização.
- Nenhuma publicação, mensagem, candidatura, contato, deploy ou compromisso externo sem autorização explícita.
- NEXUS e ATLAS são projetos separados.

## Acessos rápidos — apresentação

Use estes endereços quando precisar abrir o material em uma apresentação:

| Página | Abrir |
|---|---|
| **Portfólio / site público** | [Abrir no GitHub Pages](https://enzonunezmachado.github.io/KAMIKAZE/) |
| Código-fonte da página inicial | [index.md](portfolio_site/docs/index.md) |
| Estilos visuais do portfólio | [portfolio.css](portfolio_site/docs/assets/portfolio.css) |
| Repositório completo | [Abrir no GitHub](https://github.com/enzonunezmachado/KAMIKAZE) |

### Demonstrações e páginas futuras

Novas páginas públicas (demonstrações, ferramentas e projetos) devem receber um link direto nesta seção assim que forem criadas e publicadas. Não inserir links para páginas ainda inexistentes ou não verificadas.

> O endereço do GitHub Pages acima foi confirmado em uma implantação concluída com sucesso. A validação de qualidade da documentação ainda está separada e apresentou uma falha de sincronização do estado; isso não deve ser confundido com o resultado do deploy do Pages.

## Navegação principal

| Área | Finalidade | Entrada |
|---|---|---|
| Prompt Vivo | Métodos, instruções, memória e continuidade da IA | [README](PROMPT_VIVO/README.md) |
| Estado operacional | RUN_ID, fase/gate, orçamento e limites | [operations/STATE.md](operations/STATE.md) |
| Estado estruturado | Snapshot verificável por scripts/CI | [state.toml](operations/state.toml) |
| Último trabalho | Última entrega substantiva e próxima retomada | [CURRENT_WORK.md](PROMPT_VIVO/CURRENT_WORK.md) |
| Company Solutions | Lotes de empresas, ranking, dossiês, contatos, projetos e financeiro | [README](operations/COMPANY_SOLUTIONS/README.md) |
| Conhecimento | Pesquisas reutilizáveis e módulos especializados | [Knowledge index](PROMPT_VIVO/knowledge/README.md) |
| Execuções | Pesquisa separada por RUN_ID | [Runs index](PROMPT_VIVO/runs/README.md) |

## Continuidade e governança da IA
Antes de trabalhar, agentes devem ler [AGENTS.md](AGENTS.md). Para retomar conversas, seguir [BOOTSTRAP](PROMPT_VIVO/BOOTSTRAP.md). A arquitetura documental, autoridade, tamanho, leitura progressiva e regras de gravação estão em [ARCHITECTURE_GOVERNANCE.md](PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md).

O estado é separado do histórico: `state.toml` é a referência estruturada; `STATE.md` e `RUN_STATE.md` são snapshots humanos; `RESUME_PACKET.md` é um resumo curto; históricos e logs preservam eventos anteriores.

## Validação automatizada
- [Validador documental](scripts/validate_docs.py): verifica arquivos obrigatórios, limites de tamanho, links selecionados e sincronização TOML/Markdown.
- [GitHub Actions](.github/workflows/docs-quality.yml): executa validação, build MkDocs e lint Markdown em push/PR.
- [MkDocs](mkdocs.yml): gera um site estático a partir de arquivos Markdown.
- [Fonte do portfólio demonstrativo](portfolio_site/README.md): conteúdo em Markdown; ainda não publicado e sem cases reais.

## Regra comercial
O projeto não deve construir ferramentas, sites ou automações apenas porque são tecnicamente possíveis. Antes, deve identificar comprador, problema, evidência de procura, alternativas, canal de aquisição, capacidade de entrega, riscos e critério de validação. Ideias do usuário devem ser registradas e avaliadas, não descartadas automaticamente por não terem surgido na pesquisa da IA.
