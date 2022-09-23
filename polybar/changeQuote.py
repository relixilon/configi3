with open("/home/mario/.config/i3/polybar/symbols.txt", "r") as symbols:
    hold = symbols.readline().strip("\n")
    with open("/home/mario/.config/i3/polybar/symbols.txt", "w") as output:
        for line in symbols:
            if line.strip("\n") != hold:
                output.write(line)
        output.write("\n"+hold)
