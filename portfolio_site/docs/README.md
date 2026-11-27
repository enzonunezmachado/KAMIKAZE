# Conteúdo do portfólio — páginas Markdown

Este diretório é a fonte editorial do site MkDocs. O HTML publicado é gerado pelo build; não editar a pasta de saída manualmente.

## Páginas e assets

- `index.md`: página inicial e apresentação do portfólio.
- `solucoes.md`: categorias em avaliação, não ofertas aprovadas.
- `projetos.md`: projetos demonstrativos; nunca inventar cases.
- `processo.md`: processo de trabalho e limites.
- `assets/kamikaze-base.css`: base visual escura e reutilizável do Kamikaze.
- `assets/portfolio.css`: ajustes específicos do tema MkDocs e componentes do portfólio.
- `assets/kamikaze.js`: aprimoramentos progressivos sem dependências; só ativa controles quando encontra os elementos correspondentes.

## Regras de conteúdo e manutenção

- Editar Markdown, não o HTML gerado.
- CSS e JavaScript são carregados por `extra_css` e `extra_javascript` em `mkdocs.yml`.
- O padrão reutilizável para novos sites está documentado em [web/README.md](../../web/README.md) e [web/AI_WEB_DEVELOPMENT_GUIDE.md](../../web/AI_WEB_DEVELOPMENT_GUIDE.md).
- Não publicar sem autorização.
- Não apresentar demo fictícia como cliente ou resultado real.
- Só afirmar que algo foi implementado/testado quando houver artefato e evidência.
