# Playbooks de criação web — prompts operacionais

**Uso:** copie apenas o roteiro correspondente à etapa atual. Preencha os campos entre colchetes. Não execute todas as etapas novamente se a informação já estiver disponível.

## Regras rápidas de design

- **Hierarquia:** uma mensagem principal por tela; título, apoio e ação devem ter pesos visuais distintos.
- **Composição:** alinhar elementos a um grid; variar blocos e proporções; não transformar tudo em cards.
- **Largura:** fundos e faixas podem ocupar 100%; aplique max-width e padding horizontal uma única vez no container interno. Evite wrappers aninhados com limites e paddings duplicados.
- **Espaço:** usar espaçamento consistente; agrupar o que pertence junto e separar o que é diferente.
- **Tipografia:** no máximo 2 famílias; poucos pesos; títulos com escala clara; parágrafos com largura confortável.
- **Cor:** definir fundo, superfície, texto, texto secundário, borda e uma cor de ação; checar contraste real.
- **Identidade:** repetir 2–3 elementos reconhecíveis (tipografia, forma, ritmo, cor ou padrão), sem decorar por decorar.
- **Responsividade:** adaptar composição e prioridade do conteúdo, não apenas encolher colunas.
- **Acessibilidade:** HTML semântico, teclado, foco visível, rótulos claros, alt adequado e movimento reduzido.
- **Interação:** todo controle precisa ter uma função real, estado visível e comportamento por teclado/toque.

## 1. Entender e delimitar

```text
Inspecione o projeto existente antes de alterar qualquer coisa.
Objetivo: [o que a página precisa alcançar]
Público: [quem vai usar]
Ação principal: [o que a pessoa deve fazer]
Conteúdo disponível: [textos, imagens, dados]
Restrições: [prazo, stack, integrações, orçamento]

Resuma em até 5 tópicos: estrutura necessária, conteúdo ausente, riscos e menor entrega útil.
Não invente informações. Se faltar algo que bloqueie a execução, faça uma única pergunta objetiva.
Não proponha framework ou dependência se HTML/CSS/JS resolverem.
```

## 2. Definir direção visual

```text
Com base no objetivo e no público, proponha UMA direção visual concreta.
Defina: personalidade em 3 palavras, paleta com função para cada cor, tipografia,
grid/container, hierarquia da primeira dobra, ritmo das seções e comportamento mobile.
Use contraste, alinhamento, escala, espaço e repetição para criar identidade.
Evite template genérico, excesso de cards, efeitos gratuitos e decoração sem função.
Mostre a estrutura da página em um wireframe textual curto antes de codificar.
```

## 3. Construir ou modificar

```text
Implemente a direção aprovada no projeto existente.
Primeiro localize os pontos de entrada e preserve o que já funciona.
Separe estrutura, estilo e comportamento; reutilize tokens e componentes existentes.
Faça mobile-first, HTML semântico, CSS organizado e JavaScript vanilla progressivo.
Não crie controles falsos, conteúdo fictício, dependências ou arquivos desnecessários.
Altere o mínimo de arquivos necessário e explique decisões não óbvias.
```

## 4. Auditar a experiência

```text
Revise a página como designer, usuário e QA — não apenas como programador.
Verifique desktop e mobile: hierarquia, alinhamento, largura, espaçamento, tipografia,
contraste, consistência, densidade, cortes, overflow, navegação e ação principal. Confirme que header, conteúdo e footer compartilham o mesmo eixo interno, sem container/padding duplicado.
Teste teclado, foco, links, botões, formulários e estados interativos.
Liste somente problemas observáveis, classificados por impacto: bloqueador, alto, médio, baixo.
Não declare inspeção visual se não abriu a página em navegador/captura real.
```

## 5. Corrigir sem mascarar

```text
Corrija estes problemas observados: [lista de problemas/evidências].
Encontre a causa na estrutura, no container, no fluxo ou na regra de estilo responsável.
Não aplique remendos globais, !important indiscriminado ou offsets para esconder o sintoma.
Faça a menor correção coerente, preserve outras telas e rode as validações disponíveis.
Compare novamente o estado corrigido com o problema original.
```

## 6. Fechar e registrar

```text
Antes de concluir, informe:
- arquivos alterados e finalidade;
- build/testes realmente executados e resultado;
- telas, larguras e interações efetivamente verificadas;
- limitações que continuam abertas;
- instruções para reproduzir a validação.

Atualize o guia somente se surgiu uma regra reutilizável, não por causa de uma correção isolada.
Não confunda build verde com qualidade visual. Não publique nem faça deploy sem autorização.
```

## Regra de uso

Escolha o menor roteiro que resolve a etapa. Não cole todos os prompts em toda tarefa. Se a solicitação for uma correção pequena, vá direto ao roteiro 5; se for um site novo, use 1 → 2 → 3 → 4 → 6. O roteiro 4 exige evidência visual real quando a aparência for parte do resultado.

## Referências que fundamentam os critérios

- **Fundamentos e identidade:** 4 The Creatives — Fundamentos de Design e Brand Identity; Canva Design School — Graphic Design Essentials; HubSpot Academy — Graphic Design Fundamentals.
- **Composição e fundamentos em português:** Cursa — Os Fundamentos do Design; curso de design gráfico Profissionaliza+.
- **Interface e responsividade:** web.dev — Learn Design / Learn Responsive Design; MDN — Aprendendo desenvolvimento web; freeCodeCamp — Responsive Web Design.
- **Implementação prática:** CodigoZero — HTML, CSS e JavaScript; RNP — Desenvolvimento Frontend.
- **Acessibilidade:** MDN — Accessibility; Escola Virtual de Governo — eMAG Desenvolvedor.

Os cursos são fontes de princípios, não checklists para copiar. Os roteiros acima convertem esses princípios em decisões e verificações durante a execução.
