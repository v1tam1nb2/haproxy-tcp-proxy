from clickhouse_driver import Client

client = Client(host='localhost', port=9000)

print(client.execute('SHOW DATABASES'))
