#PLEASE INSTALL [pip3 install azure-cosmos] IF NOT INSTALLED ALREADY

import azure.cosmos.cosmos_client as cosmos_client

config = {
    'ENDPOINT': '{YOUR-AZURE-COSMOS-ENDPOINT}',
    'PRIMARYKEY': '{YOUR-AZURE-COSMOS-PRIMARY-KEY}',
    'DATABASE': '{DATABASE-NAME}',
    'CONTAINER': '{CONTAINER-NAME}'
}

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                    'masterKey': config['PRIMARYKEY']})

# Connect to the database and read container
database_link = 'dbs/' + config['DATABASE']
db = client.ReadDatabase(database_link)
collection_link = database_link + '/colls/{0}'.format(config['CONTAINER'])
collection = client.ReadContainer(collection_link)

# Create and add some items to the container
item1 = client.CreateItem(collection['_self'], {
    'id': 2,
    'message': 'Hello CosmosDB!'
    }
)

# Query added items in SQL
query = {'query': 'SELECT * FROM server s'}
options = {}
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

result_iterable = client.QueryItems(collection['_self'], query, options)
for item in iter(result_iterable):
    try:
        print(item['message'])
    except:
        print('')
