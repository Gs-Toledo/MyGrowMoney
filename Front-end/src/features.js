import flagsmith from 'flagsmith';

await flagsmith.init({
    environmentID: 'jtDu5Dr22myxztrApPfUNH',
    identity: Math.random(),
    cacheFlags: false,
    enableAnalytics: true,
});

export function isImportTransactionsEnabled () {
    return flagsmith.hasFeature('import-transactions');
}

export function getDashboardValue () {
    return flagsmith.getValue('dashboard');
}