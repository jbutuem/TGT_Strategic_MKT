# TGT Studio — Apresentação Comercial 2026

> ## ⚠️ ANTES DE MANDAR NO WHATSAPP — 1 comando
>
> Depois do deploy, troque o domínio na tag de preview. Sem isso o card do WhatsApp
> não mostra imagem:
>
> ```bash
> sed -i '' 's|https://SEU-DOMINIO.vercel.app|https://SEU-DOMINIO-REAL.vercel.app|g' index.html
> git commit -am "og: dominio real" && git push
> ```
>
> Teste o card em <https://developers.facebook.com/tools/debug/> colando a URL e
> clicando em **Scrape Again**. O WhatsApp usa o mesmo cache da Meta — se você
> mandar o link antes de corrigir, o preview quebrado fica em cache por horas.


Deck comercial em página única. Sem build, sem dependências, sem framework.
Um arquivo (`index.html`) que roda igual em `file://`, em servidor estático e na Vercel.

**Tese:** posicionar a TGT como marketing estratégico com execução medida e processo proprietário — sem soar comercial. A apresentação não *fala* sobre neurociência: ela é **construída** com neurociência e revela a própria engenharia no capítulo 14. O pitch vira demonstração.

---

## Otimizado para envio por WhatsApp

O deck é um link frio aberto no celular. O que foi feito por causa disso:

- **`og.jpg` 1200×630, 104 KB** — imagem de preview própria, na marca, gerada para o card grande do WhatsApp. A anterior era quadrada e de 703 KB (virava miniatura).
- **`robots.txt` libera os robôs de preview** (`facebookexternalhit`, `WhatsApp`, `Twitterbot`, `LinkedInBot`, `TelegramBot`, `Slackbot`) e continua bloqueando buscadores. O `Disallow: /` geral sozinho impedia o card de renderizar.
- **Capa reordenada no celular:** headline e subtítulo cabem na primeira tela; a ilustração entra depois, reduzida. A composição empurrava o texto para fora da dobra.
- **Sem dependência de mouse:** o portfólio abre quase em cor em telas de toque e responde ao toque; textos que diziam "passe o mouse" e "tecla N" foram reescritos ou escondidos.
- **O botão "Camada neuro" fica oculto no celular** até o leitor chegar no capítulo 14. Num link frio ele era ruído logo na abertura.
- **Peso real: 327 KB até o primeiro paint, 677 KB a página inteira** (42 requisições). O CDN da Wix entrega AVIF; não precisou otimizar imagem.

---

## Deploy

### Git + Vercel (recomendado)

```bash
cd tgt-apresentacao
git init && git add -A && git commit -m "TGT — apresentação comercial 2026"
git branch -M main
git remote add origin git@github.com:jbutuem/tgt-apresentacao.git
git push -u origin main
```

Na Vercel: **Add New → Project → Import** o repositório.
Framework Preset: **Other**. Build Command: *vazio*. Output Directory: *vazio* (raiz).
Não existe `package.json` de propósito — assim a Vercel não tenta rodar build.

### Ou direto pela CLI, sem Git

```bash
npx vercel --prod
```

Domínio sugerido: `tgt-apresentacao.vercel.app` ou um subdomínio próprio
(`apresentacao.tgtstudio.com.br` via CNAME).

---

## Como se apresenta

| Ação | Atalho |
|---|---|
| Avançar capítulo | `→` `↓` `Espaço` `PageDown` |
| Voltar capítulo | `←` `↑` `PageUp` |
| Primeiro / último | `Home` / `End` |
| **Ligar a camada neuro** | `N` (ou o botão no topo direito) |
| Pular para um capítulo | trilha de traços na lateral direita |

Em tela cheia (`F11` / `⌃⌘F`) o comportamento é de deck: uma tela por capítulo, com encaixe.
No celular vira scroll contínuo. O filme do Vimeo só carrega quando alguém clica — a abertura não paga o custo do player.

### A camada neuro

O botão **Camada neuro** abre, na margem de cada tela, o princípio que sustenta aquele capítulo e a referência de origem. Fica **desligada por padrão** — o cliente precisa sentir antes de entender. Ligue quando a conversa merecer, ou deixe o próprio cliente ligar no capítulo 14. A preferência fica salva em `localStorage`.

