def format_string(input_str):
    lines = input_str.strip().split('\n')
    formatted_lines = []
    all_vars = []

    for line in lines:
        parts = line.split(' - ')
        if len(parts) == 2:
            var_name = parts[0].strip()
            formatted_lines.append(f"{var_name} = '{var_name}'")
            all_vars.append(var_name)

    # Adding ALL array at the bottom
    all_vars_str = f"ALL = [{', '.join(all_vars)}]"
    print('\n'.join(formatted_lines) + '\n' + all_vars_str)

format_string("""
ID - String
Link - String
Name - String
N - Integer
Country - String
Role - String
IsSubstitute - String
IsTrainee - String
Team - String
ContractDate - Date
Residency - String
              """)