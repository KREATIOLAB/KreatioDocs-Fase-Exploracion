# pizza.py

def hacer_pizza(*ingredientes):
    """Imprime los ingredientes que se han solicitado para la pizza."""
    print("\nHaciendo una pizza con los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")
