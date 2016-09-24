from Machine import Machine

if __name__ == "__main__":
    machina = Machine()
    machina.initialise(20)
    while True:
        machina.cycle()
        print(machina)
        input()
