import axiosMyGrowMoney from '@/services/axios-configs';

export default class CsvHandler {

    static async importCsv(formData) {

        try {
            const response = await axiosMyGrowMoney.post('/import-transactions', formData);
            return response.data
        } catch (error) {
            throw new Error(`Erro ao importar CSV: ${error.message}`);
        }
    }


    static exportCsv(jsonData, fileName = "resumo-financeiro.csv") {

        if (!Array.isArray(jsonData) || jsonData.length === 0) {
            throw new Error("Os dados fornecidos não são válidos para exportação.");
        }

        const headers = Object.keys(jsonData[0]);

        const csvContent = [
            headers.join(";"), // Adicionar cabeçalhos como a primeira linha
            ...jsonData.map(row => headers.map(header => JSON.stringify(row[header] || "")).join(";")) // Adicionar os valores
        ].join("\n");

        // Criar o arquivo blob e disparar o download
        const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
        const link = document.createElement("a");

        const url = URL.createObjectURL(blob);
        link.setAttribute("href", url);
        link.setAttribute("download", fileName);
        link.style.visibility = "hidden";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}
