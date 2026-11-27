# GitHub — Automação do repositório

Esta pasta contém configuração de automação executada pelo GitHub, não prompts de IA.

## Entrada

- [Workflows](workflows/README.md): automações disparadas por eventos do repositório.

## Segurança

- Workflows devem usar permissões mínimas.
- Não inserir secrets em logs ou arquivos.
- O workflow documental é somente leitura; o workflow de Pages constrói e publica somente o artefato estático gerado pelo MkDocs.
- A publicação do site é uma ação externa automatizada, limitada ao conteúdo de `portfolio_site/docs/` e à configuração do MkDocs.
