module.exports = {
    name: "no-fetch",
    timeout: 5000,
    async execute(browser, url) {
        const page = await browser.newPage();
        await page.setCookie({
            name: "noflag",
            value: process.env.CHALL_NO_FETCH_COOKIE|| "secret",
            domain: process.env.CHALL_NO_FETCH_DOMAIN || "localhost:9090",
        });
        await page.goto(url);
        await page.waitForNetworkIdle({
            timeout: 5000,
        });
        await page.close();
    },
};
