function open_hash() {
    const hash = document.getElementById('input_hash').value;

    if (hash == ""){
        return NaN
    }
    return window.location.href = `/p/${hash}`;
};