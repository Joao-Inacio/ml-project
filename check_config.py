from airflow.configuration import conf

print("--- DIAGNÓSTICO AIRFLOW ---")
print(f"Pasta de DAGs: {conf.get('core', 'dags_folder')}")
print(f"Carregar Exemplos?: {conf.get('core', 'load_examples')}")
print("---------------------------")