---

## Estrutura

---

## Revisão de UX / UI e neuromarketing

Auditoria feita medindo no navegador, não a olho. O que mudou:

**Tipografia.** Havia oito elementos entre 10 e 11 px e corpo em peso 300 sobre fundo escuro — em tela escura a halação afina o traço e peso 300 vira cinza. Piso novo: **15 px no corpo, 12 px em rótulo, peso 400 em tudo.** Nenhum tipo abaixo de 12 px na superfície.

**Contraste.** O vermelho da marca (`#ED1C24`) sobre o preto institucional dá **3,7:1** — reprova em texto pequeno pela WCAG AA. Entrou `--red-lt` (`#FF5A61`, **5,3:1**) só para tipo miúdo; o vermelho puro segue nos números grandes e nas áreas de cor, onde 3,7:1 basta. A palavra-chave em vermelho no topo de cada capítulo virou creme com marcador vermelho.

**Alvos de toque.** Os links de contato tinham 19 px de altura. Todos passaram para **48 px**; o botão da camada neuro, para 44 px. Zero alvos abaixo do mínimo em qualquer largura de celular.

**Conteúdo: de 1.884 para 1.358 palavras (−28%), 8,4 → 6,8 min.**
- **Capítulo 07 (Estratégia → Execução → Ativação) saiu.** Era o trecho mais genérico do deck e repetia o escopo. Virou uma linha na abertura do capítulo seguinte.
- **As citações acadêmicas saíram da superfície** e foram para a camada neuro. Elas custavam fluência — justo o que o deck afirma otimizar — e eram o menor tipo da página. Contradição interna resolvida: quem quiser a fonte liga a camada.
- Todo parágrafo foi reduzido a no máximo três linhas.
- A lista de 15 clientes virou 8 nomes + "e mais 17 contas".

**Larguras testadas:** 320 · 360 · 390 · 430 · 768 · 1440 · 1920, com a camada neuro ligada e desligada. Zero overflow, zero corte.

---

## De onde vêm os números

Consulta direta ao **HUB / Supabase `opqivuzvyvvvajokutvc`**, janela **04/05/2026 → 14/08/2026**, com `auto_closed IS NOT TRUE` e `COALESCE(started_at, created_at)` para a data.

| No deck | Valor | Origem |
|---|---|---|
| Horas de execução | 8.083 h | `SUM(hours)` em `tt_time_entries` |
| Registros | 11.032 | `COUNT(*)` em `tt_time_entries` |
| Entregáveis únicos | 387 | `COUNT(DISTINCT monday_item_name)` |
| Contas ativas | 25 | `tt_clients` ativos, excluindo internos |
| Desvio entre meses | 1,6% | CV de mai/jun/jul (2.321 · 2.389 · 2.407 h) |
| Média por entregável | 2,8 h | média de horas por `monday_item_id` |
| Boards integrados | 25 | `COUNT(DISTINCT monday_board_id)` |
| Anos de operação | 21 | CNPJ 07.374.802/0001-00, fundação 18/04/2005 |
| Horas por disciplina | cap. 09.1 | `GROUP BY action` |

**Dois pontos para você confirmar antes de mandar para cliente:**

1. **"31 pessoas"** (capa) vem de `tt_members` ativos. Se o headcount real for outro, ajuste na capa — é o único número do deck que não sai limpo de uma consulta.
2. **Fee sob gestão** existe na base (`SUM(fee_monthly)`) e foi **deliberadamente deixado de fora**. Expor receita da agência num deck comercial trabalha contra a negociação. Se quiser incluir em alguma versão específica, o campo está lá.

Para atualizar: rode a consulta, troque os `data-count` no capítulo 09 e os `data-w` das barras no 09.1. O contador anima sozinho.

---

## Identidade

Tudo derivado do **Brand Guideline TGT 2025**.

```
--ink    #231F20    preto institucional
--red    #ED1C24    vermelho TGT
--cream  #E2DBCE    creme institucional
--slate  #455E6E    azul-ardósia (usado uma única vez, no cap. 09.1)
--g1/g2/g3  #575756 · #9D9D9C · #D0D0D0
```

