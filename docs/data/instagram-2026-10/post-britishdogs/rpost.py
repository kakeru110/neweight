import asyncio
from playwright.async_api import async_playwright
SP="/tmp/claude-0/-home-user-neweight/531e02c7-808a-5e4a-b97e-cb6efa091c0d/scratchpad/sg"
SPKI=open(SP+'/../spki.txt').read().strip()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
            args=['--no-sandbox', f'--ignore-certificate-errors-spki-list={SPKI}'])
        pg=await (await b.new_context(viewport={'width':1100,'height':1400})).new_page()
        await pg.goto(f"file://{SP}/post.html", wait_until='networkidle', timeout=60000)
        await pg.wait_for_timeout(2500)
        for i in range(2,7):
            await (await pg.query_selector(f"#p{i}")).screenshot(path=f"{SP}/post-{i}.png")
        print("ok"); await b.close()
asyncio.run(main())
