import numerapi

napi = numerapi.NumerAPI(verbosity="info")
current_ds = napi.get_current_round()

print('Current round: ',current_ds)