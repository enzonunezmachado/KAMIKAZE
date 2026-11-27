# Web — padrão de desenvolvimento de sites

## Objetivo
Esta pasta guarda o método reutilizável do Kamikaze para criar e manter sites pequenos, bonitos, responsivos e funcionais com HTML, CSS e JavaScript nativos.

## Ordem de leitura para agentes
1. [AI_WEB_DEVELOPMENT_GUIDE.md](AI_WEB_DEVELOPMENT_GUIDE.md) — instruções de execução, decisões técnicas e checklist.
2. [Starter template](templates/starter.html) — estrutura de referência para páginas novas.
3. CSS e JavaScript canônicos:
   - CSS base: [kamikaze-base.css](../portfolio_site/docs/assets/kamikaze-base.css)
   - JavaScript: [kamikaze.js](../portfolio_site/docs/assets/kamikaze.js)
   - CSS específico do portfólio: [portfolio.css](../portfolio_site/docs/assets/portfolio.css)

## Padrão visual obrigatório
- Tema escuro por padrão: azul-marinho, grafite e cinzas escuros.
- Texto em cinza-claro, sem branco estourado; contraste confortável e legível.
- Destaques discretos em azul frio; vermelho não deve dominar a interface.
- Layout limpo, hierarquia visual clara, bom espaçamento e componentes consistentes.
- Responsividade real para celular, tablet e desktop.
- Respeitar `prefers-reduced-motion` e foco visível por teclado.

## Stack padrão
- HTML semântico.
- CSS moderno com custom properties, Grid/Flexbox e mobile-first.
- JavaScript vanilla, modular por responsabilidade e sem dependências por padrão.
- Sem framework, biblioteca, build step ou serviço pago se HTML/CSS/JS resolverem.
- Bibliotecas externas só quando uma necessidade concreta justificar o custo, risco e manutenção.

## Regras de uso
- Antes de criar/modificar site, ler o guia e inspecionar o projeto existente.
- Reutilizar os assets canônicos quando compatíveis; não copiar código cegamente nem sobrescrever identidade específica.
- Separar conteúdo, estrutura, estilo e comportamento.
- Não adicionar JavaScript decorativo: cada interação precisa ter função clara e alternativa acessível.
- Não declarar responsividade, acessibilidade, funcionamento ou publicação sem testar.
- Não publicar/deployar sem autorização explícita.
- Manter o escopo proporcional: sites simples devem continuar simples.

## Manutenção
- Atualizar este índice se os arquivos mudarem.
- Atualizar o guia quando uma regra recorrente for aprendida ou corrigida.
- Os assets canônicos ficam no diretório de assets do portfólio para também poderem ser servidos pelo MkDocs; o starter mostra como referenciá-los dentro deste repositório. Ao iniciar outro site, copie os dois assets para a pasta `assets/` daquele projeto e ajuste os caminhos.

## Fontes de referência
As decisões práticas e links de referência ficam em [AI_WEB_DEVELOPMENT_GUIDE.md](AI_WEB_DEVELOPMENT_GUIDE.md).
