from flagsmith import Flagsmith

flagsmith = Flagsmith(
    environment_key="jtDu5Dr22myxztrApPfUNH",
)

def is_import_transactions_enabled():
    flags = flagsmith.get_environment_flags()

    return flags.is_feature_enabled("import-transactions")