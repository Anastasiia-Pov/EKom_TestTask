import requests
import json
import sys

# Ввод списка полей со значениями через двоеточие (пример: user:2), чтобы остановить ввод - cmd + D
incoming_forms = dict([line.strip().split(':') for line in sys.stdin])

# Преобразование входных данных в query-параметры
query_params = '&'.join(f"{k}={v}" for k, v in incoming_forms.items())
result = requests.post(f'http://127.0.0.1:8000/get_form/?{query_params}')
to_process = result.json()
if isinstance(to_process, list):
    print(to_process)
else:
    print(json.dumps(to_process, sort_keys=True, indent=4))
