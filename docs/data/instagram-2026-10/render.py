import asyncio
from playwright.async_api import async_playwright
SP="docs/data/instagram-2026-10"  # 実行時はこのディレクトリに cd してパスを絶対に直すこと
SPKI=open(SP+'/../spki.txt').read().strip()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
            args=['--no-sandbox', f'--ignore-certificate-errors-spki-list={SPKI}'])
        pg=await (await b.new_context(viewport={'width':1080,'height':1350},device_scale_factor=1)).new_page()
        await pg.goto(f"file://{SP}/slides.html", wait_until='networkidle', timeout=60000)
        await pg.wait_for_timeout(2500)
        fam = await pg.evaluate("""() => { const d=document.createElement('span'); d.style.font='700 40px "Noto Sans JP"';
          d.textContent='あ'; document.body.appendChild(d); const w1=d.offsetWidth;
          d.style.font='700 40px "IPAGothic"'; const w2=d.offsetWidth; d.remove();
          return {noto:w1, ipa:w2, loaded: document.fonts.check('700 40px "Noto Sans JP"')}; }""")
        print("font:", fam)
        for i in range(1,7):
            await (await pg.query_selector(f"#s{i}")).screenshot(path=f"{SP}/size-guide-{i}.png")
        print("rendered")
        await b.close()
asyncio.run(main())
