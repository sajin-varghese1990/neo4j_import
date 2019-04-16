'''
modify the below query in Load data from CSV static method according to the data you need to import,
add node and relationship properties based on the remote data
'''


from neo4j import GraphDatabase


class HelloWorldExample(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    def load_data_csv(self, remotepath):
        with self._driver.session() as session:
            load_data = session.write_transaction(self._load_data_from_remote_csv, remotepath)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

    @staticmethod
    def _load_data_from_remote_csv(tx, remotepath):
        result = tx.run("LOAD CSV FROM $rpath AS line "
                        "CREATE (:Genre { GenreId: line[0], Name: line[1]}) ", rpath=remotepath)
        return result



