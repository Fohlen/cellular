from Machine import Machine

if __name__ == "__main__":
    machina = Machine()
    machina.initialise(20)
    try:
        while True:
            machina.cycle()
            print(machina)
            input()
    except KeyboardInterrupt:
        del machina
