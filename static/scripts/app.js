function get_hash() {
    const currentUrl = window.location.href;
    hash = currentUrl.split("p/")[1];
    link = `https://t.me/dmmebaby_bot?start=${hash}`
    return window.open(link);
};

function open_hash() {
    const hash = document.getElementById('input_hash').value;
    let link = `http://400-cards.ru/p/${hash}`;
    return window.open(link);
};