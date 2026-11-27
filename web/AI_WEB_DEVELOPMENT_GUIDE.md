# Guia de desenvolvimento web para IA — Kamikaze

**Papel:** instrução operacional reutilizável para criação, revisão e manutenção de sites.
**Público:** agentes de IA que trabalham neste repositório.
**Fonte visual canônica:** `portfolio_site/docs/assets/kamikaze-base.css`.
**Fonte de comportamento canônica:** `portfolio_site/docs/assets/kamikaze.js`.

## 1. Resultado esperado

Criar sites que pareçam produtos digitais bem cuidados, e não documentos sem personalidade. A página deve ter direção visual, hierarquia, composição, ritmo, tipografia, espaçamento, estados interativos e adaptação a diferentes telas.

O objetivo não é adicionar efeitos por adicionar. O objetivo é entregar uma experiência coerente, confiável, rápida, acessível e adequada ao propósito.

## 2. Protocolo obrigatório antes de codificar

1. Ler este guia e `web/README.md`.
2. Inspecionar a estrutura e os arquivos existentes do site. Identificar framework/build tool, pontos de entrada, CSS/JS, rotas e deploy atual.
3. Identificar finalidade, público, ação principal, conteúdo disponível e restrições.
4. Definir uma direção visual concreta: atmosfera, paleta, tipografia, layout, componentes e comportamento responsivo.
5. Preservar o que já funciona. Evitar reescrever tudo quando uma alteração localizada resolver.
6. Escolher a implementação mais simples que atende ao escopo.
7. Só então editar e testar.

Se faltarem informações essenciais sobre o propósito ou conteúdo, fazer uma pergunta objetiva. Não inventar clientes, métricas, depoimentos, certificações, funcionalidades ou integrações.

## 3. Direção visual padrão Kamikaze

### Paleta
- Fundo principal: azul-marinho/grafite muito escuro.
- Superfícies: tons escuros ligeiramente mais claros que o fundo.
- Texto principal: cinza-claro suave, não branco puro.
- Texto secundário: cinza azulado legível.
- Destaque: azul frio discreto; usar cor de estado apenas quando semanticamente necessária.
- Bordas: sutis, mas suficientes para separar superfícies.

### Composição
- Usar um container central com largura máxima coerente.
- Criar hierarquia forte: eyebrow/etiqueta, título principal, subtítulo, ação primária.
- Usar grids assimétricos ou colunas quando melhorarem a leitura; não transformar tudo em cards.
- Alternar blocos de conteúdo, áreas de destaque, listas e provas visuais.
- Evitar grandes áreas vazias sem intenção, páginas que parecem uma folha A4 e excesso de caixas repetidas.
- Criar profundidade com camadas, bordas, gradientes sutis e sombras discretas — sem exagero.
- Manter consistência de raios, espaçamento, tipografia e estados.

### Tipografia
- Preferir fontes de sistema por padrão, com fallbacks adequados.
- Usar tamanhos fluidos com `clamp()` para títulos quando fizer sentido.
- Manter largura de linha confortável e line-height suficiente.
- Não usar texto cinza tão escuro que desapareça no fundo.

### Movimento
- Transições curtas e discretas apenas para comunicar estado ou resposta.
- Respeitar `prefers-reduced-motion: reduce`.
- Não usar animações contínuas, parallax ou reveal que atrapalhem leitura/performance.

## 4. Arquitetura técnica padrão

Para um site estático simples, preferir:
```text
site/
├── index.html
├── pages/                 # apenas se houver várias páginas
├── assets/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── main.js
│   └── images/
└── README.md
```

- HTML contém estrutura e conteúdo.
- CSS fica em arquivo separado e organizado por tokens, base, layout, componentes, utilitários e media queries.
- JavaScript fica em arquivo separado, com funções pequenas e nomes claros.
- Imagens ficam em assets; usar formatos modernos quando possível e dimensões apropriadas.
- Não inserir CSS/JS inline salvo quando a plataforma exigir ou o exemplo for realmente mínimo.
- Para uma página muito pequena, não criar pastas vazias ou abstrações desnecessárias.

### CSS
- Centralizar cores, fontes, espaçamentos, raios e larguras em custom properties.
- Usar classes com nomes consistentes e escopo claro.
- Preferir Grid/Flexbox, unidades relativas e layouts fluidos.
- Evitar seletores excessivamente específicos, `!important` generalizado e valores repetidos.
- Não usar estilos inline para decisões visuais importantes.
- Começar pelo layout estreito (mobile-first) e ampliar conforme o conteúdo exigir.

### JavaScript
- Vanilla JS por padrão.
- Usar `defer` ou módulos para não bloquear a leitura do HTML.
- Verificar a existência do elemento antes de anexar comportamento.
- Preferir APIs nativas e progressive enhancement.
- Não criar botões sem ação real.
- Não guardar dados sensíveis no navegador; não inserir segredos ou chaves em código cliente.
- Evitar dependências, trackers, cookies e chamadas de rede sem necessidade e autorização.

## 5. Interações recomendadas

