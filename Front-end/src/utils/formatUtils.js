export function formatDateFromIso(isoDate) {
    if (!isoDate) return ''

    const date = new Date(isoDate)
    const day = String(date.getDate()).padStart(2, '0')
    const month = String(date.getMonth() + 1).padStart(2, '0')
    const year = date.getFullYear()

    return `${day}/${month}/${year}`
}

export function formatNumberToMoneyDouble(value) {

    if (isNaN(value)) return '0,00';

    return Number.parseFloat(value)
        .toFixed(2)
        .replace('.', ',')
        .replace(/\B(?=(\d{3})+(?!\d))/g, '.');
}

export function formatToLocaleBr(value) {
    try {
        const valorFormatado = value.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
        return valorFormatado
    } catch (error) {
        return null
    }
}