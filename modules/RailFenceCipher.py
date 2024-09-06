def railFenceEncode(plaintext: str, rail_count: int = 2):
    if rail_count < 2:
        return "You need to have at least 2 rails."

    # Create a list for each rail
    rails = []

    # We start at 1 because this statement is basically
    # for (int i = 1; i < rail_count; ++i)
    for i in range(0, rail_count):
        rails.append("")

    # Now we iterate through the plain text and add each character to the appropriate rail
    # These variables will be used to go up and down the rail list
    rail_index = 0
    rail_len = len(rails)
    go_down = True
    for char in plaintext:
        rails[rail_index] += char
        # code for moving up and down the rails
        if go_down:
            rail_index += 1
            # after going down a rail, we check if there is another rail below that one
            # if there is, we change the direction we'll be moving along the rails
            if rail_index + 1 >= rail_len:
                go_down = False
        else:
            rail_index -= 1
            # Basically the same as the code above, just going the opposite direction
            if rail_index - 1 < 0:
                go_down = True

    output = ""
    for rail in rails:
        output += rail

    return output

def railFenceDecode(ciphertext: str, rails: int = 2):
    pass