const mesesDict = {
    "1": "Jan", "2": "Fev", "3": "Mar", "4": "Abr", "5": "Mai", "6": "Jun",
    "7": "Jul", "8": "Ago", "9": "Set", "10": "Out", "11": "Nov", "12": "Dez"
}

export function getCurrentDateFormated() {
    const dataAtual = new Date(); 

    const dia = dataAtual.getDate();
    const mes = dataAtual.getMonth() + 1; // Mês começa em 0
    const ano = dataAtual.getFullYear();

    const diaFormatado = String(dia).padStart(2, '0');
    const mesFormatado = String(mes).padStart(2, '0');

    return `${diaFormatado}/${mesFormatado}/${ano}`;
}

export function getCurrentMonthName() {
    const dataAtual = new Date()
    const mes = dataAtual.getMonth() + 1
    return mesesDict[mes]
}

export function getCurrentYear() {
    const dataAtual = new Date()
    const ano = dataAtual.getFullYear()

    return ano
}