import csv

def get_payment_info_from_csv(amount):
    payment_info_list = []
    csv_file = 'csv-inic-pagos.csv'
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if float(row['amount']) == amount:
                payment_info = {
                    "amount": row['amount'],
                    "user": row['user']
                }
                payment_info_list.append(payment_info)
    return payment_info_list

