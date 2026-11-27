# Portfolio site — fonte Markdown

Este diretório contém a fonte do site demonstrativo do Kamikaze. O conteúdo é escrito em Markdown; o MkDocs o transforma em HTML estático.

## Como funciona

- Configuração: [mkdocs.yml](../mkdocs.yml), na raiz do repositório.
- Dependências: [requirements-docs.txt](../requirements-docs.txt).
- Conteúdo: `docs/*.md`.
- Base visual reutilizável: `docs/assets/kamikaze-base.css`.
- Ajustes específicos do portfólio: `docs/assets/portfolio.css`.
- JavaScript progressivo: `docs/assets/kamikaze.js`.
- Padrão de criação de novos sites: [web/README.md](../web/README.md).
- Build local: instalar as dependências e executar `mkdocs build --strict` a partir da raiz.
- Servidor local com recarga automática: `mkdocs serve`.
- Saída: `portfolio_site/site/` (gerada; não editar manualmente).

## Governança

- Não publicar o site sem autorização explícita.
- Não inventar clientes, depoimentos, resultados, certificações ou cases.
- Identificar exemplos fictícios e demos não implementadas.
- Atualizar a página de projeto somente após existir artefato funcional e verificado.
- A fonte editável é Markdown; HTML gerado não é a fonte de verdade.