Usar apenas quando agregarem valor:
- Menu mobile com botão acessível, `aria-expanded` e fechamento coerente.
- Navegação por âncoras com foco e rolagem apropriados.
- Formulário com validação clara e feedback; não simular envio se não houver backend.
- Filtros, tabs, accordion ou modal apenas quando melhorarem uma tarefa real.
- Botão de voltar ao topo em páginas longas.
- Ano automático no rodapé.

Toda interação deve funcionar por teclado e toque, apresentar estado visível e ter rótulo compreensível.

## 6. Qualidade, acessibilidade e segurança

Antes de concluir:
- [ ] HTML semântico: `header`, `nav`, `main`, `section`, `footer` conforme o conteúdo.
- [ ] Um título `h1` principal e hierarquia de headings coerente.
- [ ] Links descrevem o destino; botões executam ações.
- [ ] Imagens informativas têm texto alternativo; decorativas usam alt vazio.
- [ ] Foco de teclado visível e ordem de tabulação lógica.
- [ ] Contraste legível; não depender apenas da cor para comunicar estado.
- [ ] Layout testado em largura móvel, tablet e desktop.
- [ ] Sem rolagem horizontal inesperada.
- [ ] Menu e controles funcionam com teclado e toque.
- [ ] Movimento reduzido respeitado.
- [ ] Console sem erros relevantes; links e assets verificados.
- [ ] Sem dados, formulários, links, resultados ou integrações inventados.
- [ ] Nenhuma publicação/deploy sem autorização.

Não afirmar conformidade WCAG completa apenas por checklist manual. Registrar o que foi efetivamente testado e o que não foi.

## 7. Processo de trabalho

1. **Inspecionar:** descobrir o que existe e como é executado.
2. **Planejar:** definir a estrutura da página e direção visual antes de escrever código.
3. **Construir:** implementar HTML, CSS e JS separados.
4. **Executar localmente:** usar o servidor/build já adotado pelo projeto; não presumir que está rodando.
5. **Verificar:** abrir no navegador quando houver ferramenta disponível; conferir desktop e mobile, interações, links, console e erros.
6. **Corrigir:** resolver problemas observados, não fazer alterações cosméticas aleatórias.
7. **Registrar:** atualizar README e documentação do site com comandos, estrutura e limitações.
8. **Entregar:** informar arquivos alterados, testes realmente executados e pendências.

Se não houver navegador/ambiente visual disponível, validar o que for possível por build, lint e inspeção do código; declarar claramente que a aparência não foi conferida visualmente.

## 8. Regras para MkDocs e sites existentes

- Para o portfólio atual, a fonte é `portfolio_site/docs/*.md`; CSS e JS são carregados por `mkdocs.yml`.
- Não editar `portfolio_site/site/`, pois é saída gerada.
- O CSS específico do portfólio pode sobrescrever tokens/componentes genéricos, mas não deve duplicar toda a base sem necessidade.
- Antes de mexer em deploy, inspecionar workflows e configuração Pages; não assumir que um deploy concluído publica a saída MkDocs correta.
- Preservar URLs e navegação existentes, verificando os links após mudanças.

## 9. Fontes de referência consultadas

- [MDN — HTML: boas práticas em acessibilidade](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Core/Accessibility/HTML): semântica HTML, controles nativos, teclado e benefícios de estrutura correta.
- [MDN — CSS e JavaScript: boas práticas de acessibilidade](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/CSS_and_JavaScript): contraste, foco, animação, semântica e evitar JavaScript excessivo.
- [MDN — Design responsivo](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design): abordagem mobile-first, media queries e layouts flexíveis.
- [web.dev — Learn Responsive Design](https://web.dev/learn/design): tipografia, imagens, temas, acessibilidade e interação responsiva.
- [Chrome for Developers — CSS moderno](https://developer.chrome.com/docs/modern-web-guidance/guides/css/css?hl=en): design tokens, custom properties e organização em camadas.

Essas referências são guias de consulta, não motivo para instalar ferramentas ou frameworks em todo projeto.


## 10. Trava contra regressão do portfólio MkDocs

O portfólio publicado não pode voltar silenciosamente ao layout padrão de documentação. A estrutura visual é implementada em `portfolio_site/theme/main.html`, não apenas por CSS sobre o sidebar do tema.

- O tema MkDocs deve manter `custom_dir: portfolio_site/theme`.
- A página inicial e as páginas internas devem usar o shell personalizado, com cabeçalho, navegação, conteúdo e rodapé.
- Depois de `mkdocs build --strict`, executar obrigatoriamente `python scripts/validate_portfolio_build.py`.
- O validador verifica a presença do shell, navegação, rodapé, CSS escuro e páginas públicas geradas. Se a personalização desaparecer, a publicação deve falhar.
- O workflow `.github/workflows/deploy-pages.yml` executa essa verificação antes de criar o artefato do GitHub Pages. Não remover nem enfraquecer a validação para contornar falhas; corrigir a causa.
- Uma build verde prova estrutura e arquivos gerados, não prova fidelidade visual em navegador. Quando não houver navegador disponível, declarar essa limitação e solicitar captura de tela para conferência final.
