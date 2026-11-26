# Portfolio site — fonte Markdown

Este diretório contém a fonte do site demonstrativo do Kamikaze. O conteúdo é escrito em Markdown; o MkDocs apenas o transforma em HTML estático.

## Como funciona
- Configuração: `../../mkdocs.yml` (na raiz do repositório).
- Conteúdo: `docs/*.md`.
- Build local: `pip install -r ../../requirements-docs.txt` e depois `mkdocs build --strict` a partir da raiz.
- Saída: `site/` (gerada; não editar manualmente).

## Governança
- Não publicar o site sem autorização explícita.
- Não inventar clientes, depoimentos, resultados, certificações ou cases.
- Identificar exemplos fictícios e demos não implementadas.
- Atualizar a página de projeto somente após existir artefato funcional e verificado.
- A fonte editável é Markdown; HTML gerado não é a fonte de verdade.
