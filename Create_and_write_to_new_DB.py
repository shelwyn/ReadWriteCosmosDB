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

# Create a database
db = client.CreateDatabase({'id': config['DATABASE']})
# Create container options
options = {
    'offerThroughput': 400
}

container_definition = {
    'id': config['CONTAINER']
}

# Create a container
container = client.CreateContainer(db['_self'], container_definition, options)

# Create and add some items to the container
item1 = client.CreateItem(container['_self'], {
    'id': '61',
    'message': 'First-Message!'
    }
)

item2 = client.CreateItem(container['_self'], {
    'id': '42',
    'message': 'Second-Message!'
    }
)

# Query these items in SQL
query = {'query': 'SELECT * FROM server s'}
options = {}
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

result_iterable = client.QueryItems(container['_self'], query, options)
for item in iter(result_iterable):
    print(item['message'])