**Tipografia.** O guideline pede **Acumin Pro** (títulos) + **Montserrat** (corpo).
Acumin Pro é Adobe Fonts e não tem versão web livre, então o deck usa **Archivo** como substituta — mesma família neo-grotesca, mesmas larguras e pesos, diferença imperceptível em display. Montserrat é a original. Dados e a camada neuro usam **IBM Plex Mono**, o mesmo mono do sistema de relatórios da casa.

**Para trocar pela Acumin Pro de verdade:** crie um Web Project no Adobe Fonts, autorize o domínio da Vercel e substitua o `<link>` do Google Fonts pelo do kit Adobe. A variável `--display` já lista `'Acumin Pro'` como segunda opção — assim que a fonte carregar, ela assume sozinha, sem mexer em mais nada.

---

## Assets

Imagens (logo, composições, portfólio, logos de cliente, selo Google) são servidas do CDN da Wix da própria conta da TGT — mesma origem do site.

Se quiser o deck 100% autocontido:

```bash
python3 scripts/localizar-assets.py
```

Baixa tudo para `./assets`, reescreve os caminhos no `index.html` e guarda backup em `index.html.bak`. Só depende da biblioteca padrão do Python.

---

## Detalhes que valem saber

- **Fora do índice de busca por padrão.** `meta robots noindex` + `robots.txt Disallow`. É um link para prospect, não uma landing — e não faz sentido competir com `tgtstudio.com.br` no Google. Para publicar de verdade, remova a meta no `<head>` e troque o `robots.txt`.
- **Imprime.** `Ctrl/⌘ + P` gera um capítulo por página, sem trilha nem botões.
- **Acessível.** Navegação por teclado, foco visível, `alt` em imagem de conteúdo, `prefers-reduced-motion` respeitado (contadores param, esteira do portfólio vira scroll manual).
- **Leve.** Zero JavaScript de terceiros. O player do Vimeo só entra na página quando clicado.

---

## Testado em navegador real

Renderizado no Chromium headless em 375 / 390 / 430 / 768 / 1440 / 1920 px, com a camada neuro ligada e desligada. Verificado: zero overflow horizontal, zero conteúdo cortado por `overflow:hidden`, contadores e barras animando, esteira do portfólio em loop, fontes carregando.

Extensão real: **~1.880 palavras** com a camada neuro desligada (≈ 9 min de leitura) e ~2.460 com ela ligada. No celular são ~18.000 px de rolagem — 18 capítulos, média de 1 tela cada.

**Nota de manutenção:** o bloco `@media (max-width:880px)` fica no **fim** da folha de estilo de propósito. Vários `.g2` têm `grid-template-columns` inline (estilo inline só perde para `!important`, e regra de mesma especificidade só é vencida por ordem). Se mover esse bloco para cima, o mobile quebra em silêncio — o excesso é cortado por `overflow:hidden` em vez de gerar barra de rolagem.

---

## Contato no deck (cap. 15)

E-mail `contato@tgtstudio.com.br` · Direto **Sonia · +55 19 99163-0294** (link `wa.me/5519991630294`) · Site · Instagram.
Para trocar, edite o bloco `.contact` no capítulo 15 — o botão "Marcar uma conversa" usa o mesmo e-mail.

---

## Referências citadas no deck

Sokolov (1963) · Zeigarnik (1927) · Von Restorff (1933) · Miller (1956) · Zajonc (1968) · Tversky & Kahneman (1974) · Slamecka & Graf (1978) · Kahneman & Tversky (1979) · Newell & Rosenbloom (1981) · Cialdini (1984) · Sweller (1988) · Kahneman, Fredrickson, Schreiber & Redelmeier (1993) · Aronson & Mills (1959) · Green & Brock (2000) · Cowan (2001) · Reber, Schwarz & Winkielman (2004) · Norton, Mochon & Ariely (2012) · Beaty, Benedek, Silvia & Schacter (2016)

Todas verificáveis. Se um cliente pedir a fonte, ela está na tela.

---

TGT Studio · Campinas / SP · desde 2005
