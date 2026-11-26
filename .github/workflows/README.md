# GitHub Actions — Workflows

## Documentation quality
- Arquivo: [docs-quality.yml](docs-quality.yml).
- Disparadores: push para `main`, pull request para `main` e execução manual.
- Etapas: validação Python da estrutura/sincronização, build MkDocs e markdownlint.
- Permissões: `contents: read`.
- O workflow não publica o site e não modifica arquivos.

## Limites
Um check vermelho informa que a documentação não passou. Para bloquear merges, o repositório precisa exigir o check em branch protection/rulesets; isso não foi configurado nesta rodada.
