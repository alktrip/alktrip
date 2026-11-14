import sys,asyncio
from playwright.async_api import async_playwright
async def main(src,out,w,h,scale):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':w,'height':h},device_scale_factor=scale)
        await pg.goto('file://'+src); await pg.wait_for_timeout(400)
        el=await pg.query_selector('#c')
        await el.screenshot(path=out,omit_background=True)
        await b.close()
asyncio.run(main(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),float(sys.argv[5])))
