import json

if __name__ == "__main__":
    with open("helper.txt", "r") as f:
        lines = f.readlines()

    email = ""
    summary = ""
    is_summary = False
    for line in lines:
        if line == "Summary:\n":
            is_summary = True
        elif is_summary:
            summary += line        
        else:
            email += line

    d = {}
    d["email"] = email[:len(email) - 1]
    d["summary"] = summary 
    text = json.dumps(d, indent = None)

    with open("" , "a" ) as f:
        f.write(text + "\n")
