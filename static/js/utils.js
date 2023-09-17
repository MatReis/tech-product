function addMaskMoney(value) {
    value = value.replace(/\D/g, '');
    value = (parseFloat(value) / 100).toFixed(2).toString().replace('.', ',');
    return `R$ ${value}`;
}

function removeMaskMoney(str) {
    const number = str.replace(/\D/g, '');
    return parseFloat((parseFloat(number) / 100).toFixed(2));
}