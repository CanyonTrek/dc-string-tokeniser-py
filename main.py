from app.string_tokeniser import StringTokeniser

def main():
    input_text = "john cleese,michael palin,chapman"
    tokeniser = StringTokeniser()
    tokens = tokeniser.tokenise(input_text)
    print("Tokens:", tokens)

if __name__ == "__main__":
    main()

