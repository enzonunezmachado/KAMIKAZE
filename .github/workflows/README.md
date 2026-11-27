# GitHub Actions — Workflows

## Documentation quality

- Arquivo: [docs-quality.yml](docs-quality.yml).
- Disparadores: push para `main`, pull request para `main` e execução manual.
- Etapas: validação Python da estrutura/sincronização, build MkDocs e markdownlint.
- Permissões: `contents: read`.
- O workflow não publica o site e não modifica arquivos.

## Deploy do GitHub Pages via MkDocs

- Arquivo: [deploy-pages.yml](deploy-pages.yml).
- Disparadores: alterações em `portfolio_site/docs/**`, `mkdocs.yml`, `requirements-docs.txt` ou no próprio workflow, em push para `main`; também permite execução manual.
- Build: instala as dependências de `requirements-docs.txt` e executa `mkdocs build --strict`.
- Publicação: envia exclusivamente `portfolio_site/site/` como artefato do GitHub Pages.
- Permissões: leitura do repositório no build; `pages: write` e `id-token: write` apenas no job de deploy.
- O workflow usa o ambiente `github-pages` e não altera arquivos-fonte.
- Pré-requisito único no repositório: em **Settings → Pages → Build and deployment → Source**, selecionar **GitHub Actions**. O workflow não substitui essa configuração administrativa.

## Limites

Um check vermelho informa que a documentação não passou. Para bloquear merges, o repositório precisa exigir o check em branch protection/rulesets; isso não foi configurado nesta rodada.
