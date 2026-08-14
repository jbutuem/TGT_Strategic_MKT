# TGT Studio — Apresentação Comercial 2026

Deck comercial em página única. Sem build, sem dependências, sem framework.
Um arquivo (`index.html`) que roda igual em `file://`, em servidor estático e na Vercel.

**Tese:** posicionar a TGT como marketing estratégico com execução medida e processo proprietário — sem soar comercial. A apresentação não *fala* sobre neurociência: ela é **construída** com neurociência e revela a própria engenharia no capítulo 14. O pitch vira demonstração.

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

| # | Capítulo | Função |
|---|---|---|
| 00 | Capa | tese em três linhas |
| 01 | O filme | movimento antes do argumento (Vimeo `1088705362`) |
| 02 | A pergunta | abre o loop que só fecha no cap. 14 |
| 03 | O terreno | fluência · exposição · memória |
| 04 | O problema | fragmentação como carga cognitiva |
| 05 | Manifesto | identidade e tom de voz do brand guideline |
| 06 | Como fazemos | CX · Entregas · Eficiência |
| 07 | A arquitetura | Estratégia → Execução → Ativação |
| 08 | O escopo | 7 frentes de serviço |
| 09 | Os números | 8 KPIs medidos no HUB |
| 09.1 | Onde vai o tempo | horas por disciplina |
| 10 | O HUB | o processo disruptivo, aberto por dentro |
| 11 | Criação × aplicação | a régua com base em literatura |
| 12 | O trabalho | esteira de portfólio (pico visual) |
| 13 | Quem confia | logos + Google Partner |
| 13.5 | A virada | tela vermelha isolada |
| 14 | O blueprint | a revelação — fecha o loop |
| 15 | O convite | pergunta, não proposta |

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

## Referências citadas no deck

Sokolov (1963) · Zeigarnik (1927) · Von Restorff (1933) · Miller (1956) · Zajonc (1968) · Tversky & Kahneman (1974) · Slamecka & Graf (1978) · Kahneman & Tversky (1979) · Newell & Rosenbloom (1981) · Cialdini (1984) · Sweller (1988) · Kahneman, Fredrickson, Schreiber & Redelmeier (1993) · Aronson & Mills (1959) · Green & Brock (2000) · Cowan (2001) · Reber, Schwarz & Winkielman (2004) · Norton, Mochon & Ariely (2012) · Beaty, Benedek, Silvia & Schacter (2016)

Todas verificáveis. Se um cliente pedir a fonte, ela está na tela.

---

TGT Studio · Campinas / SP · desde 2005
