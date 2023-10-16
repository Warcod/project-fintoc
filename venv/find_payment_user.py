import csv

def get_payment_info_from_csv(amount, csv_file):
    payment_info = None
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if float(row['amount']) == amount:
                payment_info = {
                    "amount": row['amount'],
                    "user": row['user']
                }
                break
    return payment_info

# Ejemplo de uso
amount = 1200000  # Ingresa el monto que estás buscando
csv_file = 'csv-inic-pagos.csv'  # Reemplaza esto con la ruta real de tu archivo CSV

payment_info = get_payment_info_from_csv(amount, csv_file)

if payment_info:
    print("Información de pago encontrada:")
    print(payment_info)
else:
    print("No se encontró información para el monto especificado en el archivo CSV.")
