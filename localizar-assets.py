#!/usr/bin/env python3
"""
Baixa todas as imagens hospedadas no CDN da Wix para ./assets e reescreve
o index.html para apontar para os arquivos locais.

Use quando quiser um deck 100% autocontido (offline, ou imune a mudanças
na conta Wix). Rode a partir da raiz do projeto:

    python3 scripts/localizar-assets.py

Faz backup de index.html em index.html.bak antes de reescrever.
"""
import hashlib, os, re, shutil, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "index.html")
OUT  = os.path.join(ROOT, "assets")

def main():
    html = open(HTML, encoding="utf-8").read()
    urls = sorted(set(re.findall(r'https://static\.wixstatic\.com/[^"\')\s]+', html)))
    if not urls:
        print("Nenhuma imagem remota encontrada. Nada a fazer.")
        return
    os.makedirs(OUT, exist_ok=True)
    shutil.copy(HTML, HTML + ".bak")
    print(f"{len(urls)} imagens encontradas. Backup em index.html.bak\n")

    for n, url in enumerate(urls, 1):
        ext = ".jpg" if url.rstrip("/").lower().endswith((".jpg", ".jpeg")) else ".png"
        name = hashlib.sha1(url.encode()).hexdigest()[:12] + ext
        dest = os.path.join(OUT, name)
        if not os.path.exists(dest):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=45) as r, open(dest, "wb") as f:
                    shutil.copyfileobj(r, f)
            except Exception as e:
                print(f"  [{n}/{len(urls)}] FALHOU {url[:70]}… -> {e}")
                continue
        kb = os.path.getsize(dest) // 1024
        print(f"  [{n}/{len(urls)}] {name}  {kb} KB")
        html = html.replace(url, "assets/" + name)

    # preconnect ao CDN deixa de ser necessário
    html = html.replace('<link rel="preconnect" href="https://static.wixstatic.com" crossorigin>\n', "")
    open(HTML, "w", encoding="utf-8").write(html)
    print("\nPronto. index.html agora aponta para ./assets")

if __name__ == "__main__":
    sys.exit(main())
