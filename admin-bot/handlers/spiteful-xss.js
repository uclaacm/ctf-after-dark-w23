module.exports = {
    name: "spiteful-xss",
    timeout: 5000,
    async execute(browser, url) {
        const page = await browser.newPage();
        await page.setCookie({
            name: "adminpw",
            value: process.env.CHALL_SPITEFUL_XSS_ADMINPW || "secret",
            domain: process.env.CHALL_SPITEFUL_XSS_DOMAIN || "localhost:8080",
            httpOnly: true,
        });
        await page.goto(url);
        await new Promise(r => setTimeout(r, 5000));
        await page.close();
    },
};
